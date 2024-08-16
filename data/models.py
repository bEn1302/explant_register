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

class KomponentenDetails(models.Model):
    hersteller = models.CharField(max_length=100, verbose_name=_("Hersteller"))
    modell = models.CharField(max_length=100, verbose_name=_("Modell"))
    material = models.CharField(max_length=100, verbose_name=_("Material"))
    groeße = models.FloatField(verbose_name=_("Größe in mm"))
    mrt_compatibility = models.BooleanField(default=False, verbose_name=_("MRT-Kompatibilität"))
    revision_friendly = models.BooleanField(default=False, verbose_name=_("Revisionstauglichkeit"))

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.hersteller} - {self.modell} - {self.material} - {self.groeße}"

class Femurkomponente(KomponentenDetails):
    fixation_type = models.CharField(max_length=50, blank=True, choices=[("zementiert", _("Zementiert")), ("unzementiert", _("Unzementiert")), ("hybrid", ("Hybrid"))], verbose_name=_("Fixationsmethode"))
    surface_coating = models.CharField(max_length=100, blank=True, choices=[("Titan", _("Titan")), ("Hydroxylapatit", _("Hydroxylapatit")), ("keine", _("Keine"))], verbose_name=_("Oberflächenbeschichtung"))
    class Meta:
        verbose_name_plural = _("Femurkomponenten")

class Tibiaplateau(KomponentenDetails):
    fixation_type = models.CharField(max_length=50, blank=True, choices=[("zementiert", _("Zementiert")), ("unzementiert", _("Unzementiert")), ("hybrid", ("Hybrid"))], verbose_name=_("Fixationsmethode"))
    surface_coating = models.CharField(max_length=100, blank=True, choices=[("Titan", _("Titan")), ("Hydroxylapatit", _("Hydroxylapatit")), ("keine", _("Keine"))], verbose_name=_("Oberflächenbeschichtung"))
    class Meta:
        verbose_name_plural = _("Tibiaplateaus")

class Patellaersatz(KomponentenDetails):
    class Meta:
        verbose_name_plural = _("Patellaersätze")

class Kopf(KomponentenDetails):
    gliding_pairing = models.CharField(max_length=100, blank=True, choices=[("metall_auf_metall", _("Metall auf Metall")), ("metall_auf_polyethylen", _("Metall auf Polyethylen")), ("keramik_auf_keramik", _("Keramik auf Keramik"))], verbose_name=_("Gleitpaarung"))
    class Meta:
        verbose_name_plural = _("Köpfe")

class Inlay(KomponentenDetails):
    gliding_pairing = models.CharField(max_length=100, blank=True, choices=[("metall_auf_metall", _("Metall auf Metall")), ("metall_auf_polyethylen", _("Metall auf Polyethylen")), ("keramik_auf_keramik", _("Keramik auf Keramik"))], verbose_name=_("Gleitpaarung"))
    class Meta:
        verbose_name_plural = _("Inlays")

class Schaft(KomponentenDetails):
    fixation_type = models.CharField(max_length=50, blank=True, choices=[("zementiert", _("Zementiert")), ("unzementiert", _("Unzementiert")), ("hybrid", ("Hybrid"))], verbose_name=_("Fixationsmethode"))
    design = models.CharField(max_length=50, blank=True, choices=[("gerader_schaft", _("Gerader Schaft")), ("anatomisch", _("Anatomischer Schaft")), ("kurzschaft", _("Kurzschaft")), ("modular", _("Modularer Schaft"))], verbose_name=("Design"))
    surface_coating = models.CharField(max_length=100, blank=True, choices=[("Titan", _("Titan")), ("Hydroxylapatit", _("Hydroxylapatit")), ("keine", _("Keine"))], verbose_name=_("Oberflächenbeschichtung"))
    class Meta:
        verbose_name_plural = _("Schafte")

