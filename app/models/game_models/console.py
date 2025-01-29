from django.db import models

class Console(models.Model):
    console_type = models.CharField(max_length=30)
    brand=models.CharField(max_length=20)
    year=models.CharField(max_length=20)
    console_model=models.CharField(max_length=30)
    release_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    region=models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.console_model} ({self.brand})"