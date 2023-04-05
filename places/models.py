from django.db import models


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = models.TextField('Полное описание', blank=True)
    low = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):

        return self.title


class Image(models.Model):
    img = models.ImageField('Картинка', blank=True, unique=True)

    post = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        verbose_name='Картинка, к месту')

    def __str__(self):

        return str(self.post)