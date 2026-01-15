from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contas/', views.contas, name='contas'),
    path('contas/nova_conta', views.nova_conta, name='nova_conta'),
    path('contas/<int:conta_id>/', views.conta, name='conta'),
]