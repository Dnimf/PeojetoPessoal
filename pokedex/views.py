from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
# Create your views here.
from django.http import HttpResponse
from .models import *
from .serializers import *


def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")
@api_view(['GET', 'PUT', 'POST'])
def pokemon_banco(request, nome):
    if request.method == "POST":
        new_pok = request.data
        name = new_pok["name"]
        img = new_pok["imagem"]
        tipo = new_pok["tipo"]
        fraqueza = new_pok["fraqueza"]
        pokemon = Pokemon(name=name, imagem=img, tipo=tipo, fraqueza=fraqueza)
        pokemon.save()
    if request.method == "GET":
        pokemon = Pokemon.objects.get(name=nome)
    poke_serialized = PokSerializer(pokemon)
    return Response(poke_serialized.data)

@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def tipos(request,nome):
    if request.method == "POST":
        new_type = request.data
        nome = new_type["name"]
        fraquezas = new_type["fraquezas"]
        efetivos = new_type["efetivos"]
        resistencia = new_type["resistencia"]
        tipo = Tipo(name=nome, fraquezas=fraquezas, efetivos=efetivos, resistencia=resistencia)
        tipo.save()
    tipo_serialized = TypeSerializer(tipo)
    return Response(tipo_serialized.data)
# parei no terrestre