# Generated by Django 3.2.8 on 2021-10-23 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_delete_etudiant'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Etudiant', 'verbose_name_plural': 'Etudiants'},
        ),
    ]