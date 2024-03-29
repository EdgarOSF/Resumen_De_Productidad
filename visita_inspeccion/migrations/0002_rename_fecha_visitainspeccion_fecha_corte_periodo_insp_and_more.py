# Generated by Django 4.1.4 on 2023-01-20 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visita_inspeccion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitainspeccion',
            old_name='fecha',
            new_name='fecha_corte_periodo_insp',
        ),
        migrations.RenameField(
            model_name='visitainspeccion',
            old_name='fecha_corte',
            new_name='fecha_inicio_periodo_insp',
        ),
        migrations.RenameField(
            model_name='visitainspeccion',
            old_name='fecha_inicio_insp',
            new_name='fecha_realizacion',
        ),
        migrations.AddField(
            model_name='visitainspeccion',
            name='duracion',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visitainspeccion',
            name='realizo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
