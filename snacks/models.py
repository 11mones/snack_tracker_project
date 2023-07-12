from django.db import models
from django.contrib.auth import get_user_model

class Snack(models.Model):
    name = models.CharField(max_length=64,help_text="Name of snack")
    Autpurchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    desc = models.TextField(default="no descriprion available")


    def __str__(self):
        return self.name

# Create your models here.
