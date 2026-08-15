# Export the abelianization coordinates and full quotient-automorphism
# generators used by the cutoff-nine SG(128,2320) restriction audit.

if LoadPackage("smallgrp") = fail then
    Error("SmallGrp is required");
fi;
if not IsBound(ERDOS117_OUTPUT) then
    Error("set ERDOS117_OUTPUT");
fi;

q := SmallGroup(64, 261);;
elements := AsList(q);;
derived := DerivedSubgroup(q);;
abelianizationMap := NaturalHomomorphismByNormalSubgroup(q, derived);;
abelianization := Image(abelianizationMap);;
abelianizationIso := IsomorphismPcGroup(abelianization);;
abelianizationPc := Image(abelianizationIso);;
abelianizationPcgs := Pcgs(abelianizationPc);;
automorphisms := AutomorphismGroup(q);;
automorphismGenerators := GeneratorsOfGroup(automorphisms);;

stream := OutputTextFile(ERDOS117_OUTPUT, false);;
SetPrintFormattingStatus(stream, false);;
AppendTo(stream, "# GAP_VERSION=", GAPInfo.Version, "\n");
AppendTo(
    stream, "# SMALLGRP_VERSION=", InstalledPackageVersion("smallgrp"), "\n"
);
AppendTo(stream, "# Q_ORDER=64\n");
AppendTo(stream, "# Q_ID=261\n");
AppendTo(stream, "# STRUCTURE=", StructureDescription(q), "\n");
AppendTo(stream, "# DERIVED_ORDER=", Size(derived), "\n");
AppendTo(stream, "# ABELIANIZATION_ORDER=", Size(abelianization), "\n");
AppendTo(
    stream, "# ABELIANIZATION_RELATIVE_ORDERS=",
    JoinStringsWithSeparator(List(RelativeOrders(abelianizationPcgs), String), ","),
    "\n"
);
AppendTo(stream, "# AUTOMORPHISM_GROUP_ORDER=", Size(automorphisms), "\n");
AppendTo(stream, "# AUTOMORPHISM_GENERATOR_COUNT=", Length(automorphismGenerators), "\n");

AppendTo(stream, "ABELIANIZATION\n");
AppendTo(stream, "vertex\tcoordinates\n");
for index in [1 .. Length(elements)] do
    image := Image(
        abelianizationIso,
        Image(abelianizationMap, elements[index])
    );
    AppendTo(
        stream, index - 1, "\t",
        JoinStringsWithSeparator(
            List(ExponentsOfPcElement(abelianizationPcgs, image), String), ","
        ),
        "\n"
    );
od;

AppendTo(stream, "AUTOMORPHISMS\n");
AppendTo(stream, "generator\tpermutation\n");
for index in [1 .. Length(automorphismGenerators)] do
    permutation := List(
        elements,
        element -> Position(
            elements,
            Image(automorphismGenerators[index], element)
        ) - 1
    );
    AppendTo(
        stream, index, "\t",
        JoinStringsWithSeparator(List(permutation, String), ","), "\n"
    );
od;

CloseStream(stream);;
SetPrintFormattingStatus(OutputTextUser(), false);;
Print(
    "[COMPUTED] exported SG261 abelianization and automorphisms: abelianization=",
    Size(abelianization), " automorphism_group=", Size(automorphisms),
    " generators=", Length(automorphismGenerators), "\n"
);
QUIT;