class Pfanne(KomponentenDetails):
    fixation_type = models.CharField(max_length=50, blank=True, choices=[("zementiert", _("Zementiert")), ("unzementiert", _("Unzementiert")), ("hybrid", ("Hybrid"))], verbose_name=_("Fixationsmethode"))
    surface_coating = models.CharField(max_length=100, blank=True, choices=[("Titan", _("Titan")), ("Hydroxylapatit", _("Hydroxylapatit")), ("keine", _("Keine"))], verbose_name=_("Oberflächenbeschichtung"))
    gliding_pairing = models.CharField(max_length=100, blank=True, choices=[("metall_auf_metall", _("Metall auf Metall")), ("metall_auf_polyethylen", _("Metall auf Polyethylen")), ("keramik_auf_keramik", _("Keramik auf Keramik"))], verbose_name=_("Gleitpaarung"))
    class Meta:
        verbose_name_plural = _("Pfannen")

class Stent(KomponentenDetails):
    legierung = models.CharField(max_length=100, verbose_name=_("Legierung"))
    class Meta:
        verbose_name_plural = _("Stents")

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
    groeße = models.FloatField(verbose_name=_('Größe'), null=True)            # in m
    geschlecht = models.CharField(choices=[('maennlich', _('Männlich')), ('weiblich', _('Weiblich')),('divers', _('Divers'))], verbose_name=_('Geschlecht'), max_length=20, null=True)
    aktivitaet = models.TextField(verbose_name=_('Aktivität'), blank=True, null=True)      # viel/wenig Bewegung --> was etc.
    begleiterkrankungen = models.TextField(verbose_name=_('Begleiterkrankungen'), blank=True, null=True)
    nachuntersuchungen = models.TextField(verbose_name=_('Nachuntersuchungen'), blank=True, null=True)
    med_vorgeschichte = models.TextField(verbose_name=_('Med. Vorgeschichte'), blank=True, null=True)
    roentgenbilder = models.ImageField(verbose_name=_('Röntgenbilder'), blank=True, null=True, upload_to='images/')

    class Meta:
        verbose_name_plural = _("Patienten")

    def __str__(self):
        return f"{self.geburtsdatum} - {self.gewicht} - {self.geschlecht}"

class Lagerort(models.Model):
    einrichtung = models.CharField(max_length=50, verbose_name=_('Einrichtung'))
    schrank = models.IntegerField(verbose_name=_('Schrank'))
    kiste = models.IntegerField(verbose_name=_('Kiste'))

    class Meta:
        verbose_name_plural = _("Lagerorte")

    def __str__(self):
        return f" Einrichtung: {self.einrichtung} - Schrank: {self.schrank} - Kiste: {self.kiste}"

