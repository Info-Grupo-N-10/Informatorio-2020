# Generated by Django 3.0 on 2020-09-19 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0005_auto_20200919_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenes_publicaciones',
            name='img',
            field=models.ImageField(upload_to='publicaciones'),
        ),
    ]
