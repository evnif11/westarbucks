# Generated by Django 4.0 on 2021-12-12 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_nutrition_caffeine_mg_alter_nutrition_drink_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drink',
            old_name='nutritions',
            new_name='sizes',
        ),
    ]
