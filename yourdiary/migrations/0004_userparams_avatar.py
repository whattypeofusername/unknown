# Generated by Django 3.1.4 on 2021-04-24 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yourdiary', '0003_tasks_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userparams',
            name='avatar',
            field=models.ImageField(default='users_avatars/default_avatar.png', upload_to='users_avatars/'),
        ),
    ]
