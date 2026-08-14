# Exact capability/epicentre certificate for a bounded SmallGroups(64,*) ID range.
# Required variables: ERDOS117_START_ID, ERDOS117_END_ID, ERDOS117_OUTPUT,
# ERDOS117_STDOUT_LOG.  The selected 2-Schur cover is converted injectively
# to a pc group, and the image of its center in Q is exported with explicit
# pc exponent witnesses.

if not IsBound(ERDOS117_START_ID) or not IsBound(ERDOS117_END_ID)
   or not IsBound(ERDOS117_OUTPUT) or not IsBound(ERDOS117_STDOUT_LOG) then
    Error("set start/end ID, output, and stdout log");
fi;

Erdos117VectorString := function(vector)
return JoinStringsWithSeparator(List(vector, String), ",");
end;;

Erdos117RelationString := function(pcgs)
local orders, powers, commutators, left, right;
orders := RelativeOrders(pcgs);
powers := List(
    [1 .. Length(pcgs)],
    index -> ExponentsOfPcElement(pcgs, pcgs[index] ^ orders[index])
);
commutators := [];
for left in [1 .. Length(pcgs)] do
    for right in [1 .. left - 1] do
        Add(commutators, ExponentsOfPcElement(pcgs, Comm(pcgs[left], pcgs[right])));
    od;
od;
return Concatenation(
    Erdos117VectorString(orders), "|",
    JoinStringsWithSeparator(List(powers, Erdos117VectorString), ";"), "|",
    JoinStringsWithSeparator(List(commutators, Erdos117VectorString), ";")
);
end;;

RunErdos117CapabilityOrder64 := function()
local stream, progress, qId, q, qPcgs, qElements, epi, source, pcEpi,
    pcKernel, cover, coverPcgs, coverKernel, exterior, exteriorGenerators,
    exteriorOrders, lifts, center, epicentrePositions,
    position, element, lift, qExponents, liftExponents, liftCommutators,
    startTime, elapsed, qRelations, coverRelations, identityPosition,
    witnessRows;

stream := OutputTextFile(ERDOS117_OUTPUT, false);
progress := OutputTextFile(ERDOS117_STDOUT_LOG, false);
SetPrintFormattingStatus(stream, false);
SetPrintFormattingStatus(progress, false);
AppendTo(stream, "# GAP_VERSION=", GAPInfo.Version, "\n");
AppendTo(stream, "# SMALLGRP_VERSION=", InstalledPackageVersion("smallgrp"), "\n");
AppendTo(stream, "# Q_ORDER=64\n");
AppendTo(stream, "# START_Q_ID=", ERDOS117_START_ID, "\n");
AppendTo(stream, "# END_Q_ID=", ERDOS117_END_ID, "\n");
AppendTo(stream, "# SCHUR_COVER_PRIMES=2\n");
AppendTo(
    stream,
    "q_id\tstructure\tq_pc_presentation\tcover_order\tcover_pc_presentation\t",
    "pc_conversion_kernel_order\tcover_kernel_order\tcover_kernel_central\t",
    "cover_kernel_in_derived\texterior_order\texterior_orders\t",
    "epicentre_size\tepicentre_position\tis_identity\tq_exponents\t",
    "lift_exponents\tlift_commutators\twitness_commutator_row\truntime_ms\n"
);

for qId in [ERDOS117_START_ID .. ERDOS117_END_ID] do
    startTime := Runtime();
    q := SmallGroup(64, qId);
    qPcgs := Pcgs(q);
    qElements := AsList(q);
    identityPosition := Position(qElements, One(q));
    epi := EpimorphismSchurCover(q, [2]);
    source := Source(epi);
    pcEpi := EpimorphismPGroup(source, 2, 10);
    pcKernel := KernelOfMultiplicativeGeneralMapping(pcEpi);
    if Size(pcKernel) <> 1 then
        Error("pc conversion lost part of the Schur cover");
    fi;
    cover := Range(pcEpi);
    coverPcgs := Pcgs(cover);
    coverKernel := Image(pcEpi, KernelOfMultiplicativeGeneralMapping(epi));
    if not IsSubgroup(Center(cover), coverKernel) then
        Error("selected Schur-cover kernel is not central");
    fi;
    exterior := DerivedSubgroup(cover);
    if not IsSubgroup(exterior, coverKernel) then
        Error("selected Schur-cover kernel is not in the derived subgroup");
    fi;
    if not IsAbelian(exterior) then
        Error("capability witness export requires abelian exterior square");
    fi;
    exteriorGenerators := IndependentGeneratorsOfAbelianGroup(exterior);
    exteriorOrders := List(exteriorGenerators, Order);
    lifts := List(
        qElements,
        element -> Image(pcEpi, PreImagesRepresentative(epi, element))
    );
    center := Center(cover);
    epicentrePositions := Filtered(
        [1 .. 64], position -> lifts[position] in center
    );
    qRelations := Erdos117RelationString(qPcgs);
    coverRelations := Erdos117RelationString(coverPcgs);
    elapsed := Runtime() - startTime;
    for position in epicentrePositions do
        element := qElements[position];
        lift := lifts[position];
        if Image(epi, PreImagesRepresentative(pcEpi, lift)) <> element then
            Error("cover lift does not map back to quotient element");
        fi;
        qExponents := ExponentsOfPcElement(qPcgs, element);
        liftExponents := ExponentsOfPcElement(coverPcgs, lift);
        liftCommutators := List(
            coverPcgs,
            generator -> ExponentsOfPcElement(coverPcgs, Comm(lift, generator))
        );
        witnessRows := List(
            lifts,
            other -> IndependentGeneratorExponents(exterior, Comm(lift, other))
        );
        if ForAny(liftCommutators, vector -> ForAny(vector, exponent -> exponent <> 0)) then
            Error("epicentre lift is not central");
        fi;
        AppendTo(
            stream, qId, "\t", StructureDescription(q), "\t", qRelations,
            "\t", Size(cover), "\t", coverRelations,
            "\t", Size(pcKernel), "\t", Size(coverKernel), "\ttrue\t",
            "true\t", Size(exterior), "\t",
            Erdos117VectorString(exteriorOrders), "\t",
            Length(epicentrePositions), "\t", position, "\t",
            position = identityPosition, "\t", Erdos117VectorString(qExponents),
            "\t", Erdos117VectorString(liftExponents), "\t",
            JoinStringsWithSeparator(List(liftCommutators, Erdos117VectorString), ";"),
            "\t", JoinStringsWithSeparator(List(witnessRows, Erdos117VectorString), ";"),
            "\t", elapsed, "\n"
        );
    od;
    AppendTo(
        progress, "Q=SmallGroup(64,", qId, ") structure=",
        StructureDescription(q), " cover_order=", Size(cover),
        " cover_kernel=", Size(coverKernel), " epicentre_size=",
        Length(epicentrePositions), " positions=",
        JoinStringsWithSeparator(List(epicentrePositions, String), ","),
        " runtime_ms=", elapsed, "\n"
    );
    Print(
        "Q=SmallGroup(64,", qId, ") epicentre_size=",
        Length(epicentrePositions), " runtime_ms=", elapsed, "\n"
    );
od;
AppendTo(
    progress, "completed capability batch IDs=", ERDOS117_START_ID, "..",
    ERDOS117_END_ID, "\n"
);
CloseStream(stream);
CloseStream(progress);
end;;

RunErdos117CapabilityOrder64();;
QUIT;
