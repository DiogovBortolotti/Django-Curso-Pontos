# Generated by Django 4.1.6 on 2023-03-05 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pontos_turisticos', '0006_pontoturistico_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]
