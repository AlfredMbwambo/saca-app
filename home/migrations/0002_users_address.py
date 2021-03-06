# Generated by Django 3.2.4 on 2021-10-16 14:04

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='users_address',
            fields=[
                ('address_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('citizenship', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modifield_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.user')),
            ],
            options={
                'db_table': 'addresses',
            },
            managers=[
                ('addresses', django.db.models.manager.Manager()),
            ],
        ),
    ]
