from django.urls import path

from . import views

urlpatterns = [
    path('registration/', views.UserCreation.as_view(), name='registration'),
    path('login/', views.CustomLogin.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/<slug:user_slug>', views.dash, name='dashboard'),
    path('dashboard/<slug:user_slug>/keys/<slug:pk_slug>', views.show_pk, name='pk_delete'),
    path('dashboard/<slug:user_slug>/balance', views.show_balance, name='balance'),
]