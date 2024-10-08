# Generated by Django 5.1.1 on 2024-09-17 19:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voxpopulirecipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction_text', models.CharField(max_length=200)),
                ('instruction_order', models.IntegerField(default=0)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voxpopulirecipes.recipe')),
            ],
        ),
    ]
