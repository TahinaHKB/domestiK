from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
# Create your views here.

class MemberView(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Membre.objects.all()

class TacheView(viewsets.ModelViewSet):
    serializer_class = TacheSerializer
    queryset = Tache.objects.all()

class FoyerView(viewsets.ModelViewSet):
    serializer_class = FoyerSerializer
    queryset = Foyer.objects.all()