# Pesquisa Binária
  
class PesquisaBinaria():

    def pesquisa_binaria(lista, item):
        # numero mais baixo da lista
        baixo = 0

        # numero mais alto da lista
        alto = len(lista) - 1

        while baixo <= alto:
            # será arredondado para baixo automaticamente pelo Python se não for um numero par.
            meio = (baixo + alto)// 2
            chute = lista[meio]

            if chute == item:
                return meio
            
            if chute > item:
                # chute muito alto
                alto = meio - 1
            
            else:
                # chute muito baixo:
                baixo = meio + 1 
        return None

# Testando 1 2 3....

minha_lista = [1, 3, 5, 7, 9]
print(pesquisa_binaria(minha_lista, 5))

'''Notas: 
• A pesquisa binária é muito mais rápida do que a pesquisa simples. 
• O(log n) é mais rápido do que O(n), e O(log n) fica ainda mais rápido conforme os elementos da lista aumentam. 
• A rapidez de um algoritmo não é medida em segundos. • O tempo de execução de um algoritmo é medido por meio de seu crescimento. 
• O tempo de execução dos algoritmos é expresso na notação Big O.

Bhargava, Aditya Y.. Entendendo Algoritmos (p. 43). Novatec Editora. Edição do Kindle. '''