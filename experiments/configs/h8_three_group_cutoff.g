# Exact cutoff-eight inventory for every finite SmallGroup of order
# 3, 9, 27, 81, 243, or 729.  This is a bounded-order computation only.

if LoadPackage("smallgrp") = fail then
    Error("SmallGrp is required");
fi;
if not IsBound(ERDOS117_OUTPUT) or not IsBound(ERDOS117_STDOUT_LOG) then
    Error("set ERDOS117_OUTPUT and ERDOS117_STDOUT_LOG");
fi;

Erdos117H8ThreeGroupVectorString := function(vector)
return JoinStringsWithSeparator(List(vector, String), ",");
end;;

Erdos117H8ThreeGroupCheapClique := function(
    representatives, start, target, reverseChoice
)
local clique, candidates, vertex;
clique := [start];
candidates := Filtered(
    [1 .. Length(representatives)],
    j -> j <> start and representatives[start] * representatives[j]
        <> representatives[j] * representatives[start]
);
while Length(candidates) > 0 and Length(clique) < target do
    if reverseChoice then
        vertex := candidates[Length(candidates)];
    else
        vertex := candidates[1];
    fi;
    Add(clique, vertex);
    candidates := Filtered(
        candidates,
        j -> j <> vertex and representatives[vertex] * representatives[j]
            <> representatives[j] * representatives[vertex]
    );
od;
if Length(clique) = target then
    return clique;
fi;
return [];
end;;

Erdos117H8ThreeGroupIsACGraph := function(adjacency)
local count, all, vertex, centralizerVertices, left;
count := Length(adjacency);
all := [1 .. count];
for vertex in all do
    if Length(adjacency[vertex]) = 0 then
        continue;
    fi;
    centralizerVertices := Difference(all, adjacency[vertex]);
    for left in centralizerVertices do
        if Length(Intersection(adjacency[left], centralizerVertices)) > 0 then
            return false;
        fi;
    od;
od;
return true;
end;;

RunErdos117H8ThreeGroupCutoff := function()
local stream, progress, orders, expectedTotals, orderPosition, groupOrder,
    total, identifier, group, center, representatives, count, starts, start,
    reverseChoice, witness, pairs, pcgs, relativeOrders, witnessExponents,
    forwardProducts, reverseProducts, adjacency, adjacencyMasks,
    centralizerIndices, isAC, candidateCount, excludedCount;

orders := [3, 9, 27, 81, 243, 729];
expectedTotals := [1, 2, 5, 15, 67, 504];
if NumberSmallGroups(2187) <> 9310 then
    Error("unexpected NumberSmallGroups value at the unscanned next order");
fi;
stream := OutputTextFile(ERDOS117_OUTPUT, false);
progress := OutputTextFile(ERDOS117_STDOUT_LOG, false);
SetPrintFormattingStatus(stream, false);
SetPrintFormattingStatus(progress, false);
AppendTo(stream, "# GAP_VERSION=", GAPInfo.Version, "\n");
AppendTo(
    stream, "# SMALLGRP_VERSION=", InstalledPackageVersion("smallgrp"), "\n"
);
AppendTo(stream, "# ORDERS=3,9,27,81,243,729\n");
AppendTo(stream, "# EXPECTED_TOTALS=1,2,5,15,67,504\n");
AppendTo(stream, "# TOTAL_GROUPS=594\n");
AppendTo(stream, "# NEXT_ORDER=2187\n");
AppendTo(stream, "# NEXT_ORDER_TOTAL=9310\n");
AppendTo(stream, "# NEXT_ORDER_SCANNED=false\n");
AppendTo(stream, "# CLIQUE_CUTOFF=8\n");
AppendTo(stream, "# TARGET_CLIQUE=9\n");
AppendTo(
    stream,
    "# SCOPE=finite_SmallGroups_orders_3_through_729_only_order_2187_not_scanned\n"
);
AppendTo(
    stream,
    "group_order\tgroup_id\tstructure\tcenter_order\tcoset_count\t",
    "pc_relative_orders\tstatus\twitness_vertices\twitness_exponents\t",
    "witness_forward_products\twitness_reverse_products\tis_ac\t",
    "centralizer_indices\tadjacency_masks\n"
);

