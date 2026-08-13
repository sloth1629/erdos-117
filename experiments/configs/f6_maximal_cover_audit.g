# Modern GAP audit of every finite assertion in Alencar (2011), Lemma 4.1,
# together with the A5/S5 and C2 x S3 x S3 checks used by the reconstructed
# maximal irredundant core-free six-cover argument.

if LoadPackage("smallgrp") = fail then
    Error("SmallGrp is required");
fi;
if not IsBound(ERDOS117_CLASS_OUTPUT) or not IsBound(ERDOS117_COVER_OUTPUT)
   or not IsBound(ERDOS117_STDOUT_LOG) then
    Error("set ERDOS117_CLASS_OUTPUT, ERDOS117_COVER_OUTPUT, ERDOS117_STDOUT_LOG");
fi;

Erdos117MaskInteger := function(elements, subgroup)
return Sum(AsList(subgroup), element -> 2 ^ (Position(elements, element) - 1));
end;;

Erdos117JoinIntegers := function(values)
return JoinStringsWithSeparator(List(values, String), ",");
end;;

Erdos117AuditSixCovers := function(group)
local elements, order, maximals, masks, full, statistics, chosen, search;
elements := AsList(group);
order := Length(elements);
maximals := MaximalSubgroups(group);
masks := List(
    maximals,
    subgroup -> BlistList(elements, AsList(subgroup))
);
full := BlistList(elements, elements);
statistics := rec(
    combination_count := 0,
    cover_count := 0,
    irredundant_cover_count := 0,
    corefree_irredundant_cover_count := 0,
    qualifying := []
);
chosen := [];
search := function(start, depth)
local last, index, union, otherUnion, position, irredundant, intersectionMask,
    intersectionSubgroup, core, combination;
if depth = 7 then
    statistics.combination_count := statistics.combination_count + 1;
    union := BlistList(elements, []);
    for index in chosen do
        UniteBlist(union, masks[index]);
    od;
    if SizeBlist(union) <> order then
        return;
    fi;
    statistics.cover_count := statistics.cover_count + 1;
    irredundant := true;
    for position in [1 .. 6] do
        otherUnion := BlistList(elements, []);
        for index in [1 .. 6] do
            if index <> position then
                UniteBlist(otherUnion, masks[chosen[index]]);
            fi;
        od;
        if SizeBlist(DifferenceBlist(masks[chosen[position]], otherUnion)) = 0 then
            irredundant := false;
            break;
        fi;
    od;
    if not irredundant then
        return;
    fi;
    statistics.irredundant_cover_count :=
        statistics.irredundant_cover_count + 1;
    intersectionMask := ShallowCopy(masks[chosen[1]]);
    for position in [2 .. 6] do
        IntersectBlist(intersectionMask, masks[chosen[position]]);
    od;
    intersectionSubgroup := Intersection(List(chosen, index -> maximals[index]));
    if SizeBlist(intersectionMask) <> Size(intersectionSubgroup) then
        Error("bitmask and subgroup intersections disagree");
    fi;
    core := Core(group, intersectionSubgroup);
    if Size(core) <> 1 then
        return;
    fi;
    statistics.corefree_irredundant_cover_count :=
        statistics.corefree_irredundant_cover_count + 1;
    combination := ShallowCopy(chosen);
    Add(
        statistics.qualifying,
        rec(
            combination := combination,
            intersection_order := Size(intersectionSubgroup),
            intersection_mask := Sum(
                ListBlist(elements, intersectionMask),
                element -> 2 ^ (Position(elements, element) - 1)
            )
        )
    );
    return;
fi;
last := Length(maximals) - (6 - depth);
for index in [start .. last] do
    chosen[depth] := index;
    search(index + 1, depth + 1);
od;
if IsBound(chosen[depth]) then
    Unbind(chosen[depth]);
fi;
end;
if Length(maximals) >= 6 then
    search(1, 1);
fi;
return rec(
    elements := elements,
    maximals := maximals,
    maximal_masks := List(
        maximals,
        subgroup -> Erdos117MaskInteger(elements, subgroup)
    ),
    statistics := statistics
);
end;;

RunErdos117F6Audit := function()
local classStream, coverStream, progress, registered, register, emitClass,
    s3, s4, s3cube, s4square, c2s3square, classes, selected, projections,
    family, order, class, serial, group, id, centerless, numberGroups,
    groupRecord, audit, tableRows, maximalSizes, qualifyingStrings,
    intersectionDistribution, elapsed, startTime;

