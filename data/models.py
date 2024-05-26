from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name=_("Benutzer"))
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name=_("Telefonnummer"))
    address = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("Adresse"))
    state = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("Bundesland"))
    zip_code = models.CharField(max_length=10, null=True, blank=True, verbose_name=_("Postleitzahl"))
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("Stadt"))
    profile_picture = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name=_("Profilbild"))

    class Meta:
        verbose_name_plural = _("Benutzerprofile")

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
    hersteller = models.CharField(verbose_name=_("Hersteller"))
    modell = models.CharField(verbose_name=_("Modell"))
    material = models.CharField(verbose_name=_("Material"))
    groeße = models.FloatField(verbose_name=_("Größe"))         # in cm / mm
    recycelt = models.BooleanField(verbose_name=_("recycelt"), blank=True, null=True)

    class Meta:
        verbose_name_plural = _("Femurkomponenten")
    
    def __str__(self):
        return f"{self.hersteller} - {self.modell} - {self.material} - {self.groeße}"

class Tibiaplateau(models.Model):
    hersteller = models.CharField(verbose_name=_("Hersteller"))
    modell = models.CharField(verbose_name=_("Modell"))
    material = models.CharField(verbose_name=_("Material"))
    groeße = models.FloatField(verbose_name=_("Größe"))         # in cm / mm
    recycelt = models.BooleanField(verbose_name=_("recycelt"), blank=True, null=True)

    class Meta:
        verbose_name_plural = _("Tibiaplateaus")

    def __str__(self):
        return f"{self.hersteller} - {self.modell} - {self.material} - {self.groeße}"

class Patellaersatz(models.Model):
    hersteller = models.CharField(verbose_name=_("Hersteller"))
    modell = models.CharField(verbose_name=_("Modell"))
    material = models.CharField(verbose_name=_("Material"))
    groeße = models.FloatField(verbose_name=_("Größe"))         # in cm / mm
    recycelt = models.BooleanField(verbose_name=_("recycelt"), blank=True, null=True)

    class Meta:
        verbose_name_plural = "Patellaersätze"

    def __str__(self):
        return f"{self.hersteller} - {self.modell} - {self.material} - {self.groeße}"

class Kopf(models.Model):
    hersteller = models.CharField(verbose_name=_("Hersteller"))
    modell = models.CharField(verbose_name=_("Modell"))
    material = models.CharField(verbose_name=_("Material"))
    groeße = models.FloatField(verbose_name=_("Größe"))         # in cm / mm
    recycelt = models.BooleanField(verbose_name=_("recycelt"), blank=True, null=True)

    class Meta:
        verbose_name_plural = _("Köpfe")

    def __str__(self):
        return f"{self.hersteller} - {self.modell} - {self.material} - {self.groeße}"

class Inlay(models.Model):
    hersteller = models.CharField(verbose_name=_("Hersteller"))
    modell = models.CharField(verbose_name=_("Modell"))
    material = models.CharField(verbose_name=_("Material"))
    groeße = models.FloatField(verbose_name=_("Größe"))         # in cm / mm
    recycelt = models.BooleanField(verbose_name=_("recycelt"), blank=True, null=True)

    class Meta:
        verbose_name_plural = _("Inlays")

    def __str__(self):
        return f"{self.hersteller} - {self.modell} - {self.material} - {self.groeße}"

class Schaft(models.Model):
    hersteller = models.CharField(verbose_name=_("Hersteller"))
    modell = models.CharField(verbose_name=_("Modell"))
    material = models.CharField(verbose_name=_("Material"))
    groeße = models.FloatField(verbose_name=_("Größe"))         # in cm / mm
    recycelt = models.BooleanField(verbose_name=_("recycelt"), blank=True, null=True)

    class Meta:
        verbose_name_plural = _("Schafte")

    def __str__(self):
        return f"{self.hersteller} - {self.modell} - {self.material} - {self.groeße}"