for orderPosition in [1 .. Length(orders)] do
    groupOrder := orders[orderPosition];
    total := NumberSmallGroups(groupOrder);
    if total <> expectedTotals[orderPosition] then
        Error("unexpected NumberSmallGroups value");
    fi;
    candidateCount := 0;
    excludedCount := 0;
    for identifier in [1 .. total] do
        group := SmallGroup(groupOrder, identifier);
        center := Centre(group);
        representatives := List(RightCosets(group, center), Representative);
        count := Length(representatives);
        witness := [];
        # Graphs of order at most 81 are cheap enough to export exactly.
        # Restrict the heuristic to larger graphs so true cutoff survivors
        # never incur a long multi-start failure.
        if count > 81 then
            starts := Filtered(
                [1 .. count],
                position -> not representatives[position] in center
            );
            if Length(starts) > 128 then
                starts := Concatenation(
                    starts{[1 .. 64]},
                    starts{[Length(starts) - 63 .. Length(starts)]}
                );
            fi;
            for reverseChoice in [false, true] do
                for start in starts do
                    witness := Erdos117H8ThreeGroupCheapClique(
                        representatives, start, 9, reverseChoice
                    );
                    if Length(witness) = 9 then
                        break;
                    fi;
                od;
                if Length(witness) = 9 then
                    break;
                fi;
            od;
        fi;

        pcgs := Pcgs(group);
        relativeOrders := RelativeOrders(pcgs);
        if Product(relativeOrders) <> groupOrder then
            Error("pc relative orders do not multiply to the group order");
        fi;

        if Length(witness) = 9 then
            excludedCount := excludedCount + 1;
            if not ForAll(
                Combinations(witness, 2),
                pair -> representatives[pair[1]] * representatives[pair[2]]
                    <> representatives[pair[2]] * representatives[pair[1]]
            ) then
                Error("saved nine-clique is invalid");
            fi;
            pairs := Combinations(witness, 2);
            witnessExponents := List(
                witness,
                position -> Erdos117H8ThreeGroupVectorString(
                    ExponentsOfPcElement(pcgs, representatives[position])
                )
            );
            forwardProducts := List(
                pairs,
                pair -> Erdos117H8ThreeGroupVectorString(
                    ExponentsOfPcElement(
                        pcgs,
                        representatives[pair[1]] * representatives[pair[2]]
                    )
                )
            );
            reverseProducts := List(
                pairs,
                pair -> Erdos117H8ThreeGroupVectorString(
                    ExponentsOfPcElement(
                        pcgs,
                        representatives[pair[2]] * representatives[pair[1]]
                    )
                )
            );
            AppendTo(
                stream, groupOrder, "\t", identifier, "\t\t", Size(center),
                "\t", count, "\t",
                Erdos117H8ThreeGroupVectorString(relativeOrders),
                "\tclique_ge_9\t",
                JoinStringsWithSeparator(List(witness, String), ","), "\t",
                JoinStringsWithSeparator(witnessExponents, ";"), "\t",
                JoinStringsWithSeparator(forwardProducts, ";"), "\t",
                JoinStringsWithSeparator(reverseProducts, ";"),
                "\t\t\t\n"
            );
        else
            candidateCount := candidateCount + 1;
            adjacency := List(
                [1 .. count],
                i -> Filtered(
                    [1 .. count],
                    j -> i <> j and representatives[i] * representatives[j]
                        <> representatives[j] * representatives[i]
                )
            );
            adjacencyMasks := List(
                adjacency,
                row -> Sum(row, target -> 2 ^ (target - 1))
            );
            centralizerIndices := List(
                adjacency,
                row -> count / (count - Length(row))
            );
            if not ForAll(centralizerIndices, IsInt) then
                Error("nonintegral centralizer index derived from adjacency");
            fi;
            isAC := Erdos117H8ThreeGroupIsACGraph(adjacency);
            AppendTo(
                stream, groupOrder, "\t", identifier, "\t",
                StructureDescription(group), "\t", Size(center), "\t", count,
                "\t", Erdos117H8ThreeGroupVectorString(relativeOrders),
                "\tcandidate\t\t\t\t\t", isAC, "\t",
                JoinStringsWithSeparator(List(centralizerIndices, String), ","),
                "\t",
                JoinStringsWithSeparator(List(adjacencyMasks, String), ","),
                "\n"
            );
        fi;
    od;
    AppendTo(
        progress, "order=", groupOrder, " total=", total,
        " candidate=", candidateCount, " clique_ge_9=", excludedCount, "\n"
    );
    Print(
        "order=", groupOrder, " total=", total, " candidate=", candidateCount,
        " clique_ge_9=", excludedCount, "\n"
    );
od;
CloseStream(stream);
CloseStream(progress);
Print("completed h8 finite 3-group cutoff-eight inventory through order 729\n");
end;;

RunErdos117H8ThreeGroupCutoff();;
QUIT;
