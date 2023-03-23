import math

from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(verbose_name='公司名称',unique=True,max_length=0xffffffff)
    score = models.FloatField(default=0.0,verbose_name='公司ESG得分')

    class Meta:
        db_table='tb_company'
        verbose_name='公司'