from django.db import models

class TableCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = 'Категорія таблиці'
        verbose_name_plural = 'Категорії таблиць'

class Table(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    owner = models.CharField(max_length=128, blank=True, null=True, default=None)
    place = models.CharField(max_length=128, blank=True, null=True, default=None)
    table_category = models.ForeignKey(TableCategory,on_delete=models.CASCADE, blank=True, null=True, default=None)
    asset_category = models.CharField(max_length=64, blank=True, null=True, default=None)
    threat = models.TextField(blank=True, null=True, default=None)
    risk = models.CharField(max_length=8, blank=True, null=True, default=None)
    source_of_threat = models.TextField(blank=True, null=True, default=None)
    mechanism = models.TextField(blank=True, null=True, default=None)
	
    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = "Таблиця"
        verbose_name_plural = "Таблиці"