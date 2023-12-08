from django.db import models

# Create your models here.

class Country(models.Model):
    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'
        ordering = ['code']

    code = models.CharField('код', max_length=3, unique=True)
    flag = models.CharField('флаг', max_length=15, unique=True)
    name = models.CharField('название', max_length=50)

    def __str__(self):
        return f'{self.name}' 

class City(models.Model):
    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'
        ordering = ['name']

    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='страна')
    name = models.CharField('название', max_length=50)

    def __str__(self):
        return f'{self.name}' 