from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = HTMLField('Полное описание', blank=True)
    lon = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):

        return f'{self.title} Id места: {self.id}'


class Image(models.Model):
    img = models.ImageField('Картинка', upload_to='media', unique=True)

    post = models.ForeignKey(
        'Place',
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name='Картинка, к месту')

    custom_order = models.IntegerField(
        default=0,
    )

    class Meta:
        ordering = ['custom_order']

    def __str__(self):
        return str(self.img)
