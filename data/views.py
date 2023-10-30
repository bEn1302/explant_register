from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from .forms import *

def start(request):
    return render(request, 'startpage/index.html')

def home(request):
    return render(request, 'data/dashboard.html')

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
    huefte_explant_table = Explantat.objects.filter(kopf__isnull=False, pfanne__isnull=False, schaft__isnull=False)
    knie_explant_table = Explantat.objects.filter(femurkomponente__isnull=False, tibiaplateau__isnull=False, patellaersatz__isnull=False)

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


# Data Insert
def add_explant(request):
    submitted = False
    if request.method == 'POST':
        explantat_form = ExplantatForm(request.POST, request.FILES)
        if explantat_form.is_valid():
            explantat_form.save()  # Speichert das Formular
            return HttpResponseRedirect('/forms?submitted=True')  # Weiterleitung zur Liste der Explantate
    else:
        explantat_form = ExplantatForm()
        if submitted in request.GET:
            submitted = True
    return render(request, 'data/explant_form.html', {'explantat_form': explantat_form, 'submitted': submitted})