classStream := OutputTextFile(ERDOS117_CLASS_OUTPUT, false);
coverStream := OutputTextFile(ERDOS117_COVER_OUTPUT, false);
progress := OutputTextFile(ERDOS117_STDOUT_LOG, false);
SetPrintFormattingStatus(classStream, false);
SetPrintFormattingStatus(coverStream, false);
SetPrintFormattingStatus(progress, false);
for class in [classStream, coverStream] do
    AppendTo(class, "# GAP_VERSION=", GAPInfo.Version, "\n");
    AppendTo(class, "# SMALLGRP_VERSION=", InstalledPackageVersion("smallgrp"), "\n");
    AppendTo(class, "# COVER_SIZE=6\n");
od;
AppendTo(
    classStream,
    "family\tambient\tclass_serial\tclass_size\tsubgroup_order\tgroup_id\t",
    "structure\tcenter_order\tprojection_sizes\tselected_for_cover\n"
);
AppendTo(
    coverStream,
    "group_id\tstructure\torder\tcase_tags\telements\tmultiplication_table\t",
    "maximal_count\tmaximal_orders\tmaximal_masks\tsix_combinations\t",
    "cover_count\tirredundant_cover_count\tqualifying_count\t",
    "intersection_distribution\tqualifying_covers\n"
);

registered := [];
register := function(subgroup, tag)
local subgroupId, position;
subgroupId := IdGroup(subgroup);
position := PositionProperty(registered, record -> record.id = subgroupId);
if position = fail then
    Add(
        registered,
        rec(
            id := subgroupId,
            group := SmallGroup(subgroupId[1], subgroupId[2]),
            tags := [tag]
        )
    );
else
    if not tag in registered[position].tags then
        Add(registered[position].tags, tag);
    fi;
fi;
end;
emitClass := function(familyName, ambientName, classSerial, classSize,
                      subgroup, projectionSizes, selectForCover)
local subgroupId;
subgroupId := IdGroup(subgroup);
AppendTo(
    classStream,
    familyName, "\t", ambientName, "\t", classSerial, "\t", classSize,
    "\t", Size(subgroup), "\t", subgroupId[1], ",", subgroupId[2],
    "\t", StructureDescription(subgroup), "\t", Size(Centre(subgroup)),
    "\t", Erdos117JoinIntegers(projectionSizes), "\t", selectForCover, "\n"
);
if selectForCover then
    register(subgroup, familyName);
fi;
end;

s3 := SymmetricGroup(3);
s4 := SymmetricGroup(4);
s3cube := DirectProduct(s3, s3, s3);
s4square := DirectProduct(s4, s4);
c2s3square := DirectProduct(CyclicGroup(2), s3, s3);

emitClass("semisimple_A5", "A5", 1, 1, AlternatingGroup(5), [], true);
emitClass("semisimple_S5", "S5", 1, 1, SymmetricGroup(5), [], true);
emitClass("lemma_1a_S3cube", "S3^3", 1, 1, s3cube, [], true);
emitClass(
    "lemma_1a_C2C3S3", "C2xC3xS3", 1, 1,
    DirectProduct(CyclicGroup(2), CyclicGroup(3), s3), [], true
);
classes := ConjugacyClassesSubgroups(s4);
for serial in [1 .. Length(classes)] do
    class := classes[serial];
    emitClass(
        "auxiliary_S4_all", "S4", serial, Size(class),
        Representative(class), [], true
    );
od;

for order in [72, 108] do
    classes := Filtered(
        ConjugacyClassesSubgroups(s3cube),
        class -> Size(Representative(class)) = order
    );
    family := Concatenation("lemma_1b_S3cube_order", String(order));
    for serial in [1 .. Length(classes)] do
        class := classes[serial];
        emitClass(
            family, "S3^3", serial, Size(class), Representative(class), [], true
        );
    od;
od;

for order in [48, 96] do
    classes := Filtered(
        ConjugacyClassesSubgroups(s4square),
        class -> Size(Representative(class)) = order
    );
    family := Concatenation("lemma_1c_S4square_order", String(order));
    for serial in [1 .. Length(classes)] do
        class := classes[serial];
        emitClass(
            family, "S4^2", serial, Size(class), Representative(class), [], true
        );
    od;
od;

