from django.db import models

class Desktop(models.Model):
 

    ram = models.PositiveIntegerField() 
    cpu = models.CharField(max_length=50)
    gpu = models.CharField(max_length=50)
    operating_system = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.cpu} - {self.gpu} - {self.ram}GB RAM - {self.operating_system}"
