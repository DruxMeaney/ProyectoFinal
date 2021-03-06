# Generated by Django 4.0.4 on 2022-06-02 21:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=254)),
                ('asunto', models.CharField(max_length=250)),
                ('mensaje', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Entradas_blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to='')),
                ('fecha_subido', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripción', models.CharField(max_length=200)),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Linea_de_Investigacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linea_de_investigacion', models.CharField(max_length=200)),
                ('descripción', models.CharField(max_length=200)),
                ('responsable', models.CharField(max_length=200)),
            ],
        ),
    ]
