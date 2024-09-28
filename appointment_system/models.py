from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField()
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()

    def __str__(self):
        return f'Appointment for {self.client_name} on {self.date}'

