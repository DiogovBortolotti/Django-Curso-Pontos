# Generated by Django 4.1.6 on 2023-02-02 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('pontos_turisticos', '0003_pontoturistico_avaliacoes_pontoturistico_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enderecos.endereco'),
            preserve_default=False,
        ),
    ]
