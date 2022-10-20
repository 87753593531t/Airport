from django.db import models


from airport.const import STATUSChoice

class Flight(models.Model):
    departures = models.ForeignKey('airport.Departure_city', on_delete=models.CASCADE, verbose_name='Город вылета')
    arrival = models.ForeignKey('airport.Arrival_city', on_delete=models.CASCADE, verbose_name='Город прилета')
    flight_number = models.CharField(max_length=100, verbose_name='Номер рейса')
    aircraft_type = models.CharField(max_length=50, verbose_name='Тип самолета')
    time = models.TimeField(max_length=50, verbose_name='Время')
    actual_time = models.TimeField(max_length=50, verbose_name='Фактическое время')
    status = models.CharField(max_length=50,choices=STATUSChoice.choice(), verbose_name='Статус')


    class Meta:
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'
        ordering = ('id', )