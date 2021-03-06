# Generated by Django 3.0.7 on 2020-06-06 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task_categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=1000)),
                ('added_date', models.DateField(auto_now_add=True)),
                ('reminder_date', models.DateField(blank=True, null=True)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_tasks', to='jobs.Job')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_tasks', to=settings.AUTH_USER_MODEL)),
                ('task_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='task_categories.TaskCategory')),
            ],
        ),
    ]
