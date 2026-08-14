# Exact cutoff-eight inventory for the finite SmallGroups of orders
# 5^3, 5^4, 5^5, and 5^6. This is a bounded-order computation and is not a
# classification of all finite 5-groups.

if LoadPackage("smallgrp") = fail then
    Error("SmallGrp is required");
fi;
if not IsBound(ERDOS117_OUTPUT) or not IsBound(ERDOS117_STDOUT_LOG) then
    Error("set ERDOS117_OUTPUT and ERDOS117_STDOUT_LOG");
fi;

Erdos117H8FiveGroupVectorString := function(vector)
return JoinStringsWithSeparator(List(vector, String), ",");
end;;

Erdos117H8FiveGroupCheapClique := function(
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

RunErdos117H8FiveGroupCutoff := function()
local stream, progress, orders, expectedTotals, orderPosition, groupOrder,
    total, identifier, group, center, representatives, count, starts, start,
    reverseChoice, witness, pairs, pcgs, relativeOrders, witnessExponents,
    forwardProducts, reverseProducts, adjacency, adjacencyMasks, candidateCount,
    excludedCount;

orders := [125, 625, 3125, 15625];
expectedTotals := [5, 15, 77, 684];
stream := OutputTextFile(ERDOS117_OUTPUT, false);
progress := OutputTextFile(ERDOS117_STDOUT_LOG, false);
SetPrintFormattingStatus(stream, false);
SetPrintFormattingStatus(progress, false);
AppendTo(stream, "# GAP_VERSION=", GAPInfo.Version, "\n");
AppendTo(
    stream, "# SMALLGRP_VERSION=", InstalledPackageVersion("smallgrp"), "\n"
);
AppendTo(stream, "# ORDERS=125,625,3125,15625\n");
AppendTo(stream, "# EXPECTED_TOTALS=5,15,77,684\n");
AppendTo(stream, "# CLIQUE_CUTOFF=8\n");
AppendTo(stream, "# TARGET_CLIQUE=9\n");
AppendTo(stream, "# SCOPE=finite_SmallGroups_orders_5^3_through_5^6_only\n");
AppendTo(
    stream,
    "group_order\tgroup_id\tstructure\tcenter_order\tcoset_count\t",
    "pc_relative_orders\tstatus\twitness_vertices\twitness_exponents\t",
    "witness_forward_products\twitness_reverse_products\tadjacency_masks\n"
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
        if IdGroup(group) <> [groupOrder, identifier] then
            Error("SmallGroup identifier mismatch");
        fi;
        center := Centre(group);
        representatives := List(RightCosets(group, center), Representative);
        count := Length(representatives);
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
        witness := [];
        for reverseChoice in [false, true] do
            for start in starts do
                witness := Erdos117H8FiveGroupCheapClique(
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
                position -> Erdos117H8FiveGroupVectorString(
                    ExponentsOfPcElement(pcgs, representatives[position])
                )
            );
            forwardProducts := List(
                pairs,
                pair -> Erdos117H8FiveGroupVectorString(
                    ExponentsOfPcElement(
                        pcgs,
                        representatives[pair[1]] * representatives[pair[2]]
                    )
                )
            );
            reverseProducts := List(
                pairs,
                pair -> Erdos117H8FiveGroupVectorString(
                    ExponentsOfPcElement(
                        pcgs,
                        representatives[pair[2]] * representatives[pair[1]]
                    )
                )
            );
            AppendTo(
                stream, groupOrder, "\t", identifier, "\t\t", Size(center),
                "\t", count, "\t",
                Erdos117H8FiveGroupVectorString(relativeOrders),
                "\tclique_ge_9\t",
                JoinStringsWithSeparator(List(witness, String), ","), "\t",
                JoinStringsWithSeparator(witnessExponents, ";"), "\t",
                JoinStringsWithSeparator(forwardProducts, ";"), "\t",
                JoinStringsWithSeparator(reverseProducts, ";"), "\t\n"
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
            AppendTo(
                stream, groupOrder, "\t", identifier, "\t",
                StructureDescription(group), "\t", Size(center), "\t", count,
                "\t", Erdos117H8FiveGroupVectorString(relativeOrders),
                "\tcandidate\t\t\t\t\t",
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
Print("completed h8 finite 5-group cutoff-eight inventory\n");
end;;

RunErdos117H8FiveGroupCutoff();;
QUIT;
