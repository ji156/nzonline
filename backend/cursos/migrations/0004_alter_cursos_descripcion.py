# Generated by Django 4.2.4 on 2024-01-03 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_alter_cursos_categoria_alter_cursos_puntuacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
