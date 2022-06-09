# Generated by Django 4.0.4 on 2022-06-06 20:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0002_alter_laboratorio_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripción', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='entradas_blog',
            name='imagen',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='foto',
            field=models.ImageField(upload_to='media/'),
        ),
    ]