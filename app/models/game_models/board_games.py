from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class BoardGames(models.Model):
    name = models.CharField(max_length=100)
    type_of_board = models.CharField(max_length=50)
    max_players = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    min_players = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2100)])
    brand = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    short_description = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.year})"

   
    class Meta:
        verbose_name = "Board Game"
        verbose_name_plural = "Board Games"
