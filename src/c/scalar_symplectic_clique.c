/*
 * Exact maximum-clique upper certificates for odd-prime scalar symplectic
 * graphs.  The program uses only ISO C plus the compiler's 64-bit popcount.
 *
 * For rank at least two, point/pair transitivity and the four explicitly
 * enumerated stabilizer orbits reduce every clique of size at least three to
 * one containing e_1, f_1, and one of
 *
 *   e_1 + t f_1,          e_1 + e_2 + t f_1,
 *
 * where t is either a square or a nonsquare.  Each residual graph is then
 * searched exactly by the Tomita greedy-color branch-and-bound recurrence.
 * A separately checked clique supplies the lower bound passed on the command
 * line; this program exhaustively proves that no larger clique exists.
 *
 * Usage: scalar_symplectic_clique PRIME RANK KNOWN_LOWER_BOUND
 */

#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_VERTICES 1024
#define MAX_DIMENSION 12
#define MAX_WORDS (MAX_VERTICES / 64)

typedef struct {
    uint64_t word[MAX_WORDS];
} Bitset;

static int prime_value;
static int rank_value;
static int dimension_value;
static int vertex_count;
static int word_count;
static int full_word_count;
static int vectors[MAX_VERTICES][MAX_DIMENSION];
static Bitset full_adjacency[MAX_VERTICES];

static int residual_count;
static int residual_to_full[MAX_VERTICES];
static Bitset residual_adjacency[MAX_VERTICES];
static int best_size;
static int best_vertices[MAX_VERTICES];
static int current_vertices[MAX_VERTICES];
static uint64_t search_nodes;
static int stop_after_improvement;
static int emit_improved_clique;

static void bitset_zero(Bitset *set) {
    memset(set, 0, sizeof(*set));
}

static void bitset_fill_prefix(Bitset *set, int count) {
    int word;
    bitset_zero(set);
    for (word = 0; word < (count + 63) / 64; ++word) {
        set->word[word] = UINT64_MAX;
    }
    if (count % 64) {
        set->word[count / 64] = (UINT64_C(1) << (count % 64)) - 1;
    }
}

static int bitset_empty(const Bitset *set) {
    int word;
    for (word = 0; word < word_count; ++word) {
        if (set->word[word]) {
            return 0;
        }
    }
    return 1;
}

static int bitset_popcount(const Bitset *set) {
    int total = 0;
    int word;
    for (word = 0; word < word_count; ++word) {
        total += __builtin_popcountll(set->word[word]);
    }
    return total;
}

static int bitset_first(const Bitset *set) {
    int word;
    for (word = 0; word < word_count; ++word) {
        if (set->word[word]) {
            return 64 * word + __builtin_ctzll(set->word[word]);
        }
    }
    return -1;
}

static int bitset_contains(const Bitset *set, int vertex) {
    return (int)((set->word[vertex / 64] >> (vertex % 64)) & UINT64_C(1));
}

static void bitset_add(Bitset *set, int vertex) {
    set->word[vertex / 64] |= UINT64_C(1) << (vertex % 64);
}

static void bitset_remove(Bitset *set, int vertex) {
    set->word[vertex / 64] &= ~(UINT64_C(1) << (vertex % 64));
}

static Bitset bitset_intersection(const Bitset *left, const Bitset *right) {
    Bitset result;
    int word;
    bitset_zero(&result);
    for (word = 0; word < word_count; ++word) {
        result.word[word] = left->word[word] & right->word[word];
    }
    return result;
}

static void bitset_subtract_adjacency(Bitset *set, const Bitset *neighbors) {
    int word;
    for (word = 0; word < word_count; ++word) {
        set->word[word] &= ~neighbors->word[word];
    }
}

static int modular_power(int base, int exponent, int modulus) {
    int64_t result = 1;
    int64_t factor = base % modulus;
    while (exponent) {
        if (exponent & 1) {
            result = result * factor % modulus;
        }
        factor = factor * factor % modulus;
        exponent >>= 1;
    }
    return (int)result;
}

static int inverse_mod_prime(int value) {
    return modular_power(value, prime_value - 2, prime_value);
}

static int symplectic_value(const int *left, const int *right) {
    int value = 0;
    int coordinate;
    for (coordinate = 0; coordinate < rank_value; ++coordinate) {
        value += left[coordinate] * right[rank_value + coordinate];
        value -= right[coordinate] * left[rank_value + coordinate];
    }
    value %= prime_value;
    return value < 0 ? value + prime_value : value;
}

static int vector_equal(const int *left, const int *right) {
    int coordinate;
    for (coordinate = 0; coordinate < dimension_value; ++coordinate) {
        if (left[coordinate] != right[coordinate]) {
            return 0;
        }
    }
    return 1;
}

static int find_vertex(const int *target) {
    int vertex;
    for (vertex = 0; vertex < vertex_count; ++vertex) {
        if (vector_equal(vectors[vertex], target)) {
            return vertex;
        }
    }
    return -1;
}

