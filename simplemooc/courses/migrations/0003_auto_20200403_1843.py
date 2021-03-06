# Generated by Django 3.0.5 on 2020-04-03 18:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('courses', '0002_auto_20200403_0012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['name'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AddField(
            model_name='course',
            name='about',
            field=models.TextField(blank=True, verbose_name='Sobre o curso'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descrição simples'),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data de início'),
        ),
    ]
