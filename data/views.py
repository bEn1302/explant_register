from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.db.models import Q
from .models import *
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from .forms import *

# Import csv
import csv

# Import Pagination
from django.core.paginator import Paginator

# Import generate PDF
from django.http import HttpResponse
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from io import BytesIO
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def start(request):
    return render(request, 'startpage/index.html')

def home(request):
    explant_list = Explantat.objects.all().order_by('-id')

    # Pagination
    p = Paginator(explant_list, 10)
    page = request.GET.get('page')
    explants = p.get_page(page)
    nums = 'a' * explants.paginator.num_pages

    return render(request, 'data/dashboard.html', {'explant_list': explant_list, 'explants':explants, 'nums':nums})

def disclaimer(request):
    return render(request, 'startpage/impressum.html')

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        # search results
        huefte_explants = Explantat.objects.filter(ursache__icontains=searched, kopf__isnull=False, pfanne__isnull=False, schaft__isnull=False)
        knie_explants = Explantat.objects.filter(ursache__icontains=searched, tibiaplateau__isnull=False, patellaersatz__isnull=False)
        return render(request, 'data/search.html', {'searched': searched, 'huefte_explants':huefte_explants, 'knie_explants':knie_explants})
    else:
        return render(request, 'data/search.html', {})


def explants_table_view(request):
    huefte_explant_table = Explantat.objects.filter(
        Q(kopf__isnull=False) | Q(kopf__isnull=False) | Q(pfanne__isnull=False) | Q(schaft__isnull=False)
    )
    knie_explant_table = Explantat.objects.filter(
        Q(femurkomponente__isnull=False) | Q(tibiaplateau__isnull=False) | Q(patellaersatz__isnull=False)
    )

    context = {
        'huefte_explant_table': huefte_explant_table,
        'knie_explant_table': knie_explant_table,
    }

    return render(request, 'data/explant_table.html', context)


# --------------------------- Update ----------------------------
def update_model(request, model_cls, form_cls, redirect_url, pk):
    obj = get_object_or_404(model_cls, pk=pk)
    
    if request.method == 'POST':
        form = form_cls(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            response_data = {'success': True}
        else:
            response_data = {'success': False, 'errors': form.errors}
            return HttpResponseBadRequest(JsonResponse(response_data))
    else:
        form = form_cls(instance=obj)
        response_data = {'success': False}

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse(response_data)
    else:
        return redirect(redirect_url)

def lagerort_update(request, pk):
    return update_model(request, Lagerort, LagerortUpdateForm, 'table-explants', pk)

def patient_update(request, pk):
    return update_model(request, Patient, PatientUpdateForm, 'table-explants', pk)

def reoperation_update(request, pk):
    return update_model(request, Reoperation, ReoperationUpdateForm, 'table-explants', pk)

def inlay_update(request, pk):
    return update_model(request, Inlay, InlayUpdateForm, 'table-explants', pk)

def kopf_update(request, pk):
    return update_model(request, Kopf, KopfUpdateForm, 'table-explants', pk)

def femurkomponente_update(request, pk):
    return update_model(request, Femurkomponente, FemurkomponenteUpdateForm, 'table-explants', pk)

def schaft_update(request, pk):
    return update_model(request, Schaft, SchaftUpdateForm, 'table-explants', pk)

def tibiaplateau_update(request, pk):
    return update_model(request, Tibiaplateau, TibiaplateauUpdateForm, 'table-explants', pk)

def pfanne_update(request, pk):
    return update_model(request, Pfanne, PfanneUpdateForm, 'table-explants', pk)

def patellaersatz_update(request, pk):
    return update_model(request, Patellaersatz, PatellaersatzUpdateForm, 'table-explants', pk)


def all_analytics(request):
    return render(request, 'data/explant_analytic.html')

# --------------------------- Update Explants ---------------------------
def explant_update(request, explant_id):
    explant = Explantat.objects.get(pk=explant_id)
    explantat_form = ExplantatForm(request.POST or None, request.FILES or None , instance=explant)
    if explantat_form.is_valid():
        explantat_form.save()
        return redirect('table-explants')
    
    return render(request, 'data/update_explant.html', {'explant': explant, 'explantat_form':explantat_form})


# --------------------------- Data Insert ---------------------------
def add_explant(request):
    if request.method == 'POST':
        explantat_form = ExplantatForm(request.POST, request.FILES)
        if explantat_form.is_valid():
            explantat_form.save()
            return HttpResponseRedirect(f"{reverse('table-explants')}?success=True")
    
    else:
        explantat_form = ExplantatForm()

    return render(request, 'data/explant_form.html', {'explantat_form': explantat_form})

# Verknüpfte Tabellen
def add_model_instance(request, form_class):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            # Redirect back to the referring page
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=400)

