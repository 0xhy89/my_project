from django.db import models

# Create your models here.


class Pizza(models.Model):
    """pizza模型"""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Topping(models.Model):
    """topping模型"""

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.name