projections := [
    Projection(s3cube, 1), Projection(s3cube, 2), Projection(s3cube, 3)
];
classes := Filtered(
    ConjugacyClassesSubgroups(s3cube),
    class -> ForAll(
        projections,
        projection -> Size(Image(projection, Representative(class))) = 6
    )
);
for serial in [1 .. Length(classes)] do
    class := classes[serial];
    group := Representative(class);
    emitClass(
        "lemma_3_S3cube_subdirect", "S3^3", serial, Size(class), group,
        List(projections, projection -> Size(Image(projection, group))), true
    );
od;

classes := ConjugacyClassesSubgroups(c2s3square);
for serial in [1 .. Length(classes)] do
    class := classes[serial];
    emitClass(
        "auxiliary_C2S3square_all", "C2xS3xS3", serial, Size(class),
        Representative(class), [], true
    );
od;

for order in [50, 100] do
    numberGroups := NumberSmallGroups(order);
    for serial in [1 .. numberGroups] do
        group := SmallGroup(order, serial);
        centerless := Size(Centre(group)) = 1;
        emitClass(
            Concatenation("lemma_2_order", String(order)),
            Concatenation("SmallGroups(", String(order), ")"),
            serial, 1, group, [], centerless
        );
    od;
od;
CloseStream(classStream);

SortBy(registered, record -> 10000 * record.id[1] + record.id[2]);
for groupRecord in registered do
    group := groupRecord.group;
    startTime := Runtime();
    audit := Erdos117AuditSixCovers(group);
    elapsed := Runtime() - startTime;
    tableRows := List(
        audit.elements,
        left -> Erdos117JoinIntegers(
            List(audit.elements, right -> Position(audit.elements, left * right))
        )
    );
    maximalSizes := List(audit.maximals, Size);
    intersectionDistribution := Collected(
        List(audit.statistics.qualifying, record -> record.intersection_order)
    );
    qualifyingStrings := List(
        audit.statistics.qualifying,
        record -> Concatenation(
            Erdos117JoinIntegers(record.combination), "@",
            String(record.intersection_order), "@", String(record.intersection_mask)
        )
    );
    AppendTo(
        coverStream,
        groupRecord.id[1], ",", groupRecord.id[2], "\t",
        StructureDescription(group), "\t", Size(group), "\t",
        JoinStringsWithSeparator(groupRecord.tags, ";"), "\t",
        JoinStringsWithSeparator(List(audit.elements, String), ","), "\t",
        JoinStringsWithSeparator(tableRows, ";"), "\t",
        Length(audit.maximals), "\t", Erdos117JoinIntegers(maximalSizes), "\t",
        Erdos117JoinIntegers(audit.maximal_masks), "\t",
        audit.statistics.combination_count, "\t",
        audit.statistics.cover_count, "\t",
        audit.statistics.irredundant_cover_count, "\t",
        audit.statistics.corefree_irredundant_cover_count, "\t",
        JoinStringsWithSeparator(
            List(
                intersectionDistribution,
                pair -> Concatenation(String(pair[1]), ":", String(pair[2]))
            ),
            ","
        ), "\t", JoinStringsWithSeparator(qualifyingStrings, ";"), "\n"
    );
    AppendTo(
        progress,
        "group=SmallGroup(", groupRecord.id[1], ",", groupRecord.id[2], ")",
        " structure=", StructureDescription(group), " order=", Size(group),
        " maximals=", Length(audit.maximals),
        " combinations=", audit.statistics.combination_count,
        " covers=", audit.statistics.cover_count,
        " irredundant=", audit.statistics.irredundant_cover_count,
        " qualifying=", audit.statistics.corefree_irredundant_cover_count,
        " intersections=", intersectionDistribution,
        " runtime_ms=", elapsed, "\n"
    );
    Print(
        "SmallGroup(", groupRecord.id[1], ",", groupRecord.id[2], ") ",
        StructureDescription(group), " qualifying=",
        audit.statistics.corefree_irredundant_cover_count,
        " runtime_ms=", elapsed, "\n"
    );
od;
AppendTo(
    progress,
    "completed finite maximal-cover audit; unique_groups=", Length(registered),
    "\n"
);
CloseStream(coverStream);
CloseStream(progress);
Print("completed finite maximal-cover audit; unique_groups=", Length(registered), "\n");
end;;

RunErdos117F6Audit();;
QUIT;
