# Generated by Django 4.1.13 on 2023-12-06 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0003_rename_statuses_offer_status_alter_offer_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='category',
            field=models.CharField(choices=[('buy', 'купить'), ('sell', 'продать')], default='buy', max_length=20, verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=models.CharField(max_length=400, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='status',
            field=models.CharField(choices=[('active', 'активно'), ('closed', 'закрыто')], default='active', max_length=20, verbose_name='статус'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='title',
            field=models.CharField(max_length=150, verbose_name='название'),
        ),
    ]
