from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.db.models import Q
from .models import *
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from .forms import *
from django.contrib import messages
# Import csv
import csv
# Import Pagination
from django.core.paginator import Paginator
# Import generate PDF
from django.http import HttpResponse
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from io import BytesIO
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from django.utils.html import format_html

def start(request):
    return render(request, 'startpage/index.html')

def home(request):
    explant_list = Explantat.objects.all().order_by('-id')
    chart_data = get_analytics_data()

    # Pagination
    p = Paginator(explant_list, 10)
    page = request.GET.get('page')
    explants = p.get_page(page)
    nums = 'a' * explants.paginator.num_pages

    context = {
        'explant_list': explant_list,
        'explants': explants,
        'nums': nums,
    }
    context.update(chart_data)

    return render(request, 'data/dashboard.html', context)

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
            explant = explantat_form.save(commit=False)
            explant.owner = request.user.id # logged in User
            explant.save()
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
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_ids[]')
        for selected_id in selected_ids:
            explant = Explantat.objects.get(pk=selected_id)
            if request.user.id == explant.owner:
                explant.delete()
                messages.success(request, 'Explant deleted!')
            else:
                messages.warning(request, f'You are not authorized to delete Explant ID(s): {selected_id}')

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
    selected_ids = [int(id) for id in request.GET.getlist('selected_ids', [])]
    
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
def create_info_table(data, title):
    # Tabelle für Informationen erstellen
    table = Table(data, colWidths=[225, 250])

    # Stil für die Tabelle definieren
    style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-0.5, 0), 6),
            ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])

    table.setStyle(style)

    # Überschrift für Informationen erstellen
    title_style = getSampleStyleSheet()['Heading1']
    title_style.spaceBefore = 10
    title_style.fontSize = 14
    title = Paragraph(f"<b>{title}</b>", title_style)

    return title, table

