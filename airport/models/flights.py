from django.db import models
from django.core.exceptions import ValidationError

from airport.const import STATUSChoice


class Flight(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    # arrival = models.ForeignKey('airport.City', on_delete=models.CASCADE, related_name='arrival', verbose_name= 'Город прилета' )
    flight_number = models.CharField(max_length=100, verbose_name='Номер рейса')
    aircraft_type = models.CharField(max_length=50, verbose_name='Тип самолета')
    time = models.DateTimeField(max_length=50, verbose_name='Время')
    actual_time = models.DateTimeField(max_length=50, verbose_name='Фактическое время')
    status = models.CharField(max_length=50, choices=STATUSChoice.choice(), verbose_name='Статус')

    class Meta:
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'
        ordering = ('id', )

    def __str__(self):
        return str(self.flight_number)

    # def clean(self):
    #     if self.city == self.city:
    #         raise ValidationError('departures and arrival count not be same value')
    #
    # def save(self, *args, **kwargs):
    #     if self.city == self.city:
    #         raise ValidationError('departures and arrival count not be same value')
    #     return super().save(*args, **kwargs)
