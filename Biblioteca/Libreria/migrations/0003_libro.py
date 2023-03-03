# Generated by Django 4.1.7 on 2023-02-22 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Libreria', '0002_alter_autor_options_remove_autor_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255, verbose_name='Titulo')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de publicacion')),
                ('autor_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Libreria.autor')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['titulo'],
            },
        ),
    ]
