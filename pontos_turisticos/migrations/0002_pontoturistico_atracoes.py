# Generated by Django 4.1.6 on 2023-02-02 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
        ('pontos_turisticos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='atracoes',
            field=models.ManyToManyField(to='atracoes.atracao'),
        ),
    ]
