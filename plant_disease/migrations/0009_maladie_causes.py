# Generated by Django 5.1.2 on 2024-10-29 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_disease', '0008_symptome_plante'),
    ]

    operations = [
        migrations.AddField(
            model_name='maladie',
            name='causes',
            field=models.ManyToManyField(blank=True, related_name='maladies', to='plant_disease.causemaladie'),
        ),
    ]
