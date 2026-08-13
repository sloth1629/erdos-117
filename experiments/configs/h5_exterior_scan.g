# Enumerate every commutator graph that arises from an S-normal quotient of
# the nonabelian exterior square Q wedge Q for every SmallGroup Q of order at
# most the configured bound.  For a Schur cover S -> Q, S' is canonically
# isomorphic to Q wedge Q via lifted commutators.

if LoadPackage("smallgrp") = fail then
    Error("SmallGrp is required");
fi;

if not IsBound(ERDOS117_OUTPUT) or not IsBound(ERDOS117_MAX_Q_ORDER) then
    Error("set ERDOS117_OUTPUT and ERDOS117_MAX_Q_ORDER");
fi;

RunErdos117ExteriorScan := function()
local stream, totalQuotients, totalGraphs, qOrder, numberGroups, qId,
    quotient, epi, coverFp, coverIso, cover, exterior, quotientElements,
    lifts, exteriorElements, commutatorPositions, allExteriorSubgroups,
    kernels, kernelSerial, kernel, kernelPositions, adjacency, rows;

stream := OutputTextFile(ERDOS117_OUTPUT, false);
SetPrintFormattingStatus(stream, false);
AppendTo(stream, "# GAP_VERSION=", GAPInfo.Version, "\n");
AppendTo(
    stream,
    "# SMALLGRP_VERSION=",
    InstalledPackageVersion("smallgrp"), "\n"
);
AppendTo(stream, "# MAX_Q_ORDER=", ERDOS117_MAX_Q_ORDER, "\n");
AppendTo(
    stream,
    "q_order\tq_id\tstructure\tcover_order\texterior_order\t",
    "all_exterior_subgroups\tnormal_kernel_count\tkernel_serial\t",
    "kernel_order\tkernel_index\tadjacency\n"
);

totalQuotients := 0;
totalGraphs := 0;
for qOrder in [1 .. ERDOS117_MAX_Q_ORDER] do
    numberGroups := NumberSmallGroups(qOrder);
    for qId in [1 .. numberGroups] do
        quotient := SmallGroup(qOrder, qId);
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
                x -> Position(exteriorElements, x)
            );
            adjacency := List(
                [1 .. qOrder],
                i -> Filtered(
                    [1 .. qOrder],
                    j -> i <> j and not commutatorPositions[i][j]
                        in kernelPositions
                )
            );
            rows := List(
                adjacency,
                row -> JoinStringsWithSeparator(List(row, String), ",")
            );
            AppendTo(
                stream,
                qOrder, "\t", qId, "\t", StructureDescription(quotient), "\t",
                Size(cover), "\t", Size(exterior), "\t",
                Length(allExteriorSubgroups), "\t", Length(kernels), "\t",
                kernelSerial, "\t", Size(kernel), "\t",
                Index(exterior, kernel), "\t",
                JoinStringsWithSeparator(rows, ";"), "\n"
            );
            totalGraphs := totalGraphs + 1;
        od;
        totalQuotients := totalQuotients + 1;
        Print(
            "Q=SmallGroup(", qOrder, ",", qId, ") exterior=",
            Size(exterior), " all_subgroups=", Length(allExteriorSubgroups),
            " normal_kernels=", Length(kernels), " total=", totalGraphs, "\n"
        );
    od;
od;

CloseStream(stream);
Print(
    "completed exterior-square scan; quotients=", totalQuotients,
    " graphs=", totalGraphs, "\n"
);
end;;

RunErdos117ExteriorScan();;
QUIT;
