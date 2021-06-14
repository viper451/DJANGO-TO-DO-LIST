# Generated by Django 3.2 on 2021-06-11 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0004_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createuserform',
            name='username',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='todolist', to=settings.AUTH_USER_MODEL),
        ),
    ]