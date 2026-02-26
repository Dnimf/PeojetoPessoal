from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    imagem = models.ImageField('./img_dados')
    tipo = models.TextField()
    fraquezas = models.TextField()
    efetivos = models.TextField()
    resistencia = models.TextField()
    
    def __str__(self):
        return f"{self.name}: {self.tipo}, {self.efetivos},{self.resistencia}"

class Treinador(models.Model):
    name = models.CharField(max_length=100)
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    p3 = models.CharField(max_length=100)
    p4 = models.CharField(max_length=100)
    p5 = models.CharField(max_length=100)
    p6 = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tipo(models.Model):
    name = models.CharField(max_length=100)
    fraquezas = models.TextField()
    efetivos = models.TextField()
    resistencia = models.TextField()
    def __str__(self):
        return f"{self.name}: {self.fraquezas}, {self.efetivos}, {self.resistencia}"