class Explantat(models.Model):
    ursache = models.TextField(verbose_name=_('Ursache'))
    verfuegbarkeit = models.BooleanField(verbose_name=_('Verfügbarkeit'))
    herkunftsort = models.CharField(verbose_name=_('Herkunftsort'), max_length=100)
    entnahme_datum = models.DateField(verbose_name=_('Entnahmedatum'), blank=True, null=True)
    eingang_datum = models.DateField(verbose_name=_('Eingangsdatum'))
    bruchgeschehen = models.TextField(verbose_name=_('Bruchgeschehen'))
    nutzungsdauer = models.IntegerField(verbose_name=_('Nutzungsdauer'), blank=True, null=True)        # in Jahre
    reinigung = models.BooleanField(verbose_name=_('Reinigung'))
    bild = models.ImageField(verbose_name=_('Bild'), blank=True, null=True, upload_to='images/')
    lagerort = models.ForeignKey(Lagerort,verbose_name=_('Lagerort') ,blank=True, null=True, on_delete=models.CASCADE)         
    patient = models.ForeignKey(Patient,verbose_name=_('Patient') , blank=True, null=True, on_delete=models.CASCADE)           
    reoperation = models.ForeignKey(Reoperation,verbose_name=_('Reoperation') , blank=True, null=True, on_delete=models.CASCADE)
    inlay = models.ForeignKey(Inlay,verbose_name=_('Inlay') ,blank=True, null=True, on_delete=models.PROTECT)
    # Hüftexplantate
    kopf = models.ForeignKey(Kopf,verbose_name=_('Kopf') ,blank=True, null=True, on_delete=models.PROTECT)
    schaft = models.ForeignKey(Schaft,verbose_name=_('Schaft') ,blank=True, null=True, on_delete=models.PROTECT)
    pfanne = models.ForeignKey(Pfanne,verbose_name=_('Pfanne') ,blank=True, null=True, on_delete=models.PROTECT)
    # Knieexplantate
    femurkomponente = models.ForeignKey(Femurkomponente,verbose_name=_('Femurkomponente') ,blank=True, null=True, on_delete=models.PROTECT)
    tibiaplateau = models.ForeignKey(Tibiaplateau,verbose_name=_('Tibiaplateau') ,blank=True, null=True, on_delete=models.PROTECT)
    patellaersatz = models.ForeignKey(Patellaersatz,verbose_name=_('Patellaersatz') ,blank=True, null=True, on_delete=models.PROTECT)
    # Stents
    stent = models.ForeignKey(Stent, verbose_name=_('Stent') ,blank=True, null=True, on_delete=models.PROTECT)
    # owner
    owner = models.IntegerField(verbose_name=_('Besitzer'), blank=False, default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = _("Explantate")

    def __str__(self):
        return f"{self.id}"    

# -------------------- Komponenten Details -------------------- #
class InlayDetails(models.Model):
    explantat = models.ForeignKey(Explantat, on_delete=models.CASCADE)
    inlay = models.ForeignKey(Inlay, on_delete=models.CASCADE)
    recycelt = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = _("Inlays Details")

# Hüfte
class KopfDetails(models.Model):
    explantat = models.ForeignKey(Explantat, on_delete=models.CASCADE)
    kopf = models.ForeignKey(Kopf, on_delete=models.CASCADE)
    recycelt = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = _("Köpfe Details")

class SchaftDetails(models.Model):
    explantat = models.ForeignKey(Explantat, on_delete=models.CASCADE)
    schaft = models.ForeignKey(Schaft, on_delete=models.CASCADE)
    recycelt = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = _("Schafte Details")

class PfanneDetails(models.Model):
    explantat = models.ForeignKey(Explantat, on_delete=models.CASCADE)
    pfanne = models.ForeignKey(Pfanne, on_delete=models.CASCADE)
    recycelt = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = _("Pfannen Details")

# Knie
class FemurkomponenteDetails(models.Model):
    explantat = models.ForeignKey(Explantat, on_delete=models.CASCADE)
    femurkomponente = models.ForeignKey(Femurkomponente, on_delete=models.CASCADE)
    recycelt = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = _("Femurkomponenten Details")

class TibiaplateauDetails(models.Model):
    explantat = models.ForeignKey(Explantat, on_delete=models.CASCADE)
    tibiaplateau = models.ForeignKey(Tibiaplateau, on_delete=models.CASCADE)
    recycelt = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = _("Tibiaplateaus Details")

class PatellaersatzDetails(models.Model):
    explantat = models.ForeignKey(Explantat, on_delete=models.CASCADE)
    patellaersatz = models.ForeignKey(Patellaersatz, on_delete=models.CASCADE)
    recycelt = models.BooleanField(verbose_name=_("recycelt"), default=False)

    class Meta:
        verbose_name_plural = _("Patellaersätze Details")

# Stent
class StentDetails(models.Model):
    explantat = models.ForeignKey(Explantat, on_delete=models.CASCADE)
    stent = models.ForeignKey(Stent, on_delete=models.CASCADE)
    recycelt = models.BooleanField(verbose_name=_("recycelt"), default=False)

    class Meta:
        verbose_name_plural = _("Stents Details")