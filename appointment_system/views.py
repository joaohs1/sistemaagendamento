from django.shortcuts import render, redirect
from .models import Service, Appointment
from django.utils import timezone


def service_list(request):
    services = Service.objects.all()
    return render(request, 'appointment_system/service_list.html', {'services': services})

def book_appointment(request, service_id):
    service = Service.objects.get(id=service_id)
    
    if request.method == 'POST':
        client_name = request.POST['client_name']
        client_email = request.POST['client_email']
        appointment_date = request.POST['appointment_date']
        
        Appointment.objects.create(
            service=service,
            date=appointment_date,
            client_name=client_name,
            client_email=client_email
        )
        return redirect('service_list')  # Redireciona após o agendamento
    
    return render(request, 'appointment_system/book_appointment.html', {'service': service})
