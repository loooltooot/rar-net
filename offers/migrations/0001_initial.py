# Generated by Django 4.1.13 on 2023-12-06 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='')),
                ('description', models.CharField(max_length=400, verbose_name='')),
                ('category', models.CharField(choices=[('buy', 'купить'), ('sell', 'продать')], default='buy', max_length=20, verbose_name='')),
                ('statuses', models.CharField(choices=[('active', 'активно'), ('closed', 'закрыто')], default='active', max_length=20, verbose_name='')),
            ],
            options={
                'verbose_name': 'заявка',
                'verbose_name_plural': 'заявки',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='фото')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offers.offer')),
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'фотографии',
            },
        ),
    ]