class Pfanne(models.Model):
    hersteller = models.CharField(verbose_name=_("Hersteller"))
    modell = models.CharField(verbose_name=_("Modell"))
    material = models.CharField(verbose_name=_("Material"))
    groeße = models.FloatField(verbose_name=_("Größe"))         # in cm / mm
    recycelt = models.BooleanField(verbose_name=_("recycelt"), blank=True, null=True)

    class Meta:
        verbose_name_plural = _("Pfannen")

    def __str__(self):
        return f"{self.hersteller} - {self.modell} - {self.material} - {self.groeße}"

class Reoperation(models.Model):
    reoperation = models.BooleanField(verbose_name=_('Reoperation'))
    reoperation_datum = models.DateField(verbose_name=_('Reoperationsdatum'))

    class Meta:
        verbose_name_plural = _("Reoperationen")
    
    def __str__(self):
        return self.reoperation_datum.strftime('%Y-%m-%d')
    
# --- Reopertion ändern zu Operation ---
# class Operation(models.Model):
#     reoperation = models.BooleanField('Reoperation')
#     reoperation_datum = models.DateField('Reoperationsdatum')
#     implantatposition = models.ImageField('Implantatposition', blank=True, null=True, upload_to='images/')
#     operierender_arzt = models.CharField('operierender Arzt')
#     klinik = models.CharField('Klinik')
#     operationsdauer = models.IntegerField('Operationsdauer')        # in h
#     nebenwirkungen = models.TextField('Nebenwirkungen')
#     postoperative_komplikationen = models.TextField('postoperative Komplikationen')

#     class Meta:
#         verbose_name_plural = "Operationen"

class Patient(models.Model):
    geburtsdatum = models.DateField(verbose_name=_('Geburtsdatum'))
    gewicht = models.FloatField(verbose_name=_('Gewicht'))          # in kg
    # groesse = models.FloatField(verbose_name=_('Größe'))            # in m
    # geschlecht = models.CharField(verbose_name=_('Geschlecht'))     # männlich, weiblich, divers
    # aktivitaet = models.TextField(verbose_name=_('Aktivität'))      # viel/wenig Bewegung --> was etc.
    # begleiterkrankungen = models.TextField(verbose_name=_('Begleiterkrankungen'))
    # nachuntersuchungen = models.TextField(verbose_name=_('Nachuntersuchungen'))
    # med_vorgeschichte = models.TextField(verbose_name=_('Medizinische Vorgeschichte'))
    # roentgenbilder = models.ImageField(verbose_name=_('Röntgenbilder'), blank=True, null=True, upload_to='images/')

    class Meta:
        verbose_name_plural = _("Patienten")

    def __str__(self):
        return f"{self.geburtsdatum} - {self.gewicht}"

class Lagerort(models.Model):
    schrank = models.IntegerField(verbose_name=_('Schrank'))
    kiste = models.IntegerField(verbose_name=_('Kiste'))
    # einrichtung = models.CharField(verbose_name=_('Einrichtung'))

    class Meta:
        verbose_name_plural = _("Lagerorte")

    def __str__(self):
        return f" Schrank: {self.schrank} - Kiste: {self.kiste}"

class Explantat(models.Model):
    ursache = models.TextField(verbose_name=_('Ursache'))
    verfuegbarkeit = models.BooleanField(verbose_name=_('Verfügbarkeit'))
    herkunftsort = models.CharField(verbose_name=_('Herkunftsort'))
    entnahme_datum = models.DateField(verbose_name=_('Entnahmedatum'), blank=True, null=True)
    eingang_datum = models.DateField(verbose_name=_('Eingangsdatum'))
    bruchgeschehen = models.TextField(verbose_name=_('Bruchgeschehen'))
    nutzungsdauer = models.IntegerField(verbose_name=_('Nutzungsdauer'), blank=True, null=True)        # in Jahre
    reinigung = models.BooleanField(verbose_name=_('Reinigung'))
    bild = models.ImageField(verbose_name=_('Bild'), blank=True, null=True, upload_to='images/')
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
    owner = models.IntegerField(verbose_name=_('Besitzer'), blank=False, default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = _("Explantate")