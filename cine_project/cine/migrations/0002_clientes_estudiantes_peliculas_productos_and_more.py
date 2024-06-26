# Generated by Django 4.2.11 on 2024-04-19 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'clientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('puntuacion', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'estudiantes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id_pelicula', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'peliculas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('categoria', models.CharField(blank=True, max_length=50, null=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'productos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reservaciones',
            fields=[
                ('id_reservacion', models.AutoField(primary_key=True, serialize=False)),
                ('id_cliente', models.IntegerField(blank=True, null=True)),
                ('id_pelicula', models.IntegerField(blank=True, null=True)),
                ('fecha_reservacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'reservaciones',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='reservacion',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='reservacion',
            name='pelicula',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Pelicula',
        ),
        migrations.DeleteModel(
            name='Reservacion',
        ),
    ]
