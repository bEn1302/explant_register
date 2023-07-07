# Generated by Django 4.2.1 on 2023-07-07 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Femurkomponente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hersteller', models.CharField(verbose_name='Hersteller')),
                ('modell', models.CharField(verbose_name='Modell')),
                ('material', models.CharField(verbose_name='Material')),
                ('groeße', models.FloatField(verbose_name='Größe')),
            ],
        ),
        migrations.CreateModel(
            name='Inlay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hersteller', models.CharField(verbose_name='Hersteller')),
                ('modell', models.CharField(verbose_name='Modell')),
                ('material', models.CharField(verbose_name='Material')),
                ('groeße', models.FloatField(verbose_name='Größe')),
            ],
        ),
        migrations.CreateModel(
            name='Kopf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hersteller', models.CharField(verbose_name='Hersteller')),
                ('modell', models.CharField(verbose_name='Modell')),
                ('material', models.CharField(verbose_name='Material')),
                ('groeße', models.FloatField(verbose_name='Größe')),
            ],
        ),
        migrations.CreateModel(
            name='Lagerort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schrank', models.IntegerField(verbose_name='Schrank')),
                ('kiste', models.IntegerField(verbose_name='Kiste')),
            ],
        ),
        migrations.CreateModel(
            name='Patellaersatz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hersteller', models.CharField(verbose_name='Hersteller')),
                ('modell', models.CharField(verbose_name='Modell')),
                ('material', models.CharField(verbose_name='Material')),
                ('groeße', models.FloatField(verbose_name='Größe')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geburtsdatum', models.DateField(verbose_name='Geburtsdatum')),
                ('gewicht', models.FloatField(verbose_name='Gewicht')),
            ],
        ),
        migrations.CreateModel(
            name='Pfanne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hersteller', models.CharField(verbose_name='Hersteller')),
                ('modell', models.CharField(verbose_name='Modell')),
                ('material', models.CharField(verbose_name='Material')),
                ('groeße', models.FloatField(verbose_name='Größe')),
            ],
        ),
        migrations.CreateModel(
            name='Reoperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reoperation', models.BooleanField(verbose_name='Reoperation')),
                ('reoperation_datum', models.DateTimeField(verbose_name='Reoperationsdatum')),
            ],
        ),
        migrations.CreateModel(
            name='Schaft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hersteller', models.CharField(verbose_name='Hersteller')),
                ('modell', models.CharField(verbose_name='Modell')),
                ('material', models.CharField(verbose_name='Material')),
                ('groeße', models.FloatField(verbose_name='Größe')),
            ],
        ),
        migrations.CreateModel(
            name='Tibiaplateau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hersteller', models.CharField(verbose_name='Hersteller')),
                ('modell', models.CharField(verbose_name='Modell')),
                ('material', models.CharField(verbose_name='Material')),
                ('groeße', models.FloatField(verbose_name='Größe')),
            ],
        ),
        migrations.CreateModel(
            name='Explantat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ursache', models.TextField(verbose_name='Ursache')),
                ('verfuegbarkeit', models.BooleanField(verbose_name='Verfügbarkeit')),
                ('herkunftsort', models.CharField(verbose_name='Herkunftsort')),
                ('entnahme_datum', models.DateTimeField(verbose_name='Entnahmedatum')),
                ('eingang_datum', models.DateTimeField(verbose_name='Eingangsdatum')),
                ('bruchgeschehen', models.TextField(verbose_name='Bruchgeschehen')),
                ('nutzungsdauer', models.IntegerField(verbose_name='Nutzungsdauer')),
                ('reinigung', models.BooleanField(verbose_name='Reinigung')),
                ('bild', models.FileField(blank=True, null=True, upload_to='', verbose_name='Bild')),
                ('femurkomponente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.femurkomponente')),
                ('inlay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.inlay')),
                ('kopf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.kopf')),
                ('lagerort', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.lagerort')),
                ('patellaersatz', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.patellaersatz')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.patient')),
                ('pfanne', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.pfanne')),
                ('reoperation', models.ManyToManyField(blank=True, null=True, to='data.reoperation')),
                ('schaft', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.schaft')),
                ('tibiaplateau', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.tibiaplateau')),
            ],
        ),
    ]