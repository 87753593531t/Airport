from django.db import models


from airport.const import CityChoice


class Arrival_city(models.Model):
    arrival_city = models.CharField(max_length=255, choices=CityChoice.choice(), verbose_name='Город прилета')
    # city = models.CharField(max_length=100, choices=CityChoice.choice(), default=CityChoice.Almaty.value, )


    class Meta:
        verbose_name = 'Arrival_city'
        verbose_name_plural = 'Arrival_citys'
        ordering = ('id', )

    def __str__(self):
        return str(self.arrival_city)