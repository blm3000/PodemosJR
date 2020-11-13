# Generated by Django 3.1.3 on 2020-11-10 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('clientes', models.ManyToManyField(to='Clientes.Cliente')),
            ],
            options={
                'verbose_name': 'grupo',
                'verbose_name_plural': 'grupos',
            },
        ),
    ]
