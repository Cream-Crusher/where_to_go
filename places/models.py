from django.db import models


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = models.TextField('Полное описание', blank=True)
    image = models.ImageField('Картинка', blank=True)

    def __str__(self):

        return self.title


class PlaceEntity(models.Model):
    place = models.ForeignKey(Place, related_name='entities', null=True, on_delete=models.CASCADE, verbose_name='Место')
    lat = models.FloatField('Широта')
    low = models.FloatField('Долгота')

    def __str__(self):

        return str(self.place)
