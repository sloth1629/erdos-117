/*
 * Exhaustive clique witnesses for every common-radical-zero pencil of
 * alternating forms on F_2^5.  This is the large-kernel obstruction in the
 * exterior-square reduction for a central quotient C_2^5.
 *
 * Build with:
 *   cc -O3 -std=c11 -Wall -Wextra -Werror h6_c2_5_pencils.c -o h6_pencils
 */

#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define FORM_COUNT 1024
#define VERTEX_COUNT 31
#define TARGET_CLIQUE 9

static uint16_t wedges[VERTEX_COUNT][VERTEX_COUNT];
static uint32_t adjacency[VERTEX_COUNT];
static uint64_t search_nodes;

static int popcount32(uint32_t value) {
    return __builtin_popcount(value);
}

static uint16_t wedge_vector(int x, int y) {
    uint16_t result = 0;
    int bit = 0;
    for (int i = 0; i < 5; ++i) {
        for (int j = i + 1; j < 5; ++j, ++bit) {
            int value = (((x >> i) & 1) & ((y >> j) & 1)) ^
                        (((x >> j) & 1) & ((y >> i) & 1));
            if (value) {
                result |= (uint16_t)(1U << bit);
            }
        }
    }
    return result;
}

static int alternating_rank(uint16_t form) {
    uint8_t rows[5] = {0, 0, 0, 0, 0};
    int bit = 0;
    for (int i = 0; i < 5; ++i) {
        for (int j = i + 1; j < 5; ++j, ++bit) {
            if (form & (uint16_t)(1U << bit)) {
                rows[i] |= (uint8_t)(1U << j);
                rows[j] |= (uint8_t)(1U << i);
            }
        }
    }
    int rank = 0;
    for (int column = 0; column < 5; ++column) {
        int pivot = -1;
        for (int row = rank; row < 5; ++row) {
            if (rows[row] & (uint8_t)(1U << column)) {
                pivot = row;
                break;
            }
        }
        if (pivot < 0) {
            continue;
        }
        uint8_t temporary = rows[rank];
        rows[rank] = rows[pivot];
        rows[pivot] = temporary;
        for (int row = 0; row < 5; ++row) {
            if (row != rank && (rows[row] & (uint8_t)(1U << column))) {
                rows[row] ^= rows[rank];
            }
        }
        ++rank;
    }
    return rank;
}

static int find_target_clique(uint32_t candidates, int depth, uint8_t *chosen) {
    if (depth == TARGET_CLIQUE) {
        return 1;
    }
    if (popcount32(candidates) < TARGET_CLIQUE - depth) {
        return 0;
    }
    while (popcount32(candidates) >= TARGET_CLIQUE - depth) {
        int best = -1;
        int best_degree = -1;
        uint32_t scan = candidates;
        while (scan) {
            int vertex = __builtin_ctz(scan);
            int degree = popcount32(adjacency[vertex] & candidates);
            if (degree > best_degree) {
                best = vertex;
                best_degree = degree;
            }
            scan &= scan - 1;
        }
        candidates &= ~(UINT32_C(1) << best);
        chosen[depth] = (uint8_t)best;
        ++search_nodes;
        if (find_target_clique(candidates & adjacency[best], depth + 1, chosen)) {
            return 1;
        }
    }
    return 0;
}

static void digest_value(uint64_t *digest, uint64_t value) {
    *digest ^= value;
    *digest *= UINT64_C(1099511628211);
}

static void print_witness(const char *profile, uint16_t a, uint16_t b,
                          const uint8_t *clique) {
    printf("representative profile=%s a=%u b=%u clique=", profile, a, b);
    for (int i = 0; i < TARGET_CLIQUE; ++i) {
        if (i) {
            putchar(',');
        }
        printf("%u", (unsigned)clique[i] + 1U);
    }
    putchar('\n');
}

