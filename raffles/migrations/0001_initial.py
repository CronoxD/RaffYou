# Generated by Django 3.0.2 on 2020-02-02 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('image', models.ImageField(blank=True, upload_to='images/artists')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArtistTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('code', models.CharField(max_length=30, unique=True, verbose_name='Código')),
                ('value', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.CharField(blank=True, max_length=250, verbose_name='Descripción')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Raffle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('name', models.CharField(max_length=250, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, upload_to='images/raffles')),
                ('event_date', models.DateTimeField(verbose_name='Fecha del evento')),
                ('event_address', models.CharField(max_length=250, verbose_name='Lugar del evento')),
                ('price', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Precio')),
                ('artists', models.ManyToManyField(to='raffles.Artist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='artist',
            name='tags',
            field=models.ManyToManyField(to='raffles.ArtistTag'),
        ),
    ]