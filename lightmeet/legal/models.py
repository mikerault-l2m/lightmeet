from datetime import datetime
from django.db import models

class legal_Controler(models.Model):
    M_Legal = models.TextField(max_length=500,default=" ")

    def __str__(self):
        return self.M_Legal

    class Meta:
        verbose_name = "Notre document juridique"
        verbose_name_plural = "Nos documents juridiques"

