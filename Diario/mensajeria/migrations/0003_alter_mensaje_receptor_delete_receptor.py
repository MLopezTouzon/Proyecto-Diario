# Generated by Django 4.0.5 on 2022-08-09 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDiario', '0029_users'),
        ('mensajeria', '0002_receptor_alter_mensaje_options_delete_hilo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='receptor',
            field=models.ManyToManyField(to='AppDiario.users'),
        ),
        migrations.DeleteModel(
            name='Receptor',
        ),
    ]