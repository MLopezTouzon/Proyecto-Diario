# Generated by Django 4.0.5 on 2022-08-06 22:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppDiario', '0022_alter_posteodeportes_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteodeportes',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='posteodeportes',
            name='titulo',
            field=ckeditor.fields.RichTextField(max_length=100),
        ),
    ]
