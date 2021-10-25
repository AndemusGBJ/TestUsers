# Generated by Django 3.2.8 on 2021-10-25 14:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_alter_epreuve_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='epreuve',
            name='dateCreation',
        ),
        migrations.AddField(
            model_name='epreuve',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date'),
            preserve_default=False,
        ),
    ]
