from django.db import models
from django.conf import settings

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_read = models.DateField(null=True, blank=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='books',
        null=True,
        blank=True
    )

def __str__(self):
    return f'{self.title} by {self.author}'