from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# from semantic_admin import SemanticModelAdmin

admin.site.register(UserProfile, ImportExportModelAdmin)

@admin.register(Explantat)
class ExplantatAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'ursache', 'verfuegbarkeit', 'herkunftsort', 'entnahme_datum', 'eingang_datum', 'bruchgeschehen', 'nutzungsdauer', 'reinigung')
    ordering = ('id',)
    search_fields = ('id', 'ursache', 'verfuegbarkeit', 'herkunftsort', 'entnahme_datum', 'eingang_datum','bruchgeschehen', 'nutzungsdauer', 'reinigung')
    list_filter = ('verfuegbarkeit', 'herkunftsort', 'entnahme_datum', 'eingang_datum', 'reinigung')

@admin.register(Lagerort)
class LagerortAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'schrank', 'kiste')
    ordering = ('id',)
    search_fields = ('id', 'schrank', 'kiste')

@admin.register(Reoperation)
class ReoperationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'reoperation', 'reoperation_datum')
    ordering = ('id',)
    search_fields = ('id', 'reoperation', 'reoperation_datum')
    list_filter = ('reoperation', 'reoperation_datum')

@admin.register(Patient)
class PatientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'geburtsdatum', 'gewicht')
    ordering = ('id',)
    search_fields = ('id', 'geburtsdatum', 'gewicht')
    list_filter = ('geburtsdatum', 'gewicht')

@admin.register(Inlay)
class InlayAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')

@admin.register(Kopf)
class KopfAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')

@admin.register(Pfanne)
class PfanneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')

@admin.register(Schaft)
class SchaftAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')

@admin.register(Tibiaplateau)
class TibiaplateauAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')

@admin.register(Femurkomponente)
class FemurkomponenteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')

@admin.register(Patellaersatz)
class PatellaersatzAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')