def add_lagerort(request):
    return add_model_instance(request, LagerortForm)

def add_patient(request):
    return add_model_instance(request, PatientForm)

def add_reoperation(request):
    return add_model_instance(request, ReoperationForm)

def add_inlay(request):
    return add_model_instance(request, InlayForm)

def add_kopf(request):
    return add_model_instance(request, KopfForm)

def add_schaft(request):
    return add_model_instance(request, SchaftForm)

def add_pfanne(request):
    return add_model_instance(request, PfanneForm)

def add_femurkomponente(request):
    return add_model_instance(request, FemurkomponenteForm)

def add_tibiaplateau(request):
    return add_model_instance(request, TibiaplateauForm)

def add_patellaersatz(request):
    return add_model_instance(request, PatellaersatzForm)

# --------------------------- Delete Data ---------------------------
@require_POST
def delete_selected_explants(request):
    selected_ids = request.POST.getlist('selected_ids[]')
    Explantat.objects.filter(pk__in=selected_ids).delete()
    return redirect('table-explants')

# --------------------------- generate CSV ---------------------------
def explant_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=explants.csv'

    # create a csv writer
    writer = csv.writer(response)

    # add column headings
    writer.writerow(['ID', 'Ursache', 'Verfügbarkeit', 'Herkunftsort', 'Entnahmedatum', 'Eingangdatum', 'Bruchgeschehen', 'Nutzungsdauer', 'Reinigung', 'Bild', 'Lagerort', 'Patient', 'Reoperation', 'Inlay', 'Kopf', 'Schaft', 'Pfanne', 'Femurkomponente', 'Tibiaplateau', 'Patellaersatz'])

    # get selected ids from request
    selected_ids = request.POST.getlist('selected_ids[]', [])  # Änderung hier: Verwendung von request.POST anstelle von request.GET
    
    # get explants with selected ids and related fields
    explants = Explantat.objects.select_related('lagerort', 'patient', 'reoperation', 'inlay', 'kopf', 'schaft', 'pfanne', 'femurkomponente', 'tibiaplateau', 'patellaersatz').filter(pk__in=selected_ids)

    # loop through and output
    for explant in explants:
        # Format dates if needed
        entnahmedatum = explant.entnahme_datum.strftime('%Y-%m-%d') if explant.entnahme_datum else ''
        eingangdatum = explant.eingang_datum.strftime('%Y-%m-%d')
        
        # add row to CSV
        writer.writerow([
            explant.pk,
            explant.ursache,
            explant.verfuegbarkeit,
            explant.herkunftsort,
            entnahmedatum,
            eingangdatum,
            explant.bruchgeschehen,
            explant.nutzungsdauer,
            explant.reinigung,
            explant.bild,
            explant.lagerort,
            explant.patient,
            explant.reoperation,
            explant.inlay,
            explant.kopf,
            explant.schaft,
            explant.pfanne,
            explant.femurkomponente,
            explant.tibiaplateau,
            explant.patellaersatz
        ])
        
    return response

