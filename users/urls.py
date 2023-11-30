from django.urls import path
from . import views

urlpatterns = [
    path('sign_in/', views.login_user, name='sign_in'),
    path('sign_out/', views.logout_user, name='sign_out'),
    path('sign_up/', views.register_user, name='sign_up'),
]