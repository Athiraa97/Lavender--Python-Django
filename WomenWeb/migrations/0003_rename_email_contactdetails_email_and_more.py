# Generated by Django 4.1.2 on 2023-01-04 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WomenWeb', '0002_contactdetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactdetails',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='contactdetails',
            old_name='subject',
            new_name='Subject',
        ),
    ]