static void construct_projective_graph(void) {
    uint64_t total_vectors = 1;
    uint64_t code;
    int coordinate;
    int vertex;

    for (coordinate = 0; coordinate < dimension_value; ++coordinate) {
        total_vectors *= (uint64_t)prime_value;
    }
    vertex_count = 0;
    for (code = 1; code < total_vectors; ++code) {
        uint64_t value = code;
        int raw[MAX_DIMENSION];
        int first = -1;
        int inverse;
        for (coordinate = dimension_value - 1; coordinate >= 0; --coordinate) {
            raw[coordinate] = (int)(value % (uint64_t)prime_value);
            value /= (uint64_t)prime_value;
        }
        for (coordinate = 0; coordinate < dimension_value; ++coordinate) {
            if (raw[coordinate]) {
                first = coordinate;
                break;
            }
        }
        inverse = inverse_mod_prime(raw[first]);
        if (raw[first] != 1) {
            continue;
        }
        if (vertex_count >= MAX_VERTICES) {
            fprintf(stderr, "projective graph exceeds MAX_VERTICES\n");
            exit(2);
        }
        for (coordinate = 0; coordinate < dimension_value; ++coordinate) {
            vectors[vertex_count][coordinate] = raw[coordinate] * inverse % prime_value;
        }
        ++vertex_count;
    }
    word_count = (vertex_count + 63) / 64;
    full_word_count = word_count;
    for (vertex = 0; vertex < vertex_count; ++vertex) {
        int other;
        bitset_zero(&full_adjacency[vertex]);
        for (other = 0; other < vertex_count; ++other) {
            if (symplectic_value(vectors[vertex], vectors[other])) {
                bitset_add(&full_adjacency[vertex], other);
            }
        }
    }
}

static void color_sort(Bitset candidates, int *order, int *bounds, int *length) {
    Bitset remaining = candidates;
    int color = 0;
    *length = 0;
    while (!bitset_empty(&remaining)) {
        Bitset available = remaining;
        ++color;
        while (!bitset_empty(&available)) {
            int selected = -1;
            int selected_degree = -1;
            Bitset scan = available;
            while (!bitset_empty(&scan)) {
                int vertex = bitset_first(&scan);
                Bitset neighbors = bitset_intersection(&available, &residual_adjacency[vertex]);
                int degree = bitset_popcount(&neighbors);
                bitset_remove(&scan, vertex);
                if (degree > selected_degree || (degree == selected_degree && vertex < selected)) {
                    selected = vertex;
                    selected_degree = degree;
                }
            }
            order[*length] = selected;
            bounds[*length] = color;
            ++*length;
            bitset_remove(&remaining, selected);
            bitset_remove(&available, selected);
            bitset_subtract_adjacency(&available, &residual_adjacency[selected]);
        }
    }
}

static void expand_clique(int depth, Bitset candidates) {
    int order[MAX_VERTICES];
    int bounds[MAX_VERTICES];
    int length;
    ++search_nodes;
    if (stop_after_improvement >= 0 && best_size > stop_after_improvement) {
        return;
    }
    color_sort(candidates, order, bounds, &length);
    while (length) {
        int vertex;
        Bitset extension;
        --length;
        if (depth + bounds[length] <= best_size) {
            return;
        }
        vertex = order[length];
        current_vertices[depth] = vertex;
        extension = bitset_intersection(&candidates, &residual_adjacency[vertex]);
        if (!bitset_empty(&extension)) {
            expand_clique(depth + 1, extension);
            if (stop_after_improvement >= 0 && best_size > stop_after_improvement) {
                return;
            }
        } else if (depth + 1 > best_size) {
            int index;
            best_size = depth + 1;
            for (index = 0; index <= depth; ++index) {
                best_vertices[index] = current_vertices[index];
            }
        }
        bitset_remove(&candidates, vertex);
    }
}

static void construct_residual(const int *prefix, int prefix_length) {
    Bitset common;
    int full_vertex;
    int residual_vertex;
    int index;
    word_count = full_word_count;
    bitset_fill_prefix(&common, vertex_count);
    for (index = 0; index < prefix_length; ++index) {
        common = bitset_intersection(&common, &full_adjacency[prefix[index]]);
    }
    residual_count = 0;
    for (full_vertex = 0; full_vertex < vertex_count; ++full_vertex) {
        if (bitset_contains(&common, full_vertex)) {
            residual_to_full[residual_count++] = full_vertex;
        }
    }
    word_count = (residual_count + 63) / 64;
    for (residual_vertex = 0; residual_vertex < residual_count; ++residual_vertex) {
        int other;
        bitset_zero(&residual_adjacency[residual_vertex]);
        for (other = 0; other < residual_count; ++other) {
            if (bitset_contains(
                    &full_adjacency[residual_to_full[residual_vertex]],
                    residual_to_full[other])) {
                bitset_add(&residual_adjacency[residual_vertex], other);
            }
        }
    }
}

