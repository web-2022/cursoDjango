# Generated by Django 4.2.6 on 2024-09-01 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departamento',
            name='nombreDeoartamento',
        ),
        migrations.AddField(
            model_name='departamento',
            name='nombreDepartamento',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='descripcionDepartamento',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
