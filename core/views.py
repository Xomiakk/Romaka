from django.shortcuts import render
from core.models import *
from django.db.models import Q


def table(request):
    category_order = ["Цілісність", "Доступність", "Конфіденційність"]
    table_categories = TableCategory.objects.order_by("name")
    table_dict = {}
    sorted_tables = []

    for category_name in category_order:
        category = [c for c in table_categories if c.name == category_name]
        if category:
            table = Table.objects.filter(table_category=category[0]).order_by("name")
            table_dict[category[0]] = table
            sorted_tables.extend(table)

    query = request.GET.get("q")
    if query:
        tables = Table.objects.filter(
            Q(name__icontains=query)
            | Q(threat__icontains=query)
            | Q(source_of_threat__icontains=query)
            | Q(mechanism__icontains=query)
        )

    else:
        tables = sorted_tables

    return render(request, "index.html", {"tables": tables, "query": query})


def integrity(request):
    category_order = ["Цілісність"]
    table_categories = TableCategory.objects.order_by("name")
    table_dict = {}
    sorted_tables = []

    for category_name in category_order:
        category = [c for c in table_categories if c.name == category_name]
        if category:
            table = Table.objects.filter(table_category=category[0]).order_by("name")
            table_dict[category[0]] = table
            sorted_tables.extend(table)

    query = request.GET.get("q")
    if query:
        tables = Table.objects.filter(
            table_category=TableCategory.objects.get(name="Цілісність")
        ).filter(
            Q(name__icontains=query)
            | Q(threat__icontains=query)
            | Q(source_of_threat__icontains=query)
            | Q(mechanism__icontains=query)
        )
    else:
        tables = sorted_tables

    return render(request, "integrity.html", {"tables": tables, "query": query})


def accessibility(request):
    category_order = ["Доступність"]
    table_categories = TableCategory.objects.order_by("name")
    table_dict = {}
    sorted_tables = []

    for category_name in category_order:
        category = [c for c in table_categories if c.name == category_name]
        if category:
            table = Table.objects.filter(table_category=category[0]).order_by("name")
            table_dict[category[0]] = table
            sorted_tables.extend(table)

    query = request.GET.get("q")
    if query:
        tables = Table.objects.filter(
            table_category=TableCategory.objects.get(name="Доступність")
        ).filter(
            Q(name__icontains=query)
            | Q(threat__icontains=query)
            | Q(source_of_threat__icontains=query)
            | Q(mechanism__icontains=query)
        )
    else:
        tables = sorted_tables

    return render(request, "accessibility.html", {"tables": tables, "query": query})


def privacy(request):
    category_order = ["Конфіденційність"]
    table_categories = TableCategory.objects.order_by("name")
    table_dict = {}
    sorted_tables = []

    for category_name in category_order:
        category = [c for c in table_categories if c.name == category_name]
        if category:
            table = Table.objects.filter(table_category=category[0]).order_by("name")
            table_dict[category[0]] = table
            sorted_tables.extend(table)

    query = request.GET.get("q")
    if query:
        tables = Table.objects.filter(
            table_category=TableCategory.objects.get(name="Конфіденційність")
        ).filter(
            Q(name__icontains=query)
            | Q(threat__icontains=query)
            | Q(source_of_threat__icontains=query)
            | Q(mechanism__icontains=query)
        )
    else:
        tables = sorted_tables

    return render(request, "privacy.html", {"tables": tables, "query": query})
