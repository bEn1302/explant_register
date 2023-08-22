from django.contrib import admin
from .models import *


@admin.register(Explantat)
class ExplantatAdmin(admin.ModelAdmin):
    list_display = ('id', 'ursache', 'verfuegbarkeit', 'herkunftsort', 'entnahme_datum', 'eingang_datum', 'bruchgeschehen', 'nutzungsdauer', 'reinigung')
    ordering = ('id',)
    search_fields = ('id', 'ursache', 'verfuegbarkeit', 'herkunftsort', 'entnahme_datum', 'eingang_datum','bruchgeschehen', 'nutzungsdauer', 'reinigung')
    list_filter = ('verfuegbarkeit', 'herkunftsort', 'entnahme_datum', 'eingang_datum', 'reinigung')

@admin.register(Lagerort)
class LagerortAdmin(admin.ModelAdmin):
    list_display = ('id', 'schrank', 'kiste')
    ordering = ('id',)
    search_fields = ('id', 'schrank', 'kiste')

@admin.register(Reoperation)
class ReoperationAdmin(admin.ModelAdmin):
    list_display = ('id', 'reoperation', 'reoperation_datum')
    ordering = ('id',)
    search_fields = ('id', 'reoperation', 'reoperation_datum')
    list_filter = ('reoperation', 'reoperation_datum')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'geburtsdatum', 'gewicht')
    ordering = ('id',)
    search_fields = ('id', 'geburtsdatum', 'gewicht')
    list_filter = ('geburtsdatum', 'gewicht')

@admin.register(Inlay)
class InlayAdmin(admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')

@admin.register(Kopf)
class KopfAdmin(admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')

@admin.register(Pfanne)
class PfanneAdmin(admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')

@admin.register(Schaft)
class SchaftAdmin(admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')

@admin.register(Tibiaplateau)
class TibiaplateauAdmin(admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')

@admin.register(Femurkomponente)
class FemurkomponenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')

@admin.register(Patellaersatz)
class PatellaersatzAdmin(admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')