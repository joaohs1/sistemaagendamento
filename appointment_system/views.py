from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, Appointment
from datetime import datetime, timedelta, date


def service_list(request):
    services = Service.objects.all()  # Recuperar todos os serviços
    return render(request, 'appointment_system/service_list.html', {'services': services})

# Função para obter dias disponíveis
def get_available_days():
    today = date.today()
    available_days = []
    
    # Verificar os próximos 30 dias para disponibilidade
    for i in range(30):
        day = today + timedelta(days=i)
        # Verificar se é um dia de semana (segunda a sexta)
        if day.weekday() < 5:
            # Verificar se há horários disponíveis neste dia (limitar a 9 agendamentos por dia)
            if Appointment.objects.filter(date=day).count() < 9:
                available_days.append(day.strftime("%Y-%m-%d"))  # Retornar a data em formato string

    return available_days

def appointment_request(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    
    if request.method == 'POST':
        client_name = request.POST['name']
        client_email = request.POST['email']
        appointment_date = request.POST['date']
        appointment_time = request.POST['time']

        Appointment.objects.create(
            service=service,
            date=appointment_date,
            time=appointment_time,
            client_name=client_name,
            client_email=client_email
        )
        return redirect('service_list')

    available_days = get_available_days()

    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        appointment_date = request.GET.get('date')
        available_times = []

        if appointment_date:
            appointments = Appointment.objects.filter(date=appointment_date, service=service)

            start_hour = 8
            end_hour = 17
            service_duration = service.duration

            current_time = datetime.strptime(f"{start_hour}:00", "%H:%M")
            end_time = datetime.strptime(f"{end_hour}:00", "%H:%M")

            while current_time + timedelta(minutes=service_duration) <= end_time:
                time_str = current_time.strftime("%H:%M")
                conflicting_appointments = appointments.filter(time=time_str)

                if not conflicting_appointments.exists():
                    available_times.append(time_str)

                current_time += timedelta(minutes=service_duration)

        return JsonResponse({'available_times': available_times})

    return render(request, 'appointment_system/appointment_request.html', {
        'service': service,
        'available_days': available_days,
    })


def book_appointment(request, service_id):
    # Esta função pode ser removida se o agendamento for tratado diretamente em appointment_request
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'appointment_system/book_appointment.html', {'service': service})
