from django.db import models

class Femurkomponente(models.Model):
    hersteller = models.CharField('Hersteller')
    modell = models.CharField('Modell')
    material = models.CharField('Material')
    groeße = models.FloatField('Größe')         # in cm / mm

class Tibiaplateau(models.Model):
    hersteller = models.CharField('Hersteller')
    modell = models.CharField('Modell')
    material = models.CharField('Material')
    groeße = models.FloatField('Größe')         # in cm / mm

class Patellaersatz(models.Model):
    hersteller = models.CharField('Hersteller')
    modell = models.CharField('Modell')
    material = models.CharField('Material')
    groeße = models.FloatField('Größe')         # in cm / mm

class Kopf(models.Model):
    hersteller = models.CharField('Hersteller')
    modell = models.CharField('Modell')
    material = models.CharField('Material')
    groeße = models.FloatField('Größe')         # in cm / mm

class Inlay(models.Model):
    hersteller = models.CharField('Hersteller')
    modell = models.CharField('Modell')
    material = models.CharField('Material')
    groeße = models.FloatField('Größe')         # in cm / mm

class Schaft(models.Model):
    hersteller = models.CharField('Hersteller')
    modell = models.CharField('Modell')
    material = models.CharField('Material')
    groeße = models.FloatField('Größe')         # in cm / mm

class Pfanne(models.Model):
    hersteller = models.CharField('Hersteller')
    modell = models.CharField('Modell')
    material = models.CharField('Material')
    groeße = models.FloatField('Größe')         # in cm / mm

class Reoperation(models.Model):
    reoperation = models.BooleanField('Reoperation')
    reoperation_datum = models.DateTimeField('Reoperationsdatum')

class Patient(models.Model):
    geburtsdatum = models.DateField('Geburtsdatum')
    gewicht = models.FloatField('Gewicht')          # in kg

class Lagerort(models.Model):
    schrank = models.IntegerField('Schrank')
    kiste = models.IntegerField('Kiste')

class Explantat(models.Model):
    ursache = models.TextField('Ursache')
    verfuegbarkeit = models.BooleanField('Verfügbarkeit')
    herkunftsort = models.CharField('Herkunftsort')
    entnahme_datum = models.DateTimeField('Entnahmedatum')
    eingang_datum = models.DateTimeField('Eingangsdatum')
    bruchgeschehen = models.TextField('Bruchgeschehen')
    nutzungsdauer = models.IntegerField('Nutzungsdauer')        # in Jahre
    reinigung = models.BooleanField('Reinigung')
    bild = models.FileField('Bild', blank=True, null=True)
    lagerort = models.ForeignKey(Lagerort, blank=True, null=True, on_delete=models.CASCADE)         
    patient = models.ForeignKey(Patient, blank=True, null=True, on_delete=models.CASCADE)           
    reoperation = models.ManyToManyField(Reoperation, blank=True, null=True)   # 1:n
    inlay = models.ForeignKey(Inlay, on_delete=models.CASCADE)
    
    # Hüftexplantate
    kopf = models.ForeignKey(Kopf, blank=True, null=True, on_delete=models.CASCADE)
    schaft = models.ForeignKey(Schaft, blank=True, null=True, on_delete=models.CASCADE)
    pfanne = models.ForeignKey(Pfanne, blank=True, null=True, on_delete=models.CASCADE)

    # Knieexplantate
    femurkomponente = models.ForeignKey(Femurkomponente, blank=True, null=True, on_delete=models.CASCADE)
    tibiaplateau = models.ForeignKey(Tibiaplateau, blank=True, null=True, on_delete=models.CASCADE)
    patellaersatz = models.ForeignKey(Patellaersatz, blank=True, null=True, on_delete=models.CASCADE)