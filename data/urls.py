from django.contrib import admin
from django.contrib.auth import views as auth_views
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
    path('users', views.users, name="users"),
    path('account', views.account, name="account"),
    
    # update views
    path('update_explant/<int:explant_id>', views.explant_update, name='explant_update'),
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
    path('update-profile/', update_profile, name='update_profile'),
    path('password/', CustomPasswordChangeView.as_view(), name='password'),

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

    # generate pdf
    path('explant_pdf/', explant_pdf, name='explant_pdf'),

    # generate csv
    path('explant_csv/', explant_csv, name='explant_csv'),

]
