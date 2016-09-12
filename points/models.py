from django.db import models

class Category(models.Model):
    lbl = models.CharField('label', max_length=32, blank=False)
    clr = models.PositiveIntegerField('color', blank=False)

class Point(models.Model):
    cat = models.ForeignKey(Category)
    lat = models.DecimalField('latitude', max_digits=9, decimal_places=6, blank=True)
    lon = models.DecimalField('longitude', max_digits=9, decimal_places=6, blank=True)
    lbl = models.CharField('label', max_length=256)

