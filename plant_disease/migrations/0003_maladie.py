# Generated by Django 5.1.2 on 2024-10-18 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_disease', '0002_plante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maladie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('bactérienne', 'Bactérienne'), ('fongique', 'Fongique'), ('virale', 'Virale')], max_length=50)),
                ('plantes', models.ManyToManyField(related_name='maladies', to='plant_disease.plante')),
            ],
        ),
    ]