# Generated by Django 3.2.4 on 2021-11-02 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20211102_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university',
            old_name='course_id',
            new_name='course',
        ),
    ]
