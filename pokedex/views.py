from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
# Create your views here.
from django.http import HttpResponse
from .models import *
from .serializers import *



import http.client

conn = http.client.HTTPSConnection("pokedex-api1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "172a72fdbdmsh4da69ff0735a3b0p1a6537jsncf214bb78a71",
    'x-rapidapi-host': "pokedex-api1.p.rapidapi.com"
}


traducao = {"fire":"Fogo", "plant": "Planta", "water":"Água","fairy": "Fada","dragon":"Dragão", "steel": "Aço", "poison":"Venenoso", "eletric": "Eletrico", "ground":"Terrestre", "rock":"Pedra", "dark":"Sombrio", "bug":"Inseto", "ice":"Gelo","normal":"Normal", "flying":"Voador", "fighting":"Lutador","ghost":"Fantasma","psychic":"Psiquico"}
place_holder = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png"

def acha_tipo(tipos):
    stats = Tipo.objects.get(name=tipos[0])
    fraquezas =stats.fraquezas
    efetivo = stats.efetivos
    resistencia = stats.resistencia
    imunidade = stats.imunidade
    if len(tipos)==3:
        stats = Tipo.objects.get(name=tipos[1])
        fraquezas1 =stats.fraquezas
        fraquezas1=fraquezas1.split()
        efetivo1 = stats.efetivos
        efetivo1=efetivo1.split()
        resistencia1 = stats.resistencia 
        resistencia1 = resistencia1.split()
        imunidade1 = stats.imunidade
        imunidade1 = imunidade1.split()
        fraquezas_1 = fraquezas.split()
        
    result = [fraquezas,efetivo, resistencia, imunidade]
    return result
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
        # try:
        #     pokemon = Pokemon.objects.get(name=nome)
        # except:
            conn.request("GET", f"/pokemon/detail/{nome}", headers=headers)
            res = conn.getresponse()
            data = res.read()
            result = (data.decode("utf-8"))
            result=result.replace("\\","")
            result = result.replace("[","")
            result = result.replace("]","")
            result = result.replace("\"","")
            # result =result.split(",")
            result =result.split(":")
            # return Response(result)
            for i in range(len(result)):
                if "type" in result[i]:
                    if "Hebrew" not in result[i]:
                        x = result[i+1].split(",")
                        break
            pokemon = Pokemon(name=nome,tipo=tip1, imagem = place_holder, fraquezas=fraquezas, efetivos=efetivo, resistencia=resistencia)
            # return Response({"f":f"{efetivo}"})
            # pokemon.save()
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
    if request.method == "GET":
        tipo = Tipo.objects.get(name=nome)
    if request.method == "PUT":
        tipo = Tipo.objects.get(name=nome)
        tipo.resistencia = request.data["resistencia"]
    tipo_serialized = TypeSerializer(tipo)
    return Response(tipo_serialized.data)
# parei no pedra