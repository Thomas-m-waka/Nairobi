# Generated by Django 4.2.2 on 2023-06-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('max', '0007_delete_guard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='withvehicle',
            name='security_guard_name',
        ),
        migrations.AddField(
            model_name='withoutvehicle',
            name='id_photo',
            field=models.ImageField(default=2, upload_to='id_photos/'),
            preserve_default=False,
        ),
    ]
