from rest_framework import serializers
from .models import *
class PokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields =['id','name','imagem','tipo','fraqueza']
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields =['id','name','fraquezas','efetivos','resistencia']