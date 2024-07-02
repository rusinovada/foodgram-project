# Generated by Django 2.2.16 on 2022-10-23 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20221020_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipetag',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_tag', to='recipes.Recipe', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='recipetag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_tag', to='recipes.Tag', verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(db_index=True, max_length=200, unique=True, verbose_name='Название тега'),
        ),
    ]
