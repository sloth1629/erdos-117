# Complete multiplication-table export for one proposed local inequality.
# This single-group certificate makes no minimal-counterexample claim.

if LoadPackage("smallgrp") = fail then
    Error("SmallGrp is required");
fi;
if not IsBound(ERDOS117_OUTPUT) or not IsBound(ERDOS117_STDOUT_LOG) then
    Error("set ERDOS117_OUTPUT and ERDOS117_STDOUT_LOG");
fi;

RunErdos117H8LocalInequalityCounterexample := function()
local stream, progress, group, elements, elementCount, tableRows, targetSerial,
    target, centralizer, centralizerPositions;

group := SmallGroup(48, 15);
if IdGroup(group) <> [48, 15] then
    Error("unexpected SmallGroup identifier");
fi;
elements := AsList(group);
elementCount := Length(elements);
targetSerial := 2;
target := elements[targetSerial];
centralizer := Centralizer(group, target);
centralizerPositions := SortedList(
    List(AsList(centralizer), element -> Position(elements, element))
);

if Order(target) <> 2 then
    Error("the selected element does not have order two");
fi;
if Size(centralizer) <> 4 or not IsAbelian(centralizer) then
    Error("unexpected centralizer");
fi;
if Index(group, centralizer) <> 12 then
    Error("unexpected centralizer index");
fi;

tableRows := List(
    [1 .. elementCount],
    i -> JoinStringsWithSeparator(
        List(
            [1 .. elementCount],
            j -> String(Position(elements, elements[i] * elements[j]))
        ),
        ","
    )
);

stream := OutputTextFile(ERDOS117_OUTPUT, false);
progress := OutputTextFile(ERDOS117_STDOUT_LOG, false);
SetPrintFormattingStatus(stream, false);
SetPrintFormattingStatus(progress, false);
AppendTo(stream, "# GAP_VERSION=", GAPInfo.Version, "\n");
AppendTo(
    stream, "# SMALLGRP_VERSION=", InstalledPackageVersion("smallgrp"), "\n"
);
AppendTo(stream, "# SCOPE=single_group_counterexample_only\n");
AppendTo(stream, "# MINIMALITY_CLAIM=false\n");
AppendTo(
    stream,
    "small_group_order\tsmall_group_id\tstructure_description\t",
    "element_count\tmultiplication_table\ttarget_serial\t",
    "target_gap_string\ttarget_order\tcentralizer_positions\t",
    "centralizer_order\tcentralizer_index\tcentralizer_abelian\n"
);
AppendTo(
    stream, "48\t15\t", StructureDescription(group), "\t", elementCount,
    "\t", JoinStringsWithSeparator(tableRows, ";"), "\t", targetSerial,
    "\t", String(target), "\t", Order(target), "\t",
    JoinStringsWithSeparator(List(centralizerPositions, String), ","), "\t",
    Size(centralizer), "\t", Index(group, centralizer), "\t",
    IsAbelian(centralizer), "\n"
);
AppendTo(
    progress, "SmallGroup(48,15) target_serial=2 target=", String(target),
    " centralizer_order=4 centralizer_index=12 centralizer_abelian=true\n"
);
CloseStream(stream);
CloseStream(progress);
Print("completed h8 local-inequality counterexample export\n");
end;;

RunErdos117H8LocalInequalityCounterexample();;
QUIT;
