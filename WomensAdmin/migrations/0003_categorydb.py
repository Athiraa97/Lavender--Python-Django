# Generated by Django 4.1.2 on 2022-12-30 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WomensAdmin', '0002_rename_admindb_employeedb'),
    ]

    operations = [
        migrations.CreateModel(
            name='categorydb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CName', models.CharField(blank=True, max_length=50, null=True)),
                ('CImage', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
