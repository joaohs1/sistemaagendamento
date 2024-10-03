from django.urls import path
from .views import service_list, appointment_request

urlpatterns = [
    path('', service_list, name='service_list'),
    path('request/<int:service_id>/', appointment_request, name='appointment_request'),  # Para agendamento
]
