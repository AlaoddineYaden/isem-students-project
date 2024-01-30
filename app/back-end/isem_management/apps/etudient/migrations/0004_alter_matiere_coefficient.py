# Generated by Django 5.0.1 on 2024-01-30 15:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudient', '0003_matiere_publier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matiere',
            name='coefficient',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)]),
        ),
    ]