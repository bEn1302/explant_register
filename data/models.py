from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

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
    entnahme_datum = models.DateField('Entnahmedatum', blank=True, null=True)
    eingang_datum = models.DateField('Eingangsdatum')
    bruchgeschehen = models.TextField('Bruchgeschehen')
    nutzungsdauer = models.IntegerField('Nutzungsdauer', blank=True, null=True)        # in Jahre
    reinigung = models.BooleanField('Reinigung')
    bild = models.ImageField('Bild', blank=True, null=True, upload_to='images/')
    lagerort = models.ForeignKey(Lagerort, blank=True, null=True, on_delete=models.CASCADE)         
    patient = models.ForeignKey(Patient, blank=True, null=True, on_delete=models.CASCADE)           
    reoperation = models.ForeignKey(Reoperation, blank=True, null=True, on_delete=models.CASCADE)
    inlay = models.ForeignKey(Inlay, blank=True, null=True, on_delete=models.PROTECT)
    # Hüftexplantate
    kopf = models.ForeignKey(Kopf, blank=True, null=True, on_delete=models.PROTECT)
    schaft = models.ForeignKey(Schaft, blank=True, null=True, on_delete=models.PROTECT)
    pfanne = models.ForeignKey(Pfanne, blank=True, null=True, on_delete=models.PROTECT)
    # Knieexplantate
    femurkomponente = models.ForeignKey(Femurkomponente, blank=True, null=True, on_delete=models.PROTECT)
    tibiaplateau = models.ForeignKey(Tibiaplateau, blank=True, null=True, on_delete=models.PROTECT)
    patellaersatz = models.ForeignKey(Patellaersatz, blank=True, null=True, on_delete=models.PROTECT)
    # owner
    owner = models.IntegerField('Owner', blank=False, default=1)

    class Meta:
        verbose_name_plural = "Explantate"