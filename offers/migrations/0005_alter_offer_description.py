# Generated by Django 4.1.13 on 2023-12-06 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0004_alter_offer_category_alter_offer_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=models.CharField(blank=True, max_length=400, verbose_name='описание'),
        ),
    ]
