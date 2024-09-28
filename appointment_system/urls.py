from django.urls import path
from .views import service_list, book_appointment

urlpatterns = [
    path('', service_list, name='service_list'),
    path('book/<int:service_id>/', book_appointment, name='book_appointment'),
]
