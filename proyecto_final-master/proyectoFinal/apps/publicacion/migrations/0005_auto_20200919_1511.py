# Generated by Django 3.0 on 2020-09-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0004_auto_20200918_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenes_publicaciones',
            name='img',
            field=models.ImageField(upload_to='perfiles'),
        ),
    ]
