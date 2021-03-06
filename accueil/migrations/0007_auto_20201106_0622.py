# Generated by Django 3.1.3 on 2020-11-06 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0006_auto_20201105_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='regions',
            name='administrative_competence',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regions',
            name='global_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regions',
            name='information_access',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regions',
            name='numeric_access',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regions',
            name='numeric_competence',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='departements',
            name='administrative_competence',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='departements',
            name='global_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='departements',
            name='information_access',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='departements',
            name='numeric_access',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='departements',
            name='numeric_competence',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
