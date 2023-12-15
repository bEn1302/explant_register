from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.db.models import Q
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
    huefte_explant_table = Explantat.objects.filter(
        Q(kopf__isnull=False) | Q(kopf__isnull=False) | Q(pfanne__isnull=False) | Q(schaft__isnull=False)
    )
    knie_explant_table = Explantat.objects.filter(
        Q(femurkomponente__isnull=False) | Q(tibiaplateau__isnull=False) | Q(patellaersatz__isnull=False)
    )
    all_explant_table = huefte_explant_table & knie_explant_table

    is_huefte = request.GET.get('is_huefte')

    context = {
        'is_huefte': is_huefte,
        'huefte_explant_table': huefte_explant_table,
        'knie_explant_table': knie_explant_table,
        'all_explant_table': all_explant_table,
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

# --------------------------- Delte Data ---------------------------
@require_POST
def delete_selected_explants(request):
    selected_ids = request.POST.getlist('selected_ids[]')
    Explantat.objects.filter(pk__in=selected_ids).delete()
    return redirect('table-explants')