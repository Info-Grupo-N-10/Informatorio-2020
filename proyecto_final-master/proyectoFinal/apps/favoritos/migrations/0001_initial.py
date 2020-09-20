# Generated by Django 3.0 on 2020-09-20 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfil', '0002_perfil_usuario_id'),
        ('publicacion', '0006_auto_20200919_1517'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoritos', to='publicacion.Publicaciones', verbose_name='Publicacion')),
                ('objetoP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfil_fav', to='perfil.Perfil', verbose_name='perfilFav')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoritos', to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
            options={
                'db_table': 'Favorito',
            },
        ),
    ]
