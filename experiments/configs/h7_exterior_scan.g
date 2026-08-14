# Resumable chosen-Schur-cover normal-kernel scan at clique cutoff seven.
# Explosive quotients are passed explicitly in ERDOS117_EXCLUDED_QUOTIENTS and
# require separate structural/orbit certificates; this script never silently
# skips a quotient.

if LoadPackage("smallgrp") = fail then
    Error("SmallGrp is required");
fi;
if not IsBound(ERDOS117_OUTPUT) or not IsBound(ERDOS117_STDOUT_LOG)
   or not IsBound(ERDOS117_START_Q_ORDER) or not IsBound(ERDOS117_END_Q_ORDER)
   or not IsBound(ERDOS117_EXCLUDED_QUOTIENTS) then
    Error("set output, stdout, start/end order, and excluded quotient list");
fi;
if not IsBound(ERDOS117_START_Q_ID) then
    ERDOS117_START_Q_ID := 1;
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

Erdos117PairString := function(pair)
return Concatenation(String(pair[1]), ",", String(pair[2]));
end;;

RunErdos117H7ExteriorScan := function()
local stream, progress, qOrder, firstId, numberGroups, qId, key, quotient,
    epi, coverFp, coverIso, cover, exterior, quotientElements, lifts,
    exteriorElements, commutatorPositions, allExteriorSubgroups, kernels,
    kernelSerial, kernel, kernelPositions, adjacency, adjacencyEncoding,
    radicalVertices, status, witness, clique, totalQuotients, scannedQuotients,
    excludedQuotients, totalKernels, startTime, elapsed, lastId;

stream := OutputTextFile(ERDOS117_OUTPUT, false);
progress := OutputTextFile(ERDOS117_STDOUT_LOG, false);
SetPrintFormattingStatus(stream, false);
SetPrintFormattingStatus(progress, false);
AppendTo(stream, "# GAP_VERSION=", GAPInfo.Version, "\n");
AppendTo(stream, "# SMALLGRP_VERSION=", InstalledPackageVersion("smallgrp"), "\n");
AppendTo(stream, "# START_Q_ORDER=", ERDOS117_START_Q_ORDER, "\n");
AppendTo(stream, "# START_Q_ID=", ERDOS117_START_Q_ID, "\n");
AppendTo(stream, "# END_Q_ORDER=", ERDOS117_END_Q_ORDER, "\n");
if IsBound(ERDOS117_END_Q_ID) then
    AppendTo(stream, "# END_Q_ID=", ERDOS117_END_Q_ID, "\n");
fi;
AppendTo(stream, "# CLIQUE_CUTOFF=7\n");
AppendTo(
    stream, "# EXCLUDED_QUOTIENTS=",
    JoinStringsWithSeparator(List(ERDOS117_EXCLUDED_QUOTIENTS, Erdos117PairString), ";"),
    "\n"
);
AppendTo(
    stream,
    "q_order\tq_id\tstructure\tcover_order\texterior_order\t",
    "all_exterior_subgroups\tnormal_kernel_count\tkernel_serial\t",
    "kernel_order\tkernel_index\tradical_count\tstatus\twitness\tadjacency\n"
);

totalQuotients := 0;
scannedQuotients := 0;
excludedQuotients := 0;
totalKernels := 0;
for qOrder in [ERDOS117_START_Q_ORDER .. ERDOS117_END_Q_ORDER] do
    numberGroups := NumberSmallGroups(qOrder);
    if qOrder = ERDOS117_START_Q_ORDER then
        firstId := ERDOS117_START_Q_ID;
    else
        firstId := 1;
    fi;
    if qOrder = ERDOS117_END_Q_ORDER and IsBound(ERDOS117_END_Q_ID) then
        lastId := Minimum(numberGroups, ERDOS117_END_Q_ID);
    else
        lastId := numberGroups;
    fi;
    for qId in [firstId .. lastId] do
        totalQuotients := totalQuotients + 1;
        key := [qOrder, qId];
        quotient := SmallGroup(qOrder, qId);
        if key in ERDOS117_EXCLUDED_QUOTIENTS then
            AppendTo(
                stream, qOrder, "\t", qId, "\t", StructureDescription(quotient),
                "\t0\t0\t0\t0\t0\t0\t0\t0\texcluded_orbit_case\t0\t0\n"
            );
            AppendTo(progress, "excluded Q=SmallGroup(", qOrder, ",", qId, ")\n");
            excludedQuotients := excludedQuotients + 1;
            continue;
        fi;

        startTime := Runtime();
        epi := EpimorphismSchurCover(quotient);
        coverFp := Source(epi);
        coverIso := IsomorphismPcGroup(coverFp);
        if coverIso = fail then
            coverIso := IsomorphismPermGroup(coverFp);
        fi;
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
        kernels := Filtered(allExteriorSubgroups, kernel -> IsNormal(cover, kernel));
        for kernelSerial in [1 .. Length(kernels)] do
            kernel := kernels[kernelSerial];
            kernelPositions := List(
                AsList(kernel), element -> Position(exteriorElements, element)
            );
            adjacency := List(
                [1 .. qOrder],
                i -> Filtered(
                    [1 .. qOrder],
                    j -> i <> j and not commutatorPositions[i][j] in kernelPositions
                )
            );
            radicalVertices := Filtered(
                [1 .. qOrder], vertex -> Length(adjacency[vertex]) = 0
            );
            witness := "";
            if Length(radicalVertices) > 1 then
                status := "nonfaithful_radical";
                witness := JoinStringsWithSeparator(List(radicalVertices, String), ",");
            else
                clique := Erdos117GreedyClique(adjacency, 8);
                if Length(clique) = 8 then
                    status := "clique_ge_8";
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
        elapsed := Runtime() - startTime;
        scannedQuotients := scannedQuotients + 1;
        AppendTo(
            progress, "Q=SmallGroup(", qOrder, ",", qId, ") exterior=",
            Size(exterior), " all_subgroups=", Length(allExteriorSubgroups),
            " normal_kernels=", Length(kernels), " runtime_ms=", elapsed,
            " total_kernels=", totalKernels, "\n"
        );
        Print(
            "Q=SmallGroup(", qOrder, ",", qId, ") kernels=", Length(kernels),
            " total=", totalKernels, " runtime_ms=", elapsed, "\n"
        );
    od;
od;
AppendTo(
    progress, "completed h7 exterior batch; quotient_rows=", totalQuotients,
    " scanned=", scannedQuotients, " excluded=", excludedQuotients,
    " kernels=", totalKernels, "\n"
);
CloseStream(stream);
CloseStream(progress);
Print(
    "completed h7 exterior batch; quotient_rows=", totalQuotients,
    " scanned=", scannedQuotients, " excluded=", excludedQuotients,
    " kernels=", totalKernels, "\n"
);
end;;

RunErdos117H7ExteriorScan();;
QUIT;
