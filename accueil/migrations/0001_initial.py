# Generated by Django 3.1.3 on 2020-11-04 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Communes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libcom', models.CharField(max_length=50)),
                ('information_access', models.IntegerField()),
                ('numeric_access', models.IntegerField()),
                ('numeric_competence', models.IntegerField()),
                ('administrative_competence', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Departements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libdep', models.CharField(max_length=50)),
                ('libcom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.communes')),
            ],
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libreg', models.CharField(max_length=50)),
                ('libdep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accueil.departements')),
            ],
        ),
    ]
