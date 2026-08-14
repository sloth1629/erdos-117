# Feasibility-only Schur/exterior inventory for three literature candidates
# beyond the proved |Q|<=81 cutoff-eight computation.  This script does not
# scan commutator graphs and makes no completeness claim for h(8).

if LoadPackage("smallgrp") = fail then
    Error("SmallGrp is required");
fi;
if not IsBound(ERDOS117_OUTPUT) or not IsBound(ERDOS117_STDOUT_LOG) then
    Error("set ERDOS117_OUTPUT and ERDOS117_STDOUT_LOG");
fi;

Erdos117H8JoinIntegers := function(values)
return JoinStringsWithSeparator(List(values, String), ",");
end;;

RunErdos117H8LiteratureCandidateInventory := function()
local stream, progress, candidates, record, label, qOrder, qId, quotient,
    multiplier, multiplierOrder, derivedOrder, exteriorOrder, epi, coverFp,
    coverIso, cover, coverKernel, exterior, allSubgroups, normalKernels,
    qElements, lifts, coverCenter, centerImagePositions, identityPosition,
    nonidentityCenterImagePositions, quotientAdjacency, adjacencyEncoding,
    namedGroup, field, fieldZero, fieldOne, r2, s2, complement, module,
    moduleGenerators, r4, s4, rImages, sImages, rAutomorphism, sAutomorphism,
    automorphismGroup, action, startTime, coverMs, pcMs, subgroupMs, normalMs,
    feasibility;

candidates := [
    ["diagonal_C2_4_semidirect_S3", 96, 227],
    ["C3_2_times_A4", 108, 41],
    ["C2_3_times_generalized_dihedral_C3_2", 144, 196]
];

stream := OutputTextFile(ERDOS117_OUTPUT, false);
progress := OutputTextFile(ERDOS117_STDOUT_LOG, false);
SetPrintFormattingStatus(stream, false);
SetPrintFormattingStatus(progress, false);
AppendTo(stream, "# GAP_VERSION=", GAPInfo.Version, "\n");
AppendTo(stream, "# SMALLGRP_VERSION=", InstalledPackageVersion("smallgrp"), "\n");
AppendTo(stream, "# SCOPE=literature_candidates_beyond_order_81_only\n");
AppendTo(stream, "# CUTOFF8_GRAPH_SCAN_PERFORMED=false\n");
AppendTo(stream, "# NAMED_CONSTRUCTIONS_VERIFIED=true\n");
AppendTo(
    stream,
    "label\tq_order\tq_id\tstructure\tq_noncommuting_adjacency\t",
    "q_center_order\tq_derived_order\t",
    "multiplier_invariants\tmultiplier_order\texterior_order_identity\t",
    "cover_order\tcover_kernel_order\tcover_kernel_central\t",
    "cover_kernel_in_derived\texterior_order_constructed\t",
    "exterior_structure\texterior_abelian\texterior_generator_count\t",
    "selected_cover_center_image_size\t",
    "nonidentity_center_image_positions\t",
    "explicit_nonidentity_zero_row_available\t",
    "all_exterior_subgroup_count\tnormal_kernel_count\t",
    "direct_cutoff8_scan_feasibility\tcover_ms\tpc_ms\t",
    "all_subgroups_ms\tnormal_filter_ms\n"
);

