# Generated by Django 3.0 on 2020-09-24 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagenes_Publicaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='publicaciones')),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=False, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=False, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('publicacion_id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=150)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField()),
                ('ambientes', models.IntegerField()),
                ('habitaciones', models.IntegerField()),
                ('baños', models.IntegerField()),
                ('cochera', models.BooleanField(default=False)),
                ('patio', models.BooleanField(default=False)),
                ('mascotas', models.BooleanField(default=False)),
                ('niños', models.BooleanField(default=False)),
                ('superficie', models.CharField(max_length=50)),
                ('servicios', models.ManyToManyField(related_name='miServicios', to='publicacion.Servicios')),
                ('tipo_inmueble', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tipoInmueble', to='publicacion.Tipo_Inmueble')),
                ('ubicacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='zonaInmueble', to='publicacion.Zona')),
            ],
        ),
    ]
