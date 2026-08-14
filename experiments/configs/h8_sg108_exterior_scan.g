# Exact raw normal-kernel scan for Q=SmallGroup(108,41)=C3^2 x A4.
# This is a single post-81 literature candidate, not a complete h(8) quotient
# inventory.  Every faithful graph is either given a 9-clique or delegated to
# the exact Python clique/color solver.

if LoadPackage("smallgrp") = fail then
    Error("SmallGrp is required");
fi;
if not IsBound(ERDOS117_OUTPUT) or not IsBound(ERDOS117_STDOUT_LOG) then
    Error("set ERDOS117_OUTPUT and ERDOS117_STDOUT_LOG");
fi;

Erdos117H8SG108GreedyClique := function(adjacency, target)
local starts, start, clique, candidates, choices, vertex;
starts := ShallowCopy([1 .. Length(adjacency)]);
SortBy(starts, vertex -> -Length(adjacency[vertex]));
for start in starts do
    clique := [start];
    candidates := ShallowCopy(adjacency[start]);
    while Length(candidates) > 0 and Length(clique) < target do
        choices := ShallowCopy(candidates);
        SortBy(
            choices,
            vertex -> -Length(Intersection(candidates, adjacency[vertex]))
        );
        vertex := choices[1];
        Add(clique, vertex);
        candidates := Intersection(candidates, adjacency[vertex]);
    od;
    if Length(clique) = target then
        return clique;
    fi;
od;
return [];
end;;

RunErdos117H8SG108ExteriorScan := function()
local stream, progress, q, epi, coverFp, coverIso, cover, coverKernel,
    exterior, qElements, lifts, exteriorElements, commutatorPositions,
    allExteriorSubgroups, kernels, kernelSerial, kernel, kernelPositions,
    adjacency, adjacencyEncoding, radicalVertices, witness, clique, status,
    startTime, elapsed;

stream := OutputTextFile(ERDOS117_OUTPUT, false);
progress := OutputTextFile(ERDOS117_STDOUT_LOG, false);
SetPrintFormattingStatus(stream, false);
SetPrintFormattingStatus(progress, false);
AppendTo(stream, "# GAP_VERSION=", GAPInfo.Version, "\n");
AppendTo(stream, "# SMALLGRP_VERSION=", InstalledPackageVersion("smallgrp"), "\n");
AppendTo(stream, "# Q_ORDER=108\n");
AppendTo(stream, "# Q_ID=41\n");
AppendTo(stream, "# CLIQUE_CUTOFF=8\n");
AppendTo(stream, "# TARGET_CLIQUE=9\n");
AppendTo(stream, "# SCOPE=single_post81_literature_candidate_only\n");
AppendTo(
    stream,
    "q_order\tq_id\tstructure\tcover_order\tcover_kernel_order\t",
    "cover_kernel_central\tcover_kernel_in_derived\texterior_order\t",
    "all_exterior_subgroups\tnormal_kernel_count\tkernel_serial\t",
    "kernel_order\tkernel_index\tradical_count\tstatus\twitness\tadjacency\n"
);

startTime := Runtime();
q := SmallGroup(108, 41);
epi := EpimorphismSchurCover(q);
coverFp := Source(epi);
coverIso := IsomorphismPcGroup(coverFp);
if coverIso = fail then
    Error("Schur cover did not convert to a pc group");
fi;
cover := Image(coverIso);
coverKernel := Image(coverIso, Kernel(epi));
exterior := DerivedSubgroup(cover);
if not IsSubgroup(Centre(cover), coverKernel) then
    Error("Schur-cover kernel is not central");
fi;
if not IsSubgroup(exterior, coverKernel) then
    Error("Schur-cover kernel is not contained in the derived subgroup");
fi;
if Size(coverKernel) <> 54 or Size(exterior) <> 216 then
    Error("unexpected multiplier or exterior-square order");
fi;
qElements := AsList(q);
lifts := List(
    qElements,
    element -> Image(coverIso, PreImagesRepresentative(epi, element))
);
exteriorElements := AsList(exterior);
commutatorPositions := List(
    [1 .. 108],
    i -> List(
        [1 .. 108],
        j -> Position(exteriorElements, Comm(lifts[i], lifts[j]))
    )
);
if ForAny(Flat(commutatorPositions), position -> position = fail) then
    Error("lift commutator left the constructed exterior square");
fi;
allExteriorSubgroups := AllSubgroups(exterior);
kernels := Filtered(
    allExteriorSubgroups,
    kernel -> IsNormal(cover, kernel)
);
if Length(allExteriorSubgroups) <> 168 or Length(kernels) <> 84 then
    Error("unexpected SG108 exterior subgroup census");
fi;

for kernelSerial in [1 .. Length(kernels)] do
    kernel := kernels[kernelSerial];
    kernelPositions := List(
        AsList(kernel), element -> Position(exteriorElements, element)
    );
    adjacency := List(
        [1 .. 108],
        i -> Filtered(
            [1 .. 108],
            j -> i <> j and not commutatorPositions[i][j] in kernelPositions
        )
    );
    radicalVertices := Filtered(
        [1 .. 108], vertex -> Length(adjacency[vertex]) = 0
    );
    if Length(radicalVertices) > 1 then
        status := "nonfaithful_radical";
        witness := JoinStringsWithSeparator(List(radicalVertices, String), ",");
    else
        clique := Erdos117H8SG108GreedyClique(adjacency, 9);
        if Length(clique) = 9 then
            status := "clique_ge_9";
            witness := JoinStringsWithSeparator(List(clique, String), ",");
        else
            status := "candidate";
            witness := "";
        fi;
    fi;
    adjacencyEncoding := JoinStringsWithSeparator(
        List(
            adjacency,
            row -> String(Sum(row, vertex -> 2 ^ (vertex - 1)))
        ),
        ","
    );
    AppendTo(
        stream, "108\t41\t", StructureDescription(q), "\t", Size(cover),
        "\t", Size(coverKernel), "\ttrue\ttrue\t", Size(exterior), "\t",
        Length(allExteriorSubgroups), "\t", Length(kernels), "\t",
        kernelSerial, "\t", Size(kernel), "\t", Index(exterior, kernel),
        "\t", Length(radicalVertices), "\t", status, "\t", witness,
        "\t", adjacencyEncoding, "\n"
    );
od;
elapsed := Runtime() - startTime;
AppendTo(
    progress, "Q=SmallGroup(108,41) exterior=216 all_subgroups=168 ",
    "normal_kernels=84 runtime_ms=", elapsed, "\n"
);
CloseStream(stream);
CloseStream(progress);
Print("completed h8 SG108 exterior scan; kernels=84 runtime_ms=", elapsed, "\n");
end;;

RunErdos117H8SG108ExteriorScan();;
QUIT;
