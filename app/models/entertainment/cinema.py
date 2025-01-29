from django.db import models

class Cinema(models.Model):
    name = models.CharField(max_length=255)  
    address = models.TextField() 
    house_number = models.CharField(max_length=10, null=True, blank=True) 
    road = models.CharField(max_length=100, null=True, blank=True) 
    quarter = models.CharField(max_length=100, null=True, blank=True) 
    city_district = models.CharField(max_length=100, null=True, blank=True) 
    municipality = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)  
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    website = models.URLField(max_length=300, null=True, blank=True) 
    phone = models.CharField(max_length=20, null=True, blank=True) 

    def __str__(self):
        return f"{self.name} - {self.address}"

    @classmethod
    def get_nearby_cinemas(cls, latitude, longitude, radius_km=10):
        """
        Fetch cinemas near the given latitude and longitude.
        This uses a basic filtering method. For better results, use a GIS database.
        """
        lat_min = latitude - (radius_km / 111)  
        lat_max = latitude + (radius_km / 111)
        lng_min = longitude - (radius_km / 111)
        lng_max = longitude + (radius_km / 111)

        return cls.objects.filter(
            latitude__range=(lat_min, lat_max),
            longitude__range=(lng_min, lng_max)
        )
