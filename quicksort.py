
# Escreva o código para a função soma

def soma(lista):
    if lista == []:
        return 0
    
    return lista[0] + soma(lista[1:])

# print(soma([1,2,3]))

# Escreva uma função recursiva que conte o número de itens em uma lista.

def conta(lista):
    if lista == []:
        return 0
    
    return 1 + conta(lista[1:])

# print(conta([1,2,3]))

# Encontre o valor mais alto em uma lista.

def maximo(lista):
    
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]

    sub_max = maximo(lista[1:])
    
    return lista[0] if lista[0] > sub_max else sub_max

# print(maximo([1,5,3]))

# Quicksort 

def quickSort(arr):
    if len(arr) < 2:
        return arr # Base: arrays com 0 ou 1 elemento já estão “ordenados”.

    else: 
     pivo = arr[0] # Caso recursivo.
     menores = [i for i in arr[1:] if i <= pivo] # Subarray de todos os elementos menores do que o pivô.
     maiores = [i for i in arr[1:] if i > pivo] # Subarray de todos os elementos maiores do que o pivô.
     
     return quickSort(menores) + [pivo] + quickSort(maiores)

print(quickSort([10, 5, 2, 3]))