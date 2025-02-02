from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models.game_models.console import Console  
from app.serializers.serializers import Get_All_Items 

@api_view(['GET'])
def get_consoles(request):
    print(type(Get_All_Items)) 
    
    items = Console.objects.all()
    serializer = Get_All_Items(items, many=True) 
    return Response(serializer.data)