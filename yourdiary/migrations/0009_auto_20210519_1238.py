# Generated by Django 3.1.4 on 2021-05-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yourdiary', '0008_tasks_done_indicator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='deadline',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='hostId',
            field=models.DateField(),
        ),
    ]