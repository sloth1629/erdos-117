# Exact chosen-Schur-cover character-dual export for one order-64 quotient.
# Required variables: ERDOS117_Q_ID, ERDOS117_OUTPUT, ERDOS117_STDOUT_LOG.

if not IsBound(ERDOS117_Q_ID) or not IsBound(ERDOS117_OUTPUT)
   or not IsBound(ERDOS117_STDOUT_LOG) then
    Error("set ERDOS117_Q_ID, ERDOS117_OUTPUT, and ERDOS117_STDOUT_LOG");
fi;

Erdos117VectorString := function(vector)
return JoinStringsWithSeparator(List(vector, String), ",");
end;;

Erdos117ActionString := function(exterior, generators, actingElement)
return JoinStringsWithSeparator(
    List(
        generators,
        element -> Erdos117VectorString(
            IndependentGeneratorExponents(exterior, element ^ actingElement)
        )
    ),
    ";"
);
end;;

Erdos117ConjugationPermutationString := function(elements, actingElement)
return JoinStringsWithSeparator(
    List(
        elements,
        element -> String(Position(elements, element ^ actingElement) - 1)
    ),
    ","
);
end;;

Erdos117AutomorphismPermutationString := function(elements, automorphism)
return JoinStringsWithSeparator(
    List(
        elements,
        element -> String(Position(elements, Image(automorphism, element)) - 1)
    ),
    ","
);
end;;

q := SmallGroup(64, ERDOS117_Q_ID);;
qPcgs := Pcgs(q);;
qElements := AsList(q);;
epi := EpimorphismSchurCover(q, [2]);;
source := Source(epi);;
pcEpi := EpimorphismPGroup(source, 2, 10);;
pcKernel := KernelOfMultiplicativeGeneralMapping(pcEpi);;
if Size(pcKernel) <> 1 then
    Error("p-group conversion lost part of the Schur cover");
fi;
cover := Range(pcEpi);;
coverPcgs := Pcgs(cover);;
coverKernel := Image(pcEpi, KernelOfMultiplicativeGeneralMapping(epi));;
exterior := DerivedSubgroup(cover);;
if not IsSubgroup(Center(cover), coverKernel) then
    Error("selected Schur-cover kernel is not central");
fi;
if not IsSubgroup(exterior, coverKernel) then
    Error("selected Schur-cover kernel is not in the derived subgroup");
fi;
if not IsAbelian(exterior) then
    Error("the generic character-dual certificate requires abelian exterior square");
fi;
independentGenerators := IndependentGeneratorsOfAbelianGroup(exterior);;
orders := List(independentGenerators, Order);;
if Product(orders) <> Size(exterior) then
    Error("independent exterior generators have the wrong total order");
fi;
lifts := List(
    qElements,
    element -> Image(pcEpi, PreImagesRepresentative(epi, element))
);;
automorphismGenerators := GeneratorsOfGroup(AutomorphismGroup(q));;

stream := OutputTextFile(ERDOS117_OUTPUT, false);;
progress := OutputTextFile(ERDOS117_STDOUT_LOG, false);;
SetPrintFormattingStatus(stream, false);;
SetPrintFormattingStatus(progress, false);;
AppendTo(stream, "# GAP_VERSION=", GAPInfo.Version, "\n");
AppendTo(stream, "# SMALLGRP_VERSION=", InstalledPackageVersion("smallgrp"), "\n");
AppendTo(stream, "# Q_ORDER=64\n");
AppendTo(stream, "# Q_ID=", ERDOS117_Q_ID, "\n");
AppendTo(stream, "# STRUCTURE=", StructureDescription(q), "\n");
AppendTo(stream, "# Q_PC_RELATIVE_ORDERS=", Erdos117VectorString(RelativeOrders(qPcgs)), "\n");
AppendTo(stream, "# COVER_ORDER=", Size(cover), "\n");
AppendTo(stream, "# PC_CONVERSION_KERNEL_ORDER=", Size(pcKernel), "\n");
AppendTo(stream, "# COVER_TO_Q_KERNEL_ORDER=", Size(coverKernel), "\n");
AppendTo(stream, "# COVER_KERNEL_CENTRAL=true\n");
AppendTo(stream, "# COVER_KERNEL_IN_DERIVED=true\n");
AppendTo(stream, "# EXTERIOR_ORDER=", Size(exterior), "\n");
AppendTo(stream, "# EXTERIOR_RELATIVE_ORDERS=", Erdos117VectorString(orders), "\n");
AppendTo(stream, "# ACTION_COUNT=", Length(coverPcgs), "\n");
AppendTo(stream, "# AUTOMORPHISM_GENERATOR_COUNT=", Length(automorphismGenerators), "\n");
AppendTo(stream, "# COMMUTATOR_ROW_COUNT=64\n");
AppendTo(stream, "ACTIONS\n");
AppendTo(stream, "action_index\timage_vectors\tq_conjugation\n");
for i in [1 .. Length(coverPcgs)] do
    g := coverPcgs[i];;
    qg := Image(epi, PreImagesRepresentative(pcEpi, g));;
    AppendTo(
        stream, i, "\t",
        Erdos117ActionString(exterior, independentGenerators, g), "\t",
        Erdos117ConjugationPermutationString(qElements, qg), "\n"
    );
od;
AppendTo(stream, "COMMUTATORS\n");
AppendTo(stream, "vertex\tq_exponents\tcommutator_vectors\n");
for i in [1 .. 64] do
    AppendTo(
        stream, i - 1, "\t",
        Erdos117VectorString(ExponentsOfPcElement(qPcgs, qElements[i])), "\t",
        JoinStringsWithSeparator(
            List(
                [1 .. 64],
                j -> Erdos117VectorString(
                    IndependentGeneratorExponents(
                        exterior, Comm(lifts[i], lifts[j])
                    )
                )
            ),
            ";"
        ),
        "\n"
    );
od;
AppendTo(stream, "AUTOMORPHISMS\n");
AppendTo(stream, "automorphism_index\tq_permutation\n");
for i in [1 .. Length(automorphismGenerators)] do
    alpha := automorphismGenerators[i];;
    AppendTo(
        stream, i, "\t",
        Erdos117AutomorphismPermutationString(qElements, alpha),
        "\n"
    );
od;
CloseStream(stream);;
AppendTo(
    progress,
    "[COMPUTED] exported order-64 character-dual chosen-cover data\n",
    "Q=SmallGroup(64,", ERDOS117_Q_ID, ") structure=", StructureDescription(q), "\n",
    "cover_order=", Size(cover), " cover_kernel_order=", Size(coverKernel),
    " exterior_order=", Size(exterior), " exterior_orders=",
    Erdos117VectorString(orders), "\n",
    "actions=", Length(coverPcgs), " automorphisms=",
    Length(automorphismGenerators), " commutator_rows=64\n"
);
CloseStream(progress);;
Print(
    "exported Q=SmallGroup(64,", ERDOS117_Q_ID, ") cover=", Size(cover),
    " exterior=", Size(exterior), " actions=", Length(coverPcgs),
    " automorphisms=", Length(automorphismGenerators), "\n"
);;
QUIT;
