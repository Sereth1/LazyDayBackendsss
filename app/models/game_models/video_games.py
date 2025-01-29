from django.db import models
from .console import Console 
from .desktop import Desktop
class VideoGame(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    console = models.ForeignKey(Console, on_delete=models.CASCADE, related_name="games")
    desktop=models.ForeignKey(Desktop,on_delete=models.CASCADE, related_name="desktop")
    game_format=models.CharField(max_length=50)
    
    
    def __str__(self):
        return f"{self.name} - {self.console.console_model}"
