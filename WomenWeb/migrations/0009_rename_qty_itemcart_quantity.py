# Generated by Django 4.1.2 on 2023-01-20 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WomenWeb', '0008_rename_quantity_itemcart_qty_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemcart',
            old_name='qty',
            new_name='quantity',
        ),
    ]