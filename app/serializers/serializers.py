from rest_framework import serializers
from app.models.game_models.console import Console  

class Get_All_Items(serializers.ModelSerializer):
    class Meta:
        model = Console
        fields = '__all__'