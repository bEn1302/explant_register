from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

admin.site.register(UserProfile, ImportExportModelAdmin)

class ExplantatAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'ursache', 'verfuegbarkeit', 'herkunftsort', 'entnahme_datum', 'eingang_datum', 'bruchgeschehen', 'nutzungsdauer', 'reinigung')
    ordering = ('id',)
    search_fields = ('id', 'ursache', 'verfuegbarkeit', 'herkunftsort', 'entnahme_datum', 'eingang_datum','bruchgeschehen', 'nutzungsdauer', 'reinigung')
    list_filter = ('verfuegbarkeit', 'herkunftsort', 'entnahme_datum', 'eingang_datum', 'reinigung')
admin.site.register(Explantat, ExplantatAdmin)


class LagerortAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'schrank', 'kiste')
    ordering = ('id',)
    search_fields = ('id', 'schrank', 'kiste')
admin.site.register(Lagerort, LagerortAdmin)

class ReoperationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'reoperation', 'reoperation_datum')
    ordering = ('id',)
    search_fields = ('id', 'reoperation', 'reoperation_datum')
    list_filter = ('reoperation', 'reoperation_datum')
admin.site.register(Reoperation, ReoperationAdmin)

class PatientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'geburtsdatum', 'gewicht')
    ordering = ('id',)
    search_fields = ('id', 'geburtsdatum', 'gewicht')
    list_filter = ('geburtsdatum', 'gewicht')
admin.site.register(Patient, PatientAdmin)

class InlayAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')
admin.site.register(Inlay, InlayAdmin)

class KopfAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')
admin.site.register(Kopf, KopfAdmin)

class PfanneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')
admin.site.register(Pfanne, PfanneAdmin)

class SchaftAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')
admin.site.register(Schaft, SchaftAdmin)

class TibiaplateauAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')
admin.site.register(Tibiaplateau, TibiaplateauAdmin)

class FemurkomponenteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')
admin.site.register(Femurkomponente, FemurkomponenteAdmin)

class PatellaersatzAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')
admin.site.register(Patellaersatz, PatellaersatzAdmin)