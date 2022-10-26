from django.db import models


class City(models.Model):
    departures = models.CharField(max_length=150, verbose_name='Город вылета')
    arrival = models.CharField(max_length=150, verbose_name='Город прилета')


    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Citys'
        ordering = ('id', )

    def __str__(self):
        return '%s, %s' % (self.departures, self.arrival)