from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} - {self.name}"

class Airline(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} - {self.name}"

class Flight(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    flight_number = models.CharField(max_length=10)
    departure_airport = models.ForeignKey(Airport, related_name='departure_flights', on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey(Airport, related_name='arrival_flights', on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return f"{self.airline} - {self.flight_number}"

