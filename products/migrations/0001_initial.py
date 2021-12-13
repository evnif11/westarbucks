# Generated by Django 4.0 on 2021-12-10 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'allergy',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('korean_name', models.CharField(max_length=100)),
                ('english_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('allergy', models.ManyToManyField(to='products.Allergy')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
            options={
                'db_table': 'drink',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('size_ml', models.IntegerField()),
                ('size_fluid_ounce', models.IntegerField()),
            ],
            options={
                'db_table': 'size',
            },
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_serving_kcal', models.IntegerField()),
                ('sodium_mg', models.IntegerField()),
                ('saturated_fat_g', models.IntegerField()),
                ('sugars_g', models.IntegerField()),
                ('protein_g', models.IntegerField()),
                ('caffeine_mg', models.IntegerField()),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drink')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.size')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drink')),
            ],
            options={
                'db_table': 'image',
            },
        ),
        migrations.AddField(
            model_name='drink',
            name='size',
            field=models.ManyToManyField(through='products.Nutrition', to='products.Size'),
        ),
        migrations.AddField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.menu'),
        ),
    ]