from django.db import models

class Personas(models.Model):
    personas = models.CharField(max_length=150)
    def __str__(self):
        return self.personas