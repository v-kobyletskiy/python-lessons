from django.db import models


# Create your models here.
class Chef(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    appointment = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, blank=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='chefs_photos', blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'
