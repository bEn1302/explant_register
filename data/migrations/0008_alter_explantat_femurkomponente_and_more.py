# Generated by Django 4.2.7 on 2023-11-30 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_alter_femurkomponente_groeße_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='explantat',
            name='femurkomponente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='data.femurkomponente'),
        ),
        migrations.AlterField(
            model_name='explantat',
            name='inlay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data.inlay'),
        ),
        migrations.AlterField(
            model_name='explantat',
            name='kopf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='data.kopf'),
        ),
        migrations.AlterField(
            model_name='explantat',
            name='patellaersatz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='data.patellaersatz'),
        ),
        migrations.AlterField(
            model_name='explantat',
            name='pfanne',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='data.pfanne'),
        ),
        migrations.AlterField(
            model_name='explantat',
            name='schaft',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='data.schaft'),
        ),
        migrations.AlterField(
            model_name='explantat',
            name='tibiaplateau',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='data.tibiaplateau'),
        ),
    ]
