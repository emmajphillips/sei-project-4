# Generated by Django 3.0.7 on 2020-06-05 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('job_title', models.CharField(blank=True, default='', max_length=60)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=60)),
            ],
        ),
    ]