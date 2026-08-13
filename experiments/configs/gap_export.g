# GAP 4.16 / SmallGrp cross-check exporter for Erdős Problem 117.
#
# Usage from the repository root (the optional-package warnings are harmless):
#   work/gap-4.16.0/gap -l 'work/gap-4.16.0;' -q \
#     -c 'ERDOS117_ORDER:=32;; ERDOS117_OUTPUT:="experiments/logs/gap_smallgroups_order32.tsv";; Read("experiments/configs/gap_export.g");'
#
# The output is a dependency-neutral TSV multiplication-table export.  Python
# then recomputes center cosets, clique number, chromatic number, and abelian
# covers without trusting GAP's graph algorithms.

if LoadPackage("smallgrp") = fail then
    Error("SmallGrp is required");
fi;

if not IsBound(ERDOS117_ORDER) or not IsBound(ERDOS117_OUTPUT) then
    Error("set ERDOS117_ORDER and ERDOS117_OUTPUT before reading this script");
fi;
order := ERDOS117_ORDER;
output := ERDOS117_OUTPUT;
if not IsInt(order) or order < 1 then
    Error("ORDER must be a positive integer");
fi;

stream := OutputTextFile(output, false);
SetPrintFormattingStatus(stream, false);
AppendTo(stream, "# GAP_VERSION\t", GAPInfo.Version, "\n");
AppendTo(stream, "# SMALLGRP_VERSION\t", PackageInfo("smallgrp")[1].Version, "\n");
AppendTo(stream, "# ORDER\t", order, "\n");
AppendTo(stream, "# COUNT\t", NumberSmallGroups(order), "\n");
AppendTo(stream, "group_id\tstructure_description\telement_count\telements\tmultiplication_table\n");

for identifier in [1 .. NumberSmallGroups(order)] do
    group := SmallGroup(order, identifier);
    elements := AsList(group);
    labels := List([1 .. Length(elements)], String);
    table := [];
    for left in elements do
        row := [];
        for right in elements do
            Add(row, Position(elements, left * right));
        od;
        Add(table, row);
    od;
    tableRows := List(table, row -> JoinStringsWithSeparator(List(row, String), ","));
    AppendTo(
        stream,
        "SmallGroup(", order, ",", identifier, ")\t",
        StructureDescription(group), "\t",
        Length(elements), "\t",
        JoinStringsWithSeparator(labels, ","), "\t",
        JoinStringsWithSeparator(tableRows, ";"), "\n"
    );
od;
CloseStream(stream);
Print("exported ", NumberSmallGroups(order), " groups of order ", order, " to ", output, "\n");
QUIT;
