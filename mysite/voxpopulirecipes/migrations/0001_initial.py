# Generated by Django 5.1.1 on 2024-09-16 17:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_text', models.CharField(max_length=200)),
                ('ingredient_amount', models.CharField(max_length=200)),
                ('ingredient_unit', models.CharField(max_length=200)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voxpopulirecipes.recipe')),
            ],
        ),
    ]