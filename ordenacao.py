# ordenar um array do menor para o maior

def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i

    return menor_indice


# teste = buscaMenor(arr=[2,3,4])
# print(teste)

# usar a função para escrever a ordenação por seleção

def ordenacaoporSelecao(arr):
    novoArr = []

    for i in range(len(arr)):        
        menor = buscaMenor(arr)        
        novoArr.append(arr.pop(menor))
    
    return novoArr

print(ordenacaoporSelecao(arr=[5,3,6,2,10]))


'''Notas:
• A memória do seu computador é como umc onjunto gigante de gavetas. 
• Quando se quer armazenar múltiplos elementos, usa-se um array ou uma lista. 
• No array, todos os elementos são armazenados um ao lado do outro. 
• Na lista, os elementos estão espalhados e um elemento armazena o endereço do próximo elemento. 
• Arrays permitem leituras rápidas. • Listas encadeadas permitem rápidas inserções e eliminações. 
• Todos os elementos de um array devem ser do mesmo tipo (todos ints, todos doubles, e assim por diante).


Bhargava, Aditya Y.. Entendendo Algoritmos (p. 67). Novatec Editora. Edição do Kindle. '''

