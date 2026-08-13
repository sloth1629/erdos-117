# Enumerate every S-normal K <= S' for chosen Schur covers S -> Q, for all
# SmallGroups Q of order at most 36.  The exceptional Q=C2^5 is handled by
# the separate alternating-form certificate h6_c2_5.json.

if LoadPackage("smallgrp") = fail then
    Error("SmallGrp is required");
fi;

if not IsBound(ERDOS117_OUTPUT) or not IsBound(ERDOS117_STDOUT_LOG)
   or not IsBound(ERDOS117_MAX_Q_ORDER) then
    Error("set ERDOS117_OUTPUT, ERDOS117_STDOUT_LOG, and ERDOS117_MAX_Q_ORDER");
fi;

Erdos117GreedyClique := function(adjacency, target)
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

RunErdos117H6ExteriorScan := function()
local stream, progress, totalQuotients, scannedQuotients, totalKernels, qOrder,
    numberGroups, qId, quotient, epi, coverFp, coverIso, cover, exterior,
    quotientElements, lifts, exteriorElements, commutatorPositions,
    allExteriorSubgroups, kernels, kernelSerial, kernel, kernelPositions,
    adjacency, adjacencyEncoding, radicalVertices, status, witness, clique;

stream := OutputTextFile(ERDOS117_OUTPUT, false);
SetPrintFormattingStatus(stream, false);
progress := OutputTextFile(ERDOS117_STDOUT_LOG, false);
SetPrintFormattingStatus(progress, false);
AppendTo(stream, "# GAP_VERSION=", GAPInfo.Version, "\n");
AppendTo(stream, "# SMALLGRP_VERSION=", InstalledPackageVersion("smallgrp"), "\n");
AppendTo(stream, "# MAX_Q_ORDER=", ERDOS117_MAX_Q_ORDER, "\n");
AppendTo(stream, "# CLIQUE_CUTOFF=6\n");
AppendTo(stream, "# SPECIAL_QUOTIENT=SmallGroup(32,51)\n");
AppendTo(
    stream,
    "q_order\tq_id\tstructure\tcover_order\texterior_order\t",
    "all_exterior_subgroups\tnormal_kernel_count\tkernel_serial\t",
    "kernel_order\tkernel_index\tradical_count\tstatus\twitness\tadjacency\n"
);

totalQuotients := 0;
scannedQuotients := 0;
totalKernels := 0;
for qOrder in [1 .. ERDOS117_MAX_Q_ORDER] do
    numberGroups := NumberSmallGroups(qOrder);
    for qId in [1 .. numberGroups] do
        totalQuotients := totalQuotients + 1;
        quotient := SmallGroup(qOrder, qId);
        if qOrder = 32 and qId = 51 then
            AppendTo(
                stream, qOrder, "\t", qId, "\t", StructureDescription(quotient),
                "\t0\t1024\t229755605\t229755605\t0\t0\t0\t0\t",
                "special_c2_5\t\t\n"
            );
            Print("Q=SmallGroup(32,51) delegated to h6_c2_5 certificate\n");
            AppendTo(progress, "Q=SmallGroup(32,51) delegated to h6_c2_5 certificate\n");
            continue;
        fi;

        epi := EpimorphismSchurCover(quotient);
        coverFp := Source(epi);
        coverIso := IsomorphismPcGroup(coverFp);
        cover := Image(coverIso);
        exterior := DerivedSubgroup(cover);
        quotientElements := AsList(quotient);
        lifts := List(
            quotientElements,
            element -> Image(coverIso, PreImagesRepresentative(epi, element))
        );
        exteriorElements := AsList(exterior);
        commutatorPositions := List(
            [1 .. qOrder],
            i -> List(
                [1 .. qOrder],
                j -> Position(exteriorElements, Comm(lifts[i], lifts[j]))
            )
        );
        allExteriorSubgroups := AllSubgroups(exterior);
        kernels := Filtered(
            allExteriorSubgroups,
            kernel -> IsNormal(cover, kernel)
        );
        for kernelSerial in [1 .. Length(kernels)] do
            kernel := kernels[kernelSerial];
            kernelPositions := List(
                AsList(kernel),
                element -> Position(exteriorElements, element)
            );
            adjacency := List(
                [1 .. qOrder],
                i -> Filtered(
                    [1 .. qOrder],
                    j -> i <> j and not commutatorPositions[i][j] in kernelPositions
                )
            );
            radicalVertices := Filtered(
                [1 .. qOrder],
                vertex -> Length(adjacency[vertex]) = 0
            );
            witness := "";
            if Length(radicalVertices) > 1 then
                status := "nonfaithful_radical";
                witness := JoinStringsWithSeparator(List(radicalVertices, String), ",");
            else
                clique := Erdos117GreedyClique(adjacency, 7);
                if Length(clique) = 7 then
                    status := "clique_ge_7";
                    witness := JoinStringsWithSeparator(List(clique, String), ",");
                else
                    status := "candidate";
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
                stream, qOrder, "\t", qId, "\t", StructureDescription(quotient),
                "\t", Size(cover), "\t", Size(exterior), "\t",
                Length(allExteriorSubgroups), "\t", Length(kernels), "\t",
                kernelSerial, "\t", Size(kernel), "\t", Index(exterior, kernel),
                "\t", Length(radicalVertices), "\t", status, "\t", witness,
                "\t", adjacencyEncoding, "\n"
            );
            totalKernels := totalKernels + 1;
        od;
        scannedQuotients := scannedQuotients + 1;
        Print(
            "Q=SmallGroup(", qOrder, ",", qId, ") exterior=", Size(exterior),
            " all_subgroups=", Length(allExteriorSubgroups),
            " normal_kernels=", Length(kernels), " total=", totalKernels, "\n"
        );
        AppendTo(
            progress,
            "Q=SmallGroup(", qOrder, ",", qId, ") exterior=", Size(exterior),
            " all_subgroups=", Length(allExteriorSubgroups),
            " normal_kernels=", Length(kernels), " total=", totalKernels, "\n"
        );
    od;
od;
CloseStream(stream);
AppendTo(
    progress,
    "completed h6 exterior scan; quotients=", totalQuotients,
    " scanned=", scannedQuotients, " kernels=", totalKernels, "\n"
);
CloseStream(progress);
Print(
    "completed h6 exterior scan; quotients=", totalQuotients,
    " scanned=", scannedQuotients, " kernels=", totalKernels, "\n"
);
end;;

RunErdos117H6ExteriorScan();;
QUIT;
