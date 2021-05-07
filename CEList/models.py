from django.db import models


class List(models.Model):
    pass


class Item(models.Model):
    nitem = models.TextField(default='')
    nname = models.TextField(default='')
    nAddress = models.TextField(default='')
    nprice = models.TextField(default='')
    ndate = models.TextField(default='') 
    list = models.ForeignKey(List, default=None, on_delete=models.PROTECT)
