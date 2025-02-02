from django.db import models

class Console(models.Model):
    HANDHELD = "Handheld"
    HOME_CONSOLE = "Home Console"
    HYBRID = "Hybrid"

    CONSOLE_TYPES = [
        (HANDHELD, "Handheld"),
        (HOME_CONSOLE, "Home Console"),
        (HYBRID, "Hybrid"),
    ]

    NTSC = "NTSC"
    PAL = "PAL"
    REGION_FREE = "Region-Free"

    REGION_CHOICES = [
        (NTSC, "NTSC"),
        (PAL, "PAL"),
        (REGION_FREE, "Region-Free"),
    ]

    console_type = models.CharField(max_length=20, choices=CONSOLE_TYPES)
    brand = models.CharField(max_length=50)  
    year = models.PositiveIntegerField() 
    console_model = models.CharField(max_length=50) 
    release_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    region = models.CharField(max_length=15, choices=REGION_CHOICES)

    def __str__(self):
        return f"{self.console_model} ({self.brand}, {self.year})"
