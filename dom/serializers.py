from rest_framework import serializers
from .models import *

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membre
        fields = ('__all__')

class TacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tache
        fields = ('__all__')

class FoyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foyer
        fields = ('__all__')