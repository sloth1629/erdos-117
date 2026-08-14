# Fast complete inventory for every quotient Q relevant to f(7)=81.
#
# AbelianInvariantsMultiplier avoids constructing a Schur cover.  The exact
# identity |Q wedge Q|=|M(Q)| |Q'| gives the exterior-square order, while the
# multiplier invariants identify the cases whose raw subgroup lattices are
# already visibly impossible to enumerate.  A later bounded scan constructs
# chosen covers only for cases selected from this inventory.

if LoadPackage("smallgrp") = fail then
    Error("SmallGrp is required");
fi;
if not IsBound(ERDOS117_OUTPUT) or not IsBound(ERDOS117_MAX_Q_ORDER) then
    Error("set ERDOS117_OUTPUT and ERDOS117_MAX_Q_ORDER");
fi;

Erdos117JoinIntegers := function(values)
return JoinStringsWithSeparator(List(values, String), ",");
end;;

RunErdos117H7QuotientInventory := function()
local stream, total, qOrder, qId, numberGroups, quotient, multiplier,
    multiplierOrder, derivedOrder, exteriorOrder, startTime, elapsed;

stream := OutputTextFile(ERDOS117_OUTPUT, false);
SetPrintFormattingStatus(stream, false);
AppendTo(stream, "# GAP_VERSION=", GAPInfo.Version, "\n");
AppendTo(stream, "# SMALLGRP_VERSION=", InstalledPackageVersion("smallgrp"), "\n");
AppendTo(stream, "# MAX_Q_ORDER=", ERDOS117_MAX_Q_ORDER, "\n");
AppendTo(stream, "# IDENTITY=|Q_wedge_Q|=|M(Q)|*|Q'|\n");
AppendTo(stream, "# NO_SCHUR_COVER_CONSTRUCTED=true\n");
AppendTo(
    stream,
    "q_order\tq_id\tstructure\tq_abelian\tq_elementary_abelian\t",
    "q_exponent\tq_derived_order\tq_center_order\tmultiplier_order\t",
    "multiplier_invariants\tmultiplier_generator_count\t",
    "exterior_order\tabout_exterior_structure\truntime_ms\n"
);

total := 0;
for qOrder in [1 .. ERDOS117_MAX_Q_ORDER] do
    numberGroups := NumberSmallGroups(qOrder);
    for qId in [1 .. numberGroups] do
        startTime := Runtime();
        quotient := SmallGroup(qOrder, qId);
        multiplier := AbelianInvariantsMultiplier(quotient);
        multiplierOrder := Product(multiplier);
        derivedOrder := Size(DerivedSubgroup(quotient));
        exteriorOrder := multiplierOrder * derivedOrder;
        elapsed := Runtime() - startTime;
        AppendTo(
            stream,
            qOrder, "\t", qId, "\t", StructureDescription(quotient), "\t",
            IsAbelian(quotient), "\t", IsElementaryAbelian(quotient), "\t",
            Exponent(quotient), "\t", derivedOrder, "\t",
            Size(Centre(quotient)), "\t", multiplierOrder, "\t",
            Erdos117JoinIntegers(multiplier), "\t", Length(multiplier), "\t",
            exteriorOrder, "\t"
        );
        if IsAbelian(quotient) then
            AppendTo(stream, "multiplier_is_exact_exterior_structure");
        else
            AppendTo(stream, "extension_of_Qprime_by_multiplier");
        fi;
        AppendTo(stream, "\t", elapsed, "\n");
        total := total + 1;
    od;
od;
CloseStream(stream);
Print("completed h7 quotient inventory; quotients=", total, "\n");
end;;

RunErdos117H7QuotientInventory();;
QUIT;
