from django.contrib import admin
from .models import *


class TableCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TableCategory._meta.fields]

    class Meta:
        model = TableCategory


admin.site.register(TableCategory, TableCategoryAdmin)


class TableAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Table._meta.fields]

    class Meta:
        model = Table


admin.site.register(Table, TableAdmin)
