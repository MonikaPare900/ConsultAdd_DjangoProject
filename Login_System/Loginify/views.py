from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import UserDetails
from .serializers import UserDetailSerializer



# Create your views here.

def print_hello(request):
    return HttpResponse("Hello World !")

def get_all_data(request):
    if request.method=='GET':
        try:
            all_users = UserDetails.objects.all()
            serializer_data = UserDetailSerializer(all_users,many=True)
            return JsonResponse(serializer_data,safe=False)
        except Exception as e:
            return JsonResponse({"error":str(e)})


