# Generated by Django 5.0.1 on 2024-03-22 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_alter_explantat_bild'),
    ]

    operations = [
        migrations.AddField(
            model_name='explantat',
            name='owner',
            field=models.IntegerField(default=1, verbose_name='Owner'),
        ),
    ]