# Generated by Django 3.0.7 on 2020-06-06 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0002_contact_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_contacts', to=settings.AUTH_USER_MODEL),
        ),
    ]
