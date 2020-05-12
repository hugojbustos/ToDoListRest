from django.shortcuts import render
from django.views.generic import ListView
from .models import Tarea
from rest_framework import viewsets
from .serializers import TareaSerializer
#from .models import Hero


class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all().order_by('id')
    serializer_class = TareaSerializer


# Create your views here.




