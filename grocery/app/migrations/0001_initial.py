# Generated by Django 4.0.6 on 2022-07-25 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_item', models.CharField(choices=[('None', 'None'), ('FoodGrains & Oils', 'FoodGrains & Oils'), ('Fruits & Veg', 'Fruits & Veg'), ('Snacks', 'Snacks'), ('Dairy Products', 'Dairy Products'), ('Personal Care', 'Personal Care'), ('Home Care', 'Home Care')], default='None', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_item', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='0', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviews_item', models.CharField(choices=[('None', 'None'), ('Excellent', 'Excellent'), ('Good', 'Good'), ('Average', 'Average'), ('Bad', 'Bad')], default='None', max_length=10)),
            ],
        ),
    ]
