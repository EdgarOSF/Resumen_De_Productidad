# Generated by Django 4.1.4 on 2023-02-13 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de Itinerancia')),
                ('municipio_sede', models.CharField(max_length=200, verbose_name='Municipio Sede')),
                ('poblado_sede', models.CharField(max_length=200, verbose_name='Municipio Sede')),
                ('total_asuntos', models.DecimalField(decimal_places=0, max_digits=2)),
                ('sentencias', models.DecimalField(decimal_places=0, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio_Atendido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Municipio')),
                ('nucleos_poblacion', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Nucleos de Poblacion')),
                ('fk_itinerancia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipio_itinerancia', to='itinerancia.itinerancia')),
            ],
        ),
    ]