int main(void) {
    uint64_t pencil_count = 0;
    uint64_t radical_zero_count = 0;
    uint64_t profile_244_count = 0;
    uint64_t profile_444_count = 0;
    uint64_t witness_count = 0;
    uint64_t total_nodes = 0;
    uint64_t maximum_nodes = 0;
    uint64_t digest = UINT64_C(1469598103934665603);
    uint16_t hardest_a = 0;
    uint16_t hardest_b = 0;
    uint16_t representative_a[2] = {0, 0};
    uint16_t representative_b[2] = {0, 0};
    uint8_t representative_clique[2][TARGET_CLIQUE] = {{0}};
    clock_t started = clock();

    for (int x = 1; x <= VERTEX_COUNT; ++x) {
        for (int y = 1; y <= VERTEX_COUNT; ++y) {
            wedges[x - 1][y - 1] = wedge_vector(x, y);
        }
    }

    /* The nonzero elements of a pencil are {a,b,a+b}.  Requiring
       a < b < a+b gives each two-dimensional subspace exactly once. */
    for (uint16_t a = 1; a < FORM_COUNT; ++a) {
        for (uint16_t b = (uint16_t)(a + 1); b < FORM_COUNT; ++b) {
            uint16_t c = a ^ b;
            if (c <= b) {
                continue;
            }
            ++pencil_count;

            int common_radical_zero = 1;
            for (int x = 0; x < VERTEX_COUNT; ++x) {
                uint32_t row = 0;
                for (int y = 0; y < VERTEX_COUNT; ++y) {
                    uint16_t wedge = wedges[x][y];
                    if (__builtin_parity((unsigned)(a & wedge)) ||
                        __builtin_parity((unsigned)(b & wedge))) {
                        row |= UINT32_C(1) << y;
                    }
                }
                adjacency[x] = row;
                if (row == 0) {
                    common_radical_zero = 0;
                }
            }
            if (!common_radical_zero) {
                continue;
            }
            ++radical_zero_count;

            int ranks[3] = {
                alternating_rank(a), alternating_rank(b), alternating_rank(c)
            };
            int rank_two_count = 0;
            for (int i = 0; i < 3; ++i) {
                if (ranks[i] == 2) {
                    ++rank_two_count;
                } else if (ranks[i] != 4) {
                    fprintf(stderr, "unexpected alternating rank\n");
                    return 3;
                }
            }
            int profile_index;
            if (rank_two_count == 1) {
                ++profile_244_count;
                profile_index = 0;
            } else if (rank_two_count == 0) {
                ++profile_444_count;
                profile_index = 1;
            } else {
                fprintf(stderr, "unexpected radical-zero rank profile\n");
                return 4;
            }

            uint8_t clique[TARGET_CLIQUE];
            search_nodes = 0;
            if (!find_target_clique(UINT32_C(0x7fffffff), 0, clique)) {
                fprintf(stderr, "missing %d-clique at pencil %u,%u\n",
                        TARGET_CLIQUE, a, b);
                return 5;
            }
            ++witness_count;
            total_nodes += search_nodes;
            if (search_nodes > maximum_nodes) {
                maximum_nodes = search_nodes;
                hardest_a = a;
                hardest_b = b;
            }
            if (representative_a[profile_index] == 0) {
                representative_a[profile_index] = a;
                representative_b[profile_index] = b;
                for (int i = 0; i < TARGET_CLIQUE; ++i) {
                    representative_clique[profile_index][i] = clique[i];
                }
            }
            digest_value(&digest, a);
            digest_value(&digest, b);
            for (int i = 0; i < TARGET_CLIQUE; ++i) {
                digest_value(&digest, (uint64_t)clique[i] + 1U);
            }
        }
    }

    double cpu_seconds = (double)(clock() - started) / (double)CLOCKS_PER_SEC;
    printf("enumeration pencils=%" PRIu64 " common_radical_zero=%" PRIu64 "\n",
           pencil_count, radical_zero_count);
    printf("profiles rank_244=%" PRIu64 " rank_444=%" PRIu64 "\n",
           profile_244_count, profile_444_count);
    printf("search target=%d witnesses=%" PRIu64 " total_nodes=%" PRIu64
           " maximum_nodes=%" PRIu64 " hardest=%u,%u digest=%016" PRIx64
           " cpu_seconds=%.6f\n",
           TARGET_CLIQUE, witness_count, total_nodes, maximum_nodes,
           hardest_a, hardest_b, digest, cpu_seconds);
    print_witness("244", representative_a[0], representative_b[0],
                  representative_clique[0]);
    print_witness("444", representative_a[1], representative_b[1],
                  representative_clique[1]);

    if (pencil_count != UINT64_C(174251) ||
        radical_zero_count != UINT64_C(156240) ||
        profile_244_count != UINT64_C(52080) ||
        profile_444_count != UINT64_C(104160) ||
        witness_count != radical_zero_count) {
        return 6;
    }
    return 0;
}
