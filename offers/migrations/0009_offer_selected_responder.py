# Generated by Django 4.1.13 on 2023-12-14 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('offers', '0008_alter_offer_options_offer_pub_date_alter_photo_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='selected_responder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='selected_responders', to=settings.AUTH_USER_MODEL, verbose_name='выбран'),
        ),
    ]
