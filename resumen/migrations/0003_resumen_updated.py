# Generated by Django 4.1.4 on 2022-12-08 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumen', '0002_rename_asuntos_ingresados_resumen_asuntos_en_tramite_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumen',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]