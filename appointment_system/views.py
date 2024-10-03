from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, Appointment
from django.utils import timezone

def service_list(request):
    services = Service.objects.all()  # Recuperar todos os serviços
    return render(request, 'appointment_system/service_list.html', {'services': services})


def appointment_request(request, service_id):
    service = get_object_or_404(Service, id=service_id)  # Obter o serviço específico
    available_times = []  # Inicializar a lista de horários disponíveis

    if request.method == 'POST':
        # Processar o formulário de agendamento
        client_name = request.POST['name']
        client_email = request.POST['email']
        appointment_date = request.POST['date']
        appointment_time = request.POST['time']  # Captura a hora selecionada

        # Criar o agendamento
        Appointment.objects.create(
            service=service,
            date=appointment_date,
            time=appointment_time,  # Adiciona o horário ao agendamento
            client_name=client_name,
            client_email=client_email
        )
        return redirect('service_list')  # Redireciona após o agendamento

    # Lógica para verificar horários disponíveis
    appointment_date = request.GET.get('date')  # Obter a data da solicitação
    if appointment_date:
        appointments = Appointment.objects.filter(date=appointment_date, service=service)
        # Definir um intervalo de horários
        start_hour = 9  # Exemplo: 9:00 AM
        end_hour = 17  # Exemplo: 5:00 PM

        for hour in range(start_hour, end_hour + 1):
            time_str = f"{hour:02}:00"
            # Adiciona o horário à lista se não houver agendamentos
            if time_str not in [appt.time.strftime("%H:%M") for appt in appointments]:
                available_times.append(time_str)

    return render(request, 'appointment_system/appointment_request.html', {'service': service, 'available_times': available_times})


def book_appointment(request, service_id):
    # Esta função pode ser removida se o agendamento for tratado diretamente em appointment_request
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'appointment_system/book_appointment.html', {'service': service})
