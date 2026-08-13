# Export central-coset graphs only for groups whose deterministic greedy
# clique has size at most the configured cutoff.  This is a rigorous filter:
# every omitted group contains the saved greedy clique and therefore has
# clique number greater than the cutoff.

if LoadPackage("smallgrp") = fail then
    Error("SmallGrp is required");
fi;

if not IsBound(ERDOS117_ORDER) or not IsBound(ERDOS117_OUTPUT)
   or not IsBound(ERDOS117_CLIQUE_CUTOFF) then
    Error("set ERDOS117_ORDER, ERDOS117_OUTPUT, and ERDOS117_CLIQUE_CUTOFF");
fi;

stream := OutputTextFile(ERDOS117_OUTPUT, false);
SetPrintFormattingStatus(stream, false);
AppendTo(stream, "group_id\tstructure\tcenter_size\tcoset_count\tis_ac\tadjacency\n");

survivors := 0;
for identifier in [1 .. NumberSmallGroups(ERDOS117_ORDER)] do
    group := SmallGroup(ERDOS117_ORDER, identifier);
    center := Center(group);
    representatives := List(RightCosets(group, center), Representative);
    count := Length(representatives);
    adjacency := List(
        [1 .. count],
        i -> Filtered(
            [1 .. count],
            j -> i <> j and representatives[i] * representatives[j]
                <> representatives[j] * representatives[i]
        )
    );

    candidates := [1 .. count];
    clique := [];
    while Length(candidates) > 0
          and Length(clique) <= ERDOS117_CLIQUE_CUTOFF do
        degrees := List(
            candidates,
            v -> Length(Intersection(candidates, adjacency[v]))
        );
        vertex := candidates[Position(degrees, Maximum(degrees))];
        Add(clique, vertex);
        candidates := Intersection(candidates, adjacency[vertex]);
    od;

    if Length(clique) <= ERDOS117_CLIQUE_CUTOFF then
        survivors := survivors + 1;
        isAC := ForAll(
            Elements(group),
            x -> x in center or IsAbelian(Centralizer(group, x))
        );
        rows := List(
            adjacency,
            row -> JoinStringsWithSeparator(List(row, String), ",")
        );
        AppendTo(
            stream,
            "SmallGroup(", ERDOS117_ORDER, ",", identifier, ")\t",
            StructureDescription(group), "\t",
            Size(center), "\t", count, "\t", isAC, "\t",
            JoinStringsWithSeparator(rows, ";"), "\n"
        );
    fi;

    if identifier mod 100 = 0 then
        Print("scanned ", identifier, "/", NumberSmallGroups(ERDOS117_ORDER), "\n");
    fi;
od;

CloseStream(stream);
Print(
    "completed order ", ERDOS117_ORDER, " scan; cutoff=",
    ERDOS117_CLIQUE_CUTOFF, "; survivors=", survivors, "\n"
);
QUIT;
