# Generated by Django 4.1.2 on 2023-01-03 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WomenWeb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('Message', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
