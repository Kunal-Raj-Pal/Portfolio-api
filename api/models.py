from django.db import models

# Create your models here.


class Images(models.Model):
    image = models.ImageField(upload_to='images')



class Contact(models.Model):
    name = models.CharField (max_length=50, blank=False)
    email = models.EmailField(blank=False)
    phone = models.IntegerField()
    message = models.TextField(blank=False)

    def __str__(self):
        return self.name
