from django.db import models


# Create your models here.
class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery')
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(default=1)
    name = models.CharField(max_length=50)


class Events(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to='events')
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(default=1)


class Contacts(models.Model):
    address = models.CharField(max_length=60)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    working_hours = models.CharField(max_length=30)
    sunday_working_hours = models.CharField(max_length=30)

class MenuCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    position = models.PositiveSmallIntegerField(default=1)
    is_visible = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class MenuDish(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True, db_index=True)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    ingredients = models.TextField()
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='dishes', blank=True)
    position = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.name
