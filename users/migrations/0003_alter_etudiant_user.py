# Generated by Django 3.2.8 on 2021-10-14 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_etudiant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
