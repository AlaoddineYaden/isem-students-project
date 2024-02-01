# Generated by Django 5.0.1 on 2024-02-01 17:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudient', '0005_note_matiere_note_note_alter_module_coefficient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matiere',
            name='coefficient',
            field=models.FloatField(default='0.0', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='module',
            name='coefficient',
            field=models.FloatField(default='0.0', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='note',
            name='coefficient',
            field=models.FloatField(default='0.0', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
    ]