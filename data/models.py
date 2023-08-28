from django.db import models

class Femurkomponente(models.Model):
    hersteller = models.CharField('Hersteller', blank=True)
    modell = models.CharField('Modell', blank=True)
    material = models.CharField('Material', blank=True)
    groeße = models.FloatField('Größe', blank=True)         # in cm / mm

    class Meta:
        verbose_name_plural = "Femurkomponenten"

class Tibiaplateau(models.Model):
    hersteller = models.CharField('Hersteller', blank=True)
    modell = models.CharField('Modell', blank=True)
    material = models.CharField('Material', blank=True)
    groeße = models.FloatField('Größe', blank=True)         # in cm / mm

class Patellaersatz(models.Model):
    hersteller = models.CharField('Hersteller', blank=True)
    modell = models.CharField('Modell', blank=True)
    material = models.CharField('Material', blank=True)
    groeße = models.FloatField('Größe', blank=True)         # in cm / mm

    class Meta:
        verbose_name_plural = "Patellaersätze"

class Kopf(models.Model):
    hersteller = models.CharField('Hersteller', blank=True)
    modell = models.CharField('Modell', blank=True)
    material = models.CharField('Material', blank=True)
    groeße = models.FloatField('Größe', blank=True)         # in cm / mm

    class Meta:
        verbose_name_plural = "Köpfe"

class Inlay(models.Model):
    hersteller = models.CharField('Hersteller', blank=True)
    modell = models.CharField('Modell', blank=True)
    material = models.CharField('Material', blank=True)
    groeße = models.FloatField('Größe', blank=True)         # in cm / mm

class Schaft(models.Model):
    hersteller = models.CharField('Hersteller', blank=True)
    modell = models.CharField('Modell', blank=True)
    material = models.CharField('Material', blank=True)
    groeße = models.FloatField('Größe', blank=True)         # in cm / mm

    class Meta:
        verbose_name_plural = "Schafte"

class Pfanne(models.Model):
    hersteller = models.CharField('Hersteller', blank=True)
    modell = models.CharField('Modell', blank=True)
    material = models.CharField('Material', blank=True)
    groeße = models.FloatField('Größe', blank=True)         # in cm / mm

    class Meta:
        verbose_name_plural = "Pfannen"

class Reoperation(models.Model):
    reoperation = models.BooleanField('Reoperation', blank=True)
    reoperation_datum = models.DateField('Reoperationsdatum', blank=True)

    class Meta:
        verbose_name_plural = "Reperationen"

class Patient(models.Model):
    geburtsdatum = models.DateField('Geburtsdatum', blank=True)
    gewicht = models.FloatField('Gewicht', blank=True)          # in kg

    class Meta:
        verbose_name_plural = "Patienten"

class Lagerort(models.Model):
    schrank = models.IntegerField('Schrank', blank=True)
    kiste = models.IntegerField('Kiste', blank=True)

    class Meta:
        verbose_name_plural = "Lagerorte"

class Explantat(models.Model):
    ursache = models.TextField('Ursache', blank=True)
    verfuegbarkeit = models.BooleanField('Verfügbarkeit', blank=True)
    herkunftsort = models.CharField('Herkunftsort', blank=True)
    entnahme_datum = models.DateField('Entnahmedatum', blank=True)
    eingang_datum = models.DateField('Eingangsdatum', blank=True)
    bruchgeschehen = models.TextField('Bruchgeschehen', blank=True)
    nutzungsdauer = models.IntegerField('Nutzungsdauer', blank=True)        # in Jahre
    reinigung = models.BooleanField('Reinigung', blank=True)
    bild = models.FileField('Bild', blank=True, null=True)
    lagerort = models.ForeignKey(Lagerort, blank=True, null=True, on_delete=models.CASCADE)         
    patient = models.ForeignKey(Patient, blank=True, null=True, on_delete=models.CASCADE)           
    reoperation = models.ManyToManyField(Reoperation, blank=True)   # 1:n
    inlay = models.ForeignKey(Inlay, on_delete=models.CASCADE)
    
    # Hüftexplantate
    kopf = models.ForeignKey(Kopf, blank=True, on_delete=models.CASCADE)
    schaft = models.ForeignKey(Schaft, blank=True, on_delete=models.CASCADE)
    pfanne = models.ForeignKey(Pfanne, blank=True, on_delete=models.CASCADE)

    # Knieexplantate
    femurkomponente = models.ForeignKey(Femurkomponente, blank=True, on_delete=models.CASCADE)
    tibiaplateau = models.ForeignKey(Tibiaplateau, blank=True, on_delete=models.CASCADE)
    patellaersatz = models.ForeignKey(Patellaersatz, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Explantate"