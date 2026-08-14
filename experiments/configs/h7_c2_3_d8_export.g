# Exact Schur-cover data export for
# Q = SmallGroup(64,261) = C2^3 x D8.
#
# The exterior square is abelian of type C2^9 x C4.  The export gives its
# independent-generator coordinates, the conjugation action of a pc
# generating sequence of the selected Schur cover, and the complete 64 by 64
# lifted-commutator table.  The Python certificate checks the action against
# the simultaneously exported quotient conjugation permutations.

if not IsBound(ERDOS117_OUTPUT) or not IsBound(ERDOS117_STDOUT_LOG) then
    Error("set ERDOS117_OUTPUT and ERDOS117_STDOUT_LOG");
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

Erdos117ConjugationString := function(elements, actingElement)
return JoinStringsWithSeparator(
    List(
        elements,
        element -> String(Position(elements, element ^ actingElement) - 1)
    ),
    ","
);
end;;

q := SmallGroup(64, 261);;
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
exterior := DerivedSubgroup(cover);;
if not IsAbelian(exterior) then
    Error("the selected exterior square is not abelian");
fi;
independentGenerators := IndependentGeneratorsOfAbelianGroup(exterior);;
orders := List(independentGenerators, Order);;
if SortedList(orders) <> Concatenation(List([1 .. 9], i -> 2), [4]) then
    Error("unexpected exterior-square invariant factors");
fi;
lifts := List(
    qElements,
    element -> Image(pcEpi, PreImagesRepresentative(epi, element))
);;

stream := OutputTextFile(ERDOS117_OUTPUT, false);;
progress := OutputTextFile(ERDOS117_STDOUT_LOG, false);;
SetPrintFormattingStatus(stream, false);;
SetPrintFormattingStatus(progress, false);;
AppendTo(stream, "# GAP_VERSION=", GAPInfo.Version, "\n");
AppendTo(stream, "# SMALLGRP_VERSION=", InstalledPackageVersion("smallgrp"), "\n");
AppendTo(stream, "# Q_ORDER=64\n");
AppendTo(stream, "# Q_ID=261\n");
AppendTo(stream, "# STRUCTURE=", StructureDescription(q), "\n");
AppendTo(stream, "# Q_PC_RELATIVE_ORDERS=", Erdos117VectorString(RelativeOrders(qPcgs)), "\n");
AppendTo(stream, "# COVER_ORDER=", Size(cover), "\n");
AppendTo(stream, "# PC_CONVERSION_KERNEL_ORDER=", Size(pcKernel), "\n");
AppendTo(
    stream, "# COVER_TO_Q_KERNEL_ORDER=",
    Size(KernelOfMultiplicativeGeneralMapping(epi)), "\n"
);
AppendTo(stream, "# EXTERIOR_ORDER=", Size(exterior), "\n");
AppendTo(stream, "# EXTERIOR_RELATIVE_ORDERS=", Erdos117VectorString(orders), "\n");
AppendTo(stream, "# ACTION_COUNT=", Length(coverPcgs), "\n");
AppendTo(stream, "# COMMUTATOR_ROW_COUNT=64\n");
AppendTo(stream, "ACTIONS\n");
AppendTo(stream, "action_index\timage_vectors\tq_conjugation\n");
for i in [1 .. Length(coverPcgs)] do
    g := coverPcgs[i];;
    qg := Image(epi, PreImagesRepresentative(pcEpi, g));;
    AppendTo(
        stream, i, "\t",
        Erdos117ActionString(exterior, independentGenerators, g),
        "\t",
        Erdos117ConjugationString(qElements, qg),
        "\n"
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
CloseStream(stream);;
AppendTo(
    progress,
    "[COMPUTED] exported Q=SmallGroup(64,261) chosen-cover data\n",
    "cover_order=", Size(cover), " exterior_order=", Size(exterior),
    " exterior_orders=", Erdos117VectorString(orders), "\n",
    "actions=", Length(coverPcgs), " commutator_rows=64\n"
);
CloseStream(progress);;
Print(
    "exported Q=SmallGroup(64,261) cover=", Size(cover),
    " exterior=", Size(exterior), " actions=", Length(coverPcgs), "\n"
);;
QUIT;
