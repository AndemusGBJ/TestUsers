# Generated by Django 3.2.8 on 2021-10-23 22:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Epreuve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50, verbose_name='Nom')),
                ('description', models.TextField()),
                ('ponderation', models.FloatField(verbose_name='Maxima')),
                ('dateCreation', models.DateTimeField(verbose_name='Créée le')),
                ('duree', models.DurationField(default=datetime.timedelta(seconds=7200), verbose_name='Durée')),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('login', models.CharField(blank=True, max_length=50, null=True)),
                ('pwd', models.CharField(blank=True, default='123456789', max_length=50, null=True)),
                ('email', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Questionaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=250)),
                ('contenu', models.TextField()),
                ('ponderation', models.FloatField()),
                ('corrige', models.TextField()),
                ('idEpreuve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.epreuve', verbose_name='Epreuve')),
            ],
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('pointsObtenus', models.FloatField(null=True, verbose_name='Cotes')),
                ('idQuestion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quizzes.questionaire', verbose_name='Question')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ValidationEpreuve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validation', models.BooleanField(verbose_name='Valider')),
                ('cote', models.FloatField()),
                ('duree', models.DurationField(default=datetime.timedelta(seconds=7200))),
                ('dateEpreuve', models.DateField(auto_now_add=True)),
                ('debut', models.TimeField()),
                ('fin', models.TimeField(auto_now_add=True)),
                ('epreuve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.epreuve')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('epreuve', 'user')},
            },
        ),
    ]
