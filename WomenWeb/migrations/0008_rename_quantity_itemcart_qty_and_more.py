# Generated by Django 4.1.2 on 2023-01-20 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WomenWeb', '0007_rename_totalprice_itemcart_totalprice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemcart',
            old_name='Quantity',
            new_name='qty',
        ),
        migrations.RenameField(
            model_name='itemcart',
            old_name='Totalprice',
            new_name='totalprice',
        ),
    ]
