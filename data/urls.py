from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('analytics', views.all_analytics, name="analytic-explants"),
    path('explants', views.explants_table_view, name="table-explants"),
]
