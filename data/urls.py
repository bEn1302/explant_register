from django.contrib import admin
from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.start, name="start"),
    path('impressum', views.disclaimer, name="disclaimer"),
    path('dashboard', views.home, name="dashboard"),
    path('analytics', views.all_analytics, name="analytic-explants"),
    path('explants', views.explants_table_view, name="table-explants"),
    path('forms', views.add_explant, name="add-explants"),
    path('search', views.search, name="search"),
    
    # update views
    path('lagerort/<int:pk>/update/', views.lagerort_update, name='lagerort_update'),
    path('patient/<int:pk>/update/', views.patient_update, name='patient_update'),
    path('reoperation/<int:pk>/update/', views.reoperation_update, name='reoperation_update'),
    path('inlay/<int:pk>/update/', views.inlay_update, name='inlay_update'),
    path('kopf/<int:pk>/update/', views.kopf_update, name='kopf_update'),
    path('femurkomponente/<int:pk>/update/', views.femurkomponente_update, name='femurkomponente_update'),
    path('schaft/<int:pk>/update/', views.schaft_update, name='schaft_update'),
    path('tibiaplateau/<int:pk>/update/', views.tibiaplateau_update, name='tibiaplateau_update'),
    path('pfanne/<int:pk>/update/', views.pfanne_update, name='pfanne_update'),
    path('patellaersatz/<int:pk>/update/', views.patellaersatz_update, name='patellaersatz_update'),

    # Data insert views
    path('add_lagerort/', add_lagerort, name='add_lagerort'),
    path('add_patient/', add_patient, name='add_patient'),
    path('add_reoperation/', add_reoperation, name='add_reoperation'),
    path('add_inlay/', add_inlay, name='add_inlay'),
    path('add_schaft/', add_schaft, name='add_schaft'),
    path('add_kopf/', add_kopf, name='add_kopf'),
    path('add_pfanne/', add_pfanne, name='add_pfanne'),
    path('add_femurkomponente/', add_femurkomponente, name='add_femurkomponente'),
    path('add_tibiaplateau/', add_tibiaplateau, name='add_tibiaplateau'),
    path('add_patellaersatz/', add_patellaersatz, name='add_patellaersatz'),

    # delete Explants
    path('delete_selected_explants/', delete_selected_explants, name='delete_selected_explants'),
]
