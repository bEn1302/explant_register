from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# from semantic_admin import SemanticModelAdmin

class InlayDetailsInline(admin.TabularInline):
    model = InlayDetails
    extra = 0

class KopfDetailsInline(admin.TabularInline):
    model = KopfDetails
    extra = 0

class SchaftDetailsInline(admin.TabularInline):
    model = SchaftDetails
    extra = 0

class PfanneDetailsInline(admin.TabularInline):
    model = PfanneDetails
    extra = 0

class FemurkomponenteDetailsInline(admin.TabularInline):
    model = FemurkomponenteDetails
    extra = 0

class TibiaplateauDetailsInline(admin.TabularInline):
    model = TibiaplateauDetails
    extra = 0

class PatellaersatzDetailsInline(admin.TabularInline):
    model = PatellaersatzDetails
    extra = 0

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
    list_display = ('id', 'geburtsdatum', 'gewicht', 'groeße', 'geschlecht', 'aktivitaet', 'begleiterkrankungen', 'nachuntersuchungen', 'med_vorgeschichte', 'roentgenbilder')
    ordering = ('id',)
    search_fields = ('id', 'geburtsdatum', 'gewicht', 'groeße', 'geschlecht', 'aktivitaet', 'begleiterkrankungen', 'nachuntersuchungen', 'med_vorgeschichte')
    list_filter = ('geburtsdatum', 'gewicht', 'geschlecht')


# ------------------- Komponenten ----------------------- #

# Inlay
@admin.register(Inlay)
class InlayAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [InlayDetailsInline]
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')

@admin.register(InlayDetails)
class InlayDetailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'explantat', 'inlay', 'recycelt')
    ordering = ('id',)
    search_fields = ('id', 'explantat', 'recycelt')
    list_filter = ('explantat', 'recycelt')

# Kopf
@admin.register(Kopf)
class KopfAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [KopfDetailsInline]
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')

@admin.register(KopfDetails)
class KopfDetailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'explantat', 'kopf', 'recycelt')
    ordering = ('id',)
    search_fields = ('id', 'explantat', 'recycelt')
    list_filter = ('explantat', 'recycelt')

# Pfanne
@admin.register(Pfanne)
class PfanneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [PfanneDetailsInline]
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')

@admin.register(PfanneDetails)
class PfanneDetailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'explantat', 'pfanne', 'recycelt')
    ordering = ('id',)
    search_fields = ('id', 'explantat', 'recycelt')
    list_filter = ('explantat', 'recycelt')

# Schaft
@admin.register(Schaft)
class SchaftAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [SchaftDetailsInline]
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')

@admin.register(SchaftDetails)
class SchaftDetailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'explantat', 'schaft', 'recycelt')
    ordering = ('id',)
    search_fields = ('id', 'explantat', 'recycelt')
    list_filter = ('explantat', 'recycelt')

# Tibiaplateau
@admin.register(Tibiaplateau)
class TibiaplateauAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [TibiaplateauDetailsInline]
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')

@admin.register(TibiaplateauDetails)
class TibiaplateauDetailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'explantat', 'tibiaplateau', 'recycelt')
    ordering = ('id',)
    search_fields = ('id', 'explantat', 'recycelt')
    list_filter = ('explantat', 'recycelt')

# Femurkomponente
@admin.register(Femurkomponente)
class FemurkomponenteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [FemurkomponenteDetailsInline]
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')

@admin.register(FemurkomponenteDetails)
class FemurkomponenteDetailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'explantat', 'femurkomponente', 'recycelt')
    ordering = ('id',)
    search_fields = ('id', 'explantat', 'recycelt')
    list_filter = ('explantat', 'recycelt')    

# Patellaersatz
@admin.register(Patellaersatz)
class PatellaersatzAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [PatellaersatzDetailsInline]
    list_display = ('id', 'hersteller', 'modell', 'material', 'groeße')
    ordering = ('id',)
    search_fields = ('id', 'hersteller', 'modell', 'material', 'groeße')
    list_filter = ('hersteller', 'modell', 'material', 'groeße')

@admin.register(PatellaersatzDetails)
class PatellaersatzDetailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'explantat', 'patellaersatz', 'recycelt')
    ordering = ('id',)
    search_fields = ('id', 'explantat', 'recycelt')
    list_filter = ('explantat', 'recycelt')    
