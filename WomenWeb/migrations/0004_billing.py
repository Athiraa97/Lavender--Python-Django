# Generated by Django 4.1.2 on 2023-01-14 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WomenWeb', '0003_rename_email_contactdetails_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(blank=True, max_length=30, null=True)),
                ('Lname', models.CharField(blank=True, max_length=30, null=True)),
                ('Uname', models.CharField(blank=True, max_length=30, null=True)),
                ('Email', models.CharField(blank=True, max_length=30, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
