from django.db import models


from airport.const import CityChoice

class Departure_city(models.Model):
    departure_city = models.CharField(max_length=255, choices=CityChoice.choice(), verbose_name='Город вылета')
    # city = models.CharField(max_length=100, choices=CityChoice.choice(), default=CityChoice.Almaty.value, verbose_name='Город')

    class Meta:
        verbose_name = 'Departure_city'
        verbose_name_plural = 'Departure_citys'
        ordering = ('id', )


    def __str__(self):
        return str(self.departure_city)