# Generated by Django 4.1.6 on 2023-03-05 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pontos_turisticos', '0005_alter_pontoturistico_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(default=1, upload_to='PontoTuristico'),
            preserve_default=False,
        ),
    ]