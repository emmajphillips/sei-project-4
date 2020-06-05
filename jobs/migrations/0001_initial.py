# Generated by Django 3.0.7 on 2020-06-05 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job_status', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=60)),
                ('company', models.CharField(max_length=50)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('job_url', models.CharField(max_length=400)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(max_length=60)),
                ('country', models.CharField(max_length=60)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='job_status.JobStatus')),
            ],
        ),
    ]
