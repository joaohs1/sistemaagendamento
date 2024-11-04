from django.urls import path
from .views import service_list, appointment_request, about, contact

urlpatterns = [
    path('', about, name='about'),  # Mapeando a página "Sobre" como a homepage do app
    path('services/', service_list, name='service_list'),  # URL para lista de serviços
    path('request/<int:service_id>/', appointment_request, name='appointment_request'),  # Para agendamento
    path('contact/', contact, name='contact'),  # URL para a página de contato
]