static double elapsed_seconds(clock_t start) {
    return (double)(clock() - start) / (double)CLOCKS_PER_SEC;
}

int main(int argc, char **argv) {
    int known_lower;
    int nonsquare = -1;
    int square_class;
    int nonzero_tail;
    int canonical_first[MAX_DIMENSION] = {0};
    int canonical_second[MAX_DIMENSION] = {0};
    int first_vertex;
    int second_vertex;
    int global_maximum;
    uint64_t total_nodes = 0;
    clock_t total_start = clock();

    if (argc != 4 && argc != 5) {
        fprintf(stderr, "usage: %s PRIME RANK KNOWN_LOWER_BOUND [find]\n", argv[0]);
        return 2;
    }
    prime_value = atoi(argv[1]);
    rank_value = atoi(argv[2]);
    known_lower = atoi(argv[3]);
    emit_improved_clique = argc == 5 && strcmp(argv[4], "find") == 0;
    dimension_value = 2 * rank_value;
    if (prime_value < 3 || prime_value % 2 == 0 || rank_value < 2 ||
        dimension_value > MAX_DIMENSION) {
        fprintf(stderr, "requires an odd prime and 2 <= rank <= %d\n", MAX_DIMENSION / 2);
        return 2;
    }
    for (square_class = 2; square_class < prime_value; ++square_class) {
        if (modular_power(square_class, (prime_value - 1) / 2, prime_value) == prime_value - 1) {
            nonsquare = square_class;
            break;
        }
    }
    if (nonsquare < 0) {
        fprintf(stderr, "failed to find a nonsquare; PRIME may not be prime\n");
        return 2;
    }

    construct_projective_graph();
    canonical_first[0] = 1;
    canonical_second[rank_value] = 1;
    first_vertex = find_vertex(canonical_first);
    second_vertex = find_vertex(canonical_second);
    if (first_vertex < 0 || second_vertex < 0 ||
        !bitset_contains(&full_adjacency[first_vertex], second_vertex)) {
        fprintf(stderr, "canonical adjacent pair was not constructed\n");
        return 2;
    }
    printf("graph prime=%d rank=%d projective_vertices=%d nonsquare=%d known_lower=%d\n",
           prime_value, rank_value, vertex_count, nonsquare, known_lower);
    global_maximum = known_lower;
    stop_after_improvement = emit_improved_clique ? known_lower - 3 : -1;

    for (nonzero_tail = 0; nonzero_tail <= 1; ++nonzero_tail) {
        for (square_class = 0; square_class <= 1; ++square_class) {
            int third_vector[MAX_DIMENSION] = {0};
            int prefix[3];
            int third_vertex;
            Bitset candidates;
            clock_t case_start;
            int local_maximum;

            third_vector[0] = 1;
            if (nonzero_tail) {
                third_vector[1] = 1;
            }
            third_vector[rank_value] = square_class ? nonsquare : 1;
            third_vertex = find_vertex(third_vector);
            prefix[0] = first_vertex;
            prefix[1] = second_vertex;
            prefix[2] = third_vertex;
            if (third_vertex < 0 ||
                !bitset_contains(&full_adjacency[first_vertex], third_vertex) ||
                !bitset_contains(&full_adjacency[second_vertex], third_vertex)) {
                fprintf(stderr, "canonical triple is not a clique\n");
                return 2;
            }
            construct_residual(prefix, 3);
            bitset_fill_prefix(&candidates, residual_count);
            best_size = known_lower - 3;
            if (!emit_improved_clique) {
                stop_after_improvement = -1;
            }
            search_nodes = 0;
            case_start = clock();
            expand_clique(0, candidates);
            local_maximum = best_size + 3;
            if (local_maximum > known_lower && emit_improved_clique) {
                int index;
                printf("improved_clique full_vertices=%d,%d,%d",
                       prefix[0], prefix[1], prefix[2]);
                for (index = 0; index < best_size; ++index) {
                    printf(",%d", residual_to_full[best_vertices[index]]);
                }
                printf("\n");
                fflush(stdout);
                return 3;
            }
            if (local_maximum > global_maximum) {
                global_maximum = local_maximum;
            }
            total_nodes += search_nodes;
            printf("case tail=%s scalar=%s residual_vertices=%d maximum_at_most=%d "
                   "search_nodes=%" PRIu64 " cpu_seconds=%.6f\n",
                   nonzero_tail ? "nonzero" : "zero",
                   square_class ? "nonsquare" : "square",
                   residual_count, local_maximum, search_nodes,
                   elapsed_seconds(case_start));
            fflush(stdout);
            /* Restore the full graph word count before constructing the next case. */
            word_count = full_word_count;
        }
    }
    printf("result maximum=%d total_search_nodes=%" PRIu64 " total_cpu_seconds=%.6f\n",
           global_maximum, total_nodes, elapsed_seconds(total_start));
    return 0;
}
