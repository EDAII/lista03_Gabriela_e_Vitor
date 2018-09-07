from random import *
import os
import time

def quicksort(vector,min,max):

    pivo = getPivo(min,max)
    storeIndex = min
    aux = vector[max]
    vector[max] = vector[pivo]
    vector[pivo] = aux

    print('Pivo  ' + str(vector[min]) + ' ' + str(pivo))
    for i in range(min,max):
        if vector[i] < vector[max]:
            print(vector)
            aux = vector[storeIndex]
            vector[storeIndex] = vector[i]
            vector[i] = aux
            print(vector)
            storeIndex += 1
    aux = vector[max]
    vector[max] = vector[storeIndex]
    vector[storeIndex] = aux
    return storeIndex

def chama_quicksort(vector,start,end):
    if end > start:
        pos = quicksort(vector,start,end)
        chama_quicksort(vector,start,pos-1)
        chama_quicksort(vector,pos+1,end)
    
def getPivo(min,max):
    pivo = (max-min)/2 + min
    return pivo

def generate_vector(size, intervals):
    random_vector = []
    for i in range(size):
        new_element = randint(0,intervals)
        random_vector.append(new_element)
    return random_vector

vector = generate_vector(10,100)
print(vector)
chama_quicksort(vector,0,len(vector)-1)
print(vector)

# 51 37 44 65 31 89 11 28 15 28
# 11 28 15 28 31 89 51 37 44 65
# 11 15 28 28 31 37 44 51 65 89

     