def explant_pdf(request):
    buffer = BytesIO()

    # Informationen für jeden Datensatz erstellen
    data = []

    # get selected ids from request
    selected_ids = [int(id) for id in request.GET.getlist('selected_ids', [])]
    # get explants with selected ids and related fields
    explants = Explantat.objects.select_related('lagerort','patient', 'inlay', 'kopf', 'schaft', 'pfanne', 'reoperation', 'femurkomponente', 'tibiaplateau', 'patellaersatz').filter(pk__in=selected_ids)

    for explant in explants:
        # Allgemeine Informationen
        general_info = [
            ["ID", str(explant.id)],
            ["Ursache", explant.ursache],
            ["Verfügbarkeit", "Ja" if explant.verfuegbarkeit else "Nein"],
            ["Herkunftsort", explant.herkunftsort],
            ["Entnahmedatum", explant.entnahme_datum.strftime('%Y-%m-%d') if explant.entnahme_datum else ""],
            ["Eingangsdatum", explant.eingang_datum.strftime('%Y-%m-%d')],
            ["Bruchgeschehen", explant.bruchgeschehen],
            ["Nutzungsdauer", str(explant.nutzungsdauer) + " Jahre" if explant.nutzungsdauer else ""],
            ["Reinigung", "Ja" if explant.reinigung else "Nein"],
        ]

         # Bild in das PDF einfügen, wenn vorhanden
        if explant.bild:
            image = Image(explant.bild.path)
            image.drawHeight = min(4 * cm, image.drawHeight) # Bildhöhe anpassen
            image.drawWidth = min(6 * cm, image.drawWidth)  # Bildbreite anpassen
            general_info.append(["Bild", image])
        else:
            general_info.append(["Bild", ""])

        general_title, general_table = create_info_table(general_info, "Allgemeines")
        data.append(general_title)
        data.append(general_table)

        # Lagerortinformationen
        lagerort_info = [
            ["Schrank", explant.lagerort.schrank] if explant.lagerort else ["", ""],
            ["Kiste", explant.lagerort.kiste] if explant.lagerort else ["", ""],
        ]

        lagerort_title, lagerort_table = create_info_table(lagerort_info, "Lagerort")
        data.append(lagerort_title)
        data.append(lagerort_table)

        # Patienteninformationen
        patient_info = [
            ["Geburtsdatum", explant.patient.geburtsdatum] if explant.patient else ["", ""],
            ["Gewicht", explant.patient.gewicht] if explant.patient else ["", ""],
        ]
        

        # Tabelle und Überschrift für Patienteninformationen hinzufügen
        patient_title, patient_table = create_info_table(patient_info, "Patient")
        data.append(patient_title)
        data.append(patient_table)

        # Inlay-Informationen
        inlay_info = [
            ["Hersteller", explant.inlay.hersteller] if explant.inlay else ["", ""],
            ["Modell", explant.inlay.modell] if explant.inlay else ["", ""],
            ["Material", explant.inlay.material] if explant.inlay else ["", ""],
            ["Größe", explant.inlay.groeße] if explant.inlay else ["", ""],
        ]

        inlay_title, inlay_table = create_info_table(inlay_info, "Inlay")
        data.append(inlay_title)
        data.append(inlay_table)

        # Kopf-Informationen
        kopf_info = [
            ["Hersteller", explant.kopf.hersteller] if explant.kopf else ["", ""],
            ["Modell", explant.kopf.modell] if explant.kopf else ["", ""],
            ["Material", explant.kopf.material] if explant.kopf else ["", ""],
            ["Größe", explant.kopf.groeße] if explant.kopf else ["", ""],
        ]

        kopf_title, kopf_table = create_info_table(kopf_info, "Kopf")
        data.append(kopf_title)
        data.append(kopf_table)

        # Schaft-Informationen
        schaft_info = [
            ["Hersteller", explant.schaft.hersteller] if explant.schaft else ["", ""],
            ["Modell", explant.schaft.modell] if explant.schaft else ["", ""],
            ["Material", explant.schaft.material] if explant.schaft else ["", ""],
            ["Größe", explant.schaft.groeße] if explant.schaft else ["", ""],
        ]

        schaft_title, schaft_table = create_info_table(schaft_info, "Schaft")
        data.append(schaft_title)
        data.append(schaft_table)

        # Pfanne-Informationen
        pfanne_info = [
            ["Hersteller", explant.pfanne.hersteller] if explant.pfanne else ["", ""],
            ["Modell", explant.pfanne.modell] if explant.pfanne else ["", ""],
            ["Material", explant.pfanne.material] if explant.pfanne else ["", ""],
            ["Größe", explant.pfanne.groeße] if explant.pfanne else ["", ""],
        ]

        pfanne_title, pfanne_table = create_info_table(pfanne_info, "Pfanne")
        data.append(pfanne_title)
        data.append(pfanne_table)

        # Reoperation-Informationen
        reoperation_info = [
            ["Reoperation", explant.reoperation.reoperation] if explant.reoperation else ["", ""],
            ["Reoperationsdatum", explant.reoperation.reoperation_datum.strftime('%Y-%m-%d')] if explant.reoperation else ["", ""],
        ]

        reoperation_title, reoperation_table = create_info_table(reoperation_info, "Reoperation")
        data.append(reoperation_title)
        data.append(reoperation_table)

        # Femurkomponente-Informationen
        femurkomponente_info = [
            ["Hersteller", explant.femurkomponente.hersteller] if explant.femurkomponente else ["", ""],
            ["Modell", explant.femurkomponente.modell] if explant.femurkomponente else ["", ""],
            ["Material", explant.femurkomponente.material] if explant.femurkomponente else ["", ""],
            ["Größe", explant.femurkomponente.groeße] if explant.femurkomponente else ["", ""],
        ]

        femurkomponente_title, femurkomponente_table = create_info_table(femurkomponente_info, "Femurkomponente")
        data.append(femurkomponente_title)
        data.append(femurkomponente_table)

        # Tibiaplateau-Informationen
        tibiaplateau_info = [
            ["Hersteller", explant.tibiaplateau.hersteller] if explant.tibiaplateau else ["", ""],
            ["Modell", explant.tibiaplateau.modell] if explant.tibiaplateau else ["", ""],
            ["Material", explant.tibiaplateau.material] if explant.tibiaplateau else ["", ""],
            ["Größe", explant.tibiaplateau.groeße] if explant.tibiaplateau else ["", ""],
        ]

        tibiaplateau_title, tibiaplateau_table = create_info_table(tibiaplateau_info, "Tibiaplateau")
        data.append(tibiaplateau_title)
        data.append(tibiaplateau_table)

        # Patellaersatz-Informationen
        patellaersatz_info = [
            ["Hersteller", explant.patellaersatz.hersteller] if explant.patellaersatz else ["", ""],
            ["Modell", explant.patellaersatz.modell] if explant.patellaersatz else ["", ""],
            ["Material", explant.patellaersatz.material] if explant.patellaersatz else ["", ""],
            ["Größe", explant.patellaersatz.groeße] if explant.patellaersatz else ["", ""],
        ]

        patellaersatz_title, patellaersatz_table = create_info_table(patellaersatz_info, "Patellaersatz")
        data.append(patellaersatz_title)
        data.append(patellaersatz_table)

    # Dokument erstellen
    doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=0.5 * cm, bottomMargin=2.0 * cm, leftMargin=2.5 * cm, rightMargin=2.0 * cm)
    
    # Hinzufügen der Tabellen zum Dokument
    doc.build(data)

    buffer.seek(0)
    
    # Response für das PDF-Dokument erstellen
    response = HttpResponse(buffer.read(), content_type="application/pdf")
    response["Content-Disposition"] = "inline; filename=explant_report.pdf"

    return response

# --------------------------- chart  ---------------------------
def get_analytics_data():
    explantate_count = Explantat.objects.count()
    reoperationen_count = Reoperation.objects.count()
    inlays_count = Inlay.objects.count()
    köpfe_count = Kopf.objects.count()
    patellaersätze_count = Patellaersatz.objects.count()
    schafte_count = Schaft.objects.count()
    pfannen_count = Pfanne.objects.count()
    tibiaplateau_count = Tibiaplateau.objects.count()
    femurkomponenten_count = Femurkomponente.objects.count()

    return {
        'explantate_count': explantate_count,
        'reoperationen_count': reoperationen_count,
        'inlays_count': inlays_count,
        'köpfe_count': köpfe_count,
        'patellaersätze_count': patellaersätze_count,
        'schafte_count': schafte_count,
        'pfannen_count': pfannen_count,
        'tibiaplateau_count': tibiaplateau_count,
        'femurkomponenten_count': femurkomponenten_count,
    }

def all_analytics(request):
    data = get_analytics_data()
    return render(request, 'data/explant_analytic.html', data)

# --------------------------- Users  ---------------------------
def users(request):
    return render(request, 'data/users.html')