for record in candidates do
    label := record[1];
    qOrder := record[2];
    qId := record[3];
    if qOrder = 96 then
        # Two copies of the natural GL(2,2)=S3 module, with diagonal action.
        field := GF(2);
        fieldZero := Zero(field);
        fieldOne := One(field);
        r2 := ImmutableMatrix(
            field, [[fieldZero, fieldOne], [fieldOne, fieldOne]]
        );
        s2 := ImmutableMatrix(
            field, [[fieldZero, fieldOne], [fieldOne, fieldZero]]
        );
        complement := Group(r2, s2);
        module := ElementaryAbelianGroup(16);
        moduleGenerators := GeneratorsOfGroup(module);
        r4 := ImmutableMatrix(
            field,
            [
                [fieldZero,fieldOne, fieldZero,fieldZero],
                [fieldOne,fieldOne, fieldZero,fieldZero],
                [fieldZero,fieldZero, fieldZero,fieldOne],
                [fieldZero,fieldZero, fieldOne,fieldOne]
            ]
        );
        s4 := ImmutableMatrix(
            field,
            [
                [fieldZero,fieldOne, fieldZero,fieldZero],
                [fieldOne,fieldZero, fieldZero,fieldZero],
                [fieldZero,fieldZero, fieldZero,fieldOne],
                [fieldZero,fieldZero, fieldOne,fieldZero]
            ]
        );
        rImages := List(
            [1..4],
            i -> Product(
                [1..4],
                j -> moduleGenerators[j] ^ IntFFE(r4[i][j])
            )
        );
        sImages := List(
            [1..4],
            i -> Product(
                [1..4],
                j -> moduleGenerators[j] ^ IntFFE(s4[i][j])
            )
        );
        rAutomorphism := GroupHomomorphismByImages(
            module, module, moduleGenerators, rImages
        );
        sAutomorphism := GroupHomomorphismByImages(
            module, module, moduleGenerators, sImages
        );
        if not IsBijective(rAutomorphism) or not IsBijective(sAutomorphism) then
            Error("diagonal S3 module maps are not automorphisms");
        fi;
        automorphismGroup := Group(rAutomorphism, sAutomorphism);
        action := GroupHomomorphismByImages(
            complement, automorphismGroup, [r2,s2],
            [rAutomorphism,sAutomorphism]
        );
        namedGroup := SemidirectProduct(complement, action, module);
    elif qOrder = 108 then
        namedGroup := DirectProduct(
            ElementaryAbelianGroup(9), AlternatingGroup(4)
        );
    elif qOrder = 144 then
        namedGroup := DirectProduct(
            ElementaryAbelianGroup(8), SmallGroup(18,4)
        );
    else
        Error("unknown named candidate construction");
    fi;
    if IdGroup(namedGroup) <> [qOrder,qId] then
        Error("named candidate construction has the wrong SmallGroup ID");
    fi;
    quotient := SmallGroup(qOrder, qId);
    qElements := AsList(quotient);
    quotientAdjacency := List(
        [1 .. qOrder],
        i -> Filtered(
            [1 .. qOrder],
            j -> i <> j and Comm(qElements[i], qElements[j]) <> One(quotient)
        )
    );
    adjacencyEncoding := JoinStringsWithSeparator(
        List(
            quotientAdjacency,
            row -> String(Sum(row, vertex -> 2 ^ (vertex - 1)))
        ),
        ","
    );
    multiplier := AbelianInvariantsMultiplier(quotient);
    multiplierOrder := Product(multiplier);
    derivedOrder := Size(DerivedSubgroup(quotient));
    exteriorOrder := multiplierOrder * derivedOrder;

    startTime := Runtime();
    epi := EpimorphismSchurCover(quotient);
    coverFp := Source(epi);
    coverMs := Runtime() - startTime;
    startTime := Runtime();
    coverIso := IsomorphismPcGroup(coverFp);
    if coverIso = fail then
        Error("chosen Schur cover did not convert to a pc group");
    fi;
    cover := Image(coverIso);
    coverKernel := Image(coverIso, Kernel(epi));
    exterior := DerivedSubgroup(cover);
    identityPosition := Position(qElements, One(quotient));
    lifts := List(
        qElements,
        element -> Image(coverIso, PreImagesRepresentative(epi, element))
    );
    coverCenter := Centre(cover);
    centerImagePositions := Filtered(
        [1 .. qOrder], position -> lifts[position] in coverCenter
    );
    nonidentityCenterImagePositions := Difference(
        centerImagePositions, [identityPosition]
    );
    pcMs := Runtime() - startTime;
    if Size(exterior) <> exteriorOrder then
        Error("constructed exterior square disagrees with multiplier identity");
    fi;
    if Size(coverKernel) <> multiplierOrder then
        Error("chosen Schur-cover kernel has wrong order");
    fi;
    if not IsSubgroup(Centre(cover), coverKernel) then
        Error("chosen cover kernel is not central");
    fi;
    if not IsSubgroup(exterior, coverKernel) then
        Error("chosen cover kernel is not contained in the derived subgroup");
    fi;

    startTime := Runtime();
    allSubgroups := AllSubgroups(exterior);
    subgroupMs := Runtime() - startTime;
    startTime := Runtime();
    normalKernels := Filtered(allSubgroups, kernel -> IsNormal(cover, kernel));
    normalMs := Runtime() - startTime;
    if Length(normalKernels) <= 100 then
        feasibility := "direct_small";
    elif Length(normalKernels) <= 25000 then
        feasibility := "direct_batched";
    else
        feasibility := "requires_dual_or_orbit_reduction";
    fi;

    AppendTo(
        stream,
        label, "\t", qOrder, "\t", qId, "\t", StructureDescription(quotient),
        "\t", adjacencyEncoding, "\t", Size(Centre(quotient)), "\t",
        derivedOrder, "\t",
        Erdos117H8JoinIntegers(multiplier), "\t", multiplierOrder, "\t",
        exteriorOrder, "\t", Size(cover), "\t", Size(coverKernel), "\t",
        IsSubgroup(Centre(cover), coverKernel), "\t",
        IsSubgroup(exterior, coverKernel), "\t", Size(exterior), "\t",
        StructureDescription(exterior), "\t", IsAbelian(exterior), "\t",
        Length(MinimalGeneratingSet(exterior)), "\t",
        Length(centerImagePositions), "\t",
        Erdos117H8JoinIntegers(nonidentityCenterImagePositions), "\t",
        Length(nonidentityCenterImagePositions) > 0, "\t", Length(allSubgroups),
        "\t", Length(normalKernels), "\t", feasibility, "\t", coverMs,
        "\t", pcMs, "\t", subgroupMs, "\t", normalMs, "\n"
    );
    AppendTo(
        progress, "Q=SmallGroup(", qOrder, ",", qId, ") exterior=",
        Size(exterior), " all_subgroups=", Length(allSubgroups),
        " normal_kernels=", Length(normalKernels), " feasibility=", feasibility,
        "\n"
    );
od;
CloseStream(stream);
CloseStream(progress);
Print("completed h8 literature-candidate feasibility inventory; candidates=3\n");
end;;

RunErdos117H8LiteratureCandidateInventory();;
QUIT;
