# Generated by Django 4.2.7 on 2023-12-05 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_alter_explantat_femurkomponente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='explantat',
            name='entnahme_datum',
            field=models.DateField(blank=True, null=True, verbose_name='Entnahmedatum'),
        ),
        migrations.AlterField(
            model_name='explantat',
            name='inlay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='data.inlay'),
        ),
        migrations.AlterField(
            model_name='explantat',
            name='nutzungsdauer',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nutzungsdauer'),
        ),
    ]
