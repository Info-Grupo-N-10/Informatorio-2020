# Generated by Django 3.0 on 2020-09-18 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publicacion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoritos', to='publicacion.Publicaciones', verbose_name='Publicacion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoritos', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'db_table': 'Favorito',
            },
        ),
    ]