from django.db import models
from users.models import User


# Create your models here.
class Cow(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    cow_name = models.CharField(max_length=100, verbose_name='cow_name')
    breed = models.CharField(max_length=100, verbose_name='breed')

    def __str__(self):
        return f"{self.cow_name} breed {self.breed}"


class Milk(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE, null=False)
    liters = models.DecimalField(decimal_places=2, max_digits=8)
    date = models.DateField(auto_now=True,)
    time = models.TimeField(auto_now=True,)

    def __str__(self):
        return f"{self.cow} produces {self.liters} on {self.date} at {self.time}"