# --------------------------- generate PDF ---------------------------
def explant_pdf(request):
    buffer = BytesIO()

    # Informationen für jeden Datensatz erstellen
    data = []
    for explant in Explantat.objects.all():
        # Allgemeine Informationen
        general_info = [
            ["ID", explant.id],
            ["Ursache", explant.ursache],
            ["Verfügbarkeit", "Ja" if explant.verfuegbarkeit else "Nein"],
            ["Herkunftsort", explant.herkunftsort],
            ["Entnahmedatum", explant.entnahme_datum.strftime('%Y-%m-%d') if explant.entnahme_datum else ""],
            ["Eingangsdatum", explant.eingang_datum.strftime('%Y-%m-%d')],
            ["Bruchgeschehen", explant.bruchgeschehen],
            ["Nutzungsdauer", str(explant.nutzungsdauer) + " Jahre" if explant.nutzungsdauer else ""],
            ["Reinigung", "Ja" if explant.reinigung else "Nein"],
            ["Bild", explant.bild.url if explant.bild else ""],
        ]

        # Patienteninformationen
        patient_info = [
            ["Geburtsdatum", explant.patient.geburtsdatum] if explant.patient else ["", ""],
            ["Gewicht", explant.patient.gewicht] if explant.patient else ["", ""],
        ]

        # Inlay-Informationen
        inlay_info = [
            ["Hersteller", explant.inlay.hersteller] if explant.inlay else ["", ""],
            ["Modell", explant.inlay.modell] if explant.inlay else ["", ""],
            ["Material", explant.inlay.material] if explant.inlay else ["", ""],
            ["Größe", explant.inlay.groeße] if explant.inlay else ["", ""],
        ]

        # Kopf-Informationen
        kopf_info = [
            ["Hersteller", explant.kopf.hersteller] if explant.kopf else ["", ""],
            ["Modell", explant.kopf.modell] if explant.kopf else ["", ""],
            ["Material", explant.kopf.material] if explant.kopf else ["", ""],
            ["Größe", explant.kopf.groeße] if explant.kopf else ["", ""],
        ]

        # Schaft-Informationen
        schaft_info = [
            ["Hersteller", explant.schaft.hersteller] if explant.schaft else ["", ""],
            ["Modell", explant.schaft.modell] if explant.schaft else ["", ""],
            ["Material", explant.schaft.material] if explant.schaft else ["", ""],
            ["Größe", explant.schaft.groeße] if explant.schaft else ["", ""],
        ]

        # Pfanne-Informationen
        pfanne_info = [
            ["Hersteller", explant.pfanne.hersteller] if explant.pfanne else ["", ""],
            ["Modell", explant.pfanne.modell] if explant.pfanne else ["", ""],
            ["Material", explant.pfanne.material] if explant.pfanne else ["", ""],
            ["Größe", explant.pfanne.groeße] if explant.pfanne else ["", ""],
        ]

        # Reoperation-Informationen
        reoperation_info = [
            ["Reoperation", explant.reoperation.reoperation] if explant.reoperation else ["", ""],
            ["Reoperationsdatum", explant.reoperation.reoperation_datum.strftime('%Y-%m-%d')] if explant.reoperation else ["", ""],
        ]

        # Femurkomponente-Informationen
        femurkomponente_info = [
            ["Hersteller", explant.femurkomponente.hersteller] if explant.femurkomponente else ["", ""],
            ["Modell", explant.femurkomponente.modell] if explant.femurkomponente else ["", ""],
            ["Material", explant.femurkomponente.material] if explant.femurkomponente else ["", ""],
            ["Größe", explant.femurkomponente.groeße] if explant.femurkomponente else ["", ""],
        ]

        # Tibiaplateau-Informationen
        tibiaplateau_info = [
            ["Hersteller", explant.tibiaplateau.hersteller] if explant.tibiaplateau else ["", ""],
            ["Modell", explant.tibiaplateau.modell] if explant.tibiaplateau else ["", ""],
            ["Material", explant.tibiaplateau.material] if explant.tibiaplateau else ["", ""],
            ["Größe", explant.tibiaplateau.groeße] if explant.tibiaplateau else ["", ""],
        ]

        # Patellaersatz-Informationen
        patellaersatz_info = [
            ["Hersteller", explant.patellaersatz.hersteller] if explant.patellaersatz else ["", ""],
            ["Modell", explant.patellaersatz.modell] if explant.patellaersatz else ["", ""],
            ["Material", explant.patellaersatz.material] if explant.patellaersatz else ["", ""],
            ["Größe", explant.patellaersatz.groeße] if explant.patellaersatz else ["", ""],
        ]

        # Zusammenführen der Abschnitte
        combined_info = general_info + patient_info + inlay_info + kopf_info + schaft_info + pfanne_info + reoperation_info + femurkomponente_info + tibiaplateau_info + patellaersatz_info 

        # Tabelle für diesen Datensatz erstellen und zur Gesamttabelle hinzufügen
        table = Table(combined_info, colWidths=[100, 200])
        data.append(table)

    # Dokument erstellen
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    
    # Hinzufügen der Tabellen zum Dokument
    doc.build(data)

    # Buffer zurücksetzen
    buffer.seek(0)
    
    # Response für das PDF-Dokument erstellen
    response = HttpResponse(buffer.read(), content_type="application/pdf")
    response["Content-Disposition"] = "inline; filename=explant_report.pdf"

    return response