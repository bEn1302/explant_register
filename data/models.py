from django.db import models

class Femurkomponente(models.Model):
    hersteller = models.CharField('Hersteller')
    modell = models.CharField('Modell')
    material = models.CharField('Material')
    groeße = models.FloatField('Größe')         # in cm / mm

    class Meta:
        verbose_name_plural = "Femurkomponenten"
    
    def __str__(self):
        return f"{self.hersteller} - {self.modell}"

class Tibiaplateau(models.Model):
    hersteller = models.CharField('Hersteller')
    modell = models.CharField('Modell')
    material = models.CharField('Material')
    groeße = models.FloatField('Größe')         # in cm / mm

    def __str__(self):
        return f"{self.hersteller} - {self.modell}"

class Patellaersatz(models.Model):
    hersteller = models.CharField('Hersteller')
    modell = models.CharField('Modell')
    material = models.CharField('Material')
    groeße = models.FloatField('Größe')         # in cm / mm

    class Meta:
        verbose_name_plural = "Patellaersätze"

    def __str__(self):
        return f"{self.hersteller} - {self.modell}"

class Kopf(models.Model):
    hersteller = models.CharField('Hersteller')
    modell = models.CharField('Modell')
    material = models.CharField('Material')
    groeße = models.FloatField('Größe')         # in cm / mm

    class Meta:
        verbose_name_plural = "Köpfe"

    def __str__(self):
        return f"{self.hersteller} - {self.modell}"

class Inlay(models.Model):
    hersteller = models.CharField('Hersteller')
    modell = models.CharField('Modell')
    material = models.CharField('Material')
    groeße = models.FloatField('Größe')         # in cm / mm

    def __str__(self):
        return f"{self.hersteller} - {self.modell}"

class Schaft(models.Model):
    hersteller = models.CharField('Hersteller')
    modell = models.CharField('Modell')
    material = models.CharField('Material')
    groeße = models.FloatField('Größe')         # in cm / mm

    class Meta:
        verbose_name_plural = "Schafte"

    def __str__(self):
        return f"{self.hersteller} - {self.modell}"

class Pfanne(models.Model):
    hersteller = models.CharField('Hersteller')
    modell = models.CharField('Modell')
    material = models.CharField('Material')
    groeße = models.FloatField('Größe')         # in cm / mm

    class Meta:
        verbose_name_plural = "Pfannen"

    def __str__(self):
        return f"{self.hersteller} - {self.modell}"

class Reoperation(models.Model):
    reoperation = models.BooleanField('Reoperation')
    reoperation_datum = models.DateField('Reoperationsdatum')

    class Meta:
        verbose_name_plural = "Reperationen"
    
    def __str__(self):
        return self.reoperation_datum.strftime('%Y-%m-%d')

class Patient(models.Model):
    geburtsdatum = models.DateField('Geburtsdatum')
    gewicht = models.FloatField('Gewicht')          # in kg

    class Meta:
        verbose_name_plural = "Patienten"

class Lagerort(models.Model):
    schrank = models.IntegerField('Schrank')
    kiste = models.IntegerField('Kiste')

    class Meta:
        verbose_name_plural = "Lagerorte"

    def __str__(self):
        return f"{self.schrank} - {self.kiste}"

class Explantat(models.Model):
    ursache = models.TextField('Ursache')
    verfuegbarkeit = models.BooleanField('Verfügbarkeit')
    herkunftsort = models.CharField('Herkunftsort')
    entnahme_datum = models.DateField('Entnahmedatum')
    eingang_datum = models.DateField('Eingangsdatum')
    bruchgeschehen = models.TextField('Bruchgeschehen')
    nutzungsdauer = models.IntegerField('Nutzungsdauer')        # in Jahre
    reinigung = models.BooleanField('Reinigung')
    bild = models.FileField('Bild', blank=True, null=True)
    lagerort = models.ForeignKey(Lagerort, blank=True, null=True, on_delete=models.CASCADE)         
    patient = models.ForeignKey(Patient, blank=True, null=True, on_delete=models.CASCADE)           
    reoperation = models.ForeignKey(Reoperation, blank=True, null=True, on_delete=models.CASCADE)
    inlay = models.ForeignKey(Inlay, on_delete=models.CASCADE)
    # Hüftexplantate
    kopf = models.ForeignKey(Kopf, blank=True, null=True, on_delete=models.CASCADE)
    schaft = models.ForeignKey(Schaft, blank=True, null=True, on_delete=models.CASCADE)
    pfanne = models.ForeignKey(Pfanne, blank=True, null=True, on_delete=models.CASCADE)
    # Knieexplantate
    femurkomponente = models.ForeignKey(Femurkomponente, blank=True, null=True, on_delete=models.CASCADE)
    tibiaplateau = models.ForeignKey(Tibiaplateau, blank=True, null=True, on_delete=models.CASCADE)
    patellaersatz = models.ForeignKey(Patellaersatz, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Explantate"