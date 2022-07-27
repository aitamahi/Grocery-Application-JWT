# Generated by Django 4.0.6 on 2022-07-25 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_variant_alter_category_category_item_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='Qty_value',
            field=models.CharField(choices=[('0', '0'), ('FoodGrains', (('1Kg', '1Kg'), ('2Kg', '2Kg'), ('5Kg', '5Kg'), ('10Kg', '10Kg'))), ('Oils', (('1L', '1L'), ('2L', '2L'), ('5L', '5L'), ('10L', '10L'))), ('Fruits & Veg', (('1Kg', '1Kg'), ('2Kg', '2Kg'), ('5Kg', '5Kg'), ('10Kg', '10Kg'))), ('Snacks', (('100gm', '100gm'), ('200gm', '200gm'), ('500gm', '500gm'), ('750gm', '750gm'))), ('Dairy Products', (('1L', '1L'), ('2L', '2L'), ('5L', '5L'), ('10L', '10L'))), ('Personal Care', (('1', '1'), ('2', '2'), ('5', '5'), ('10', '10')))], default='0', max_length=50),
        ),
    ]
