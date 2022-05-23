import pandas as pd
import numpy as np

class Medidas_de_tendencia_central:
    def __init__(self, datos):
        self.datos = datos
        self.n = len(datos)

    def get_datos(self):
        return self.datos

    def get_tamaño(self):
        return self.n

    def ordenar(self, dejarla_ordenada = False):
        if dejarla_ordenada:
            self.datos.sort()
        else:
            return sorted(self.datos)

    def calcular_rango(self):
        datos_ordenados = self.ordenar()
        self.minimo = datos_ordenados[0]
        self.maximo = datos_ordenados[self.n - 1]
        self.rango = self.maximo - self.minimo

    def get_maximo(self):
        return self.maximo

    def get_minimo(self):
        return self.minimo

    def get_rango(self):
        return self.rango

    def calcular_media(self):
        suma = 0
        for dato in self.datos:
            suma += dato

        self.media = suma / self.n

    def get_media(self):
        return self.media

    def es_par(self):
        if self.n % 2 == 0:
            return True
        else:
            return False

    def calcular_mediana(self):
        datos_ordenados = self.ordenar()
        if self.es_par():
            rango_mediana = int(self.n / 2)
            self.mediana = datos_ordenados[rango_mediana - 1] + (datos_ordenados[rango_mediana] - datos_ordenados[rango_mediana - 1]) / 2
        else:
            rango_mediana = (self.n + 1) / 2
            self.mediana = datos_ordenados[rango_mediana - 1]

    def get_mediana(self):
        return self.mediana

    def calcular_moda(self):
        datos_ordenados = self.ordenar()
        temp = 0
        contador = 0
        moda = -1
        for i in range(0, self.n - 1):
            if datos_ordenados[i] == datos_ordenados[i+1]:
                contador += 1
                if contador >= temp:
                    temp = contador
                    moda = datos_ordenados[i]
                else:
                    contador = 0
        self.moda = moda

    def get_moda(self):
        return self.moda

    def __str__(self):
        print('Nuestras medidas de tendencia central son las siguientes:')
        return f'Media: {self.media}\nMediana: {self.mediana}\nModa: {self.moda}'


class Dispersion:
    def __init__(self):
        


notas = Medidas_de_tendencia_central([3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16])
notas.calcular_rango()
notas.calcular_media()
notas.calcular_mediana()
notas.calcular_moda()

print(notas)



