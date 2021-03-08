'''Quando você escreve uma função recursiva, deve informar quando a recursão deve parar. É por isso que toda função recursiva tem duas partes: o caso-base e o caso recursivo. O caso recursivo é quando a função chama a si mesma. O caso-base é quando a função não chama a si mesma novamente, de forma que o programa não se torna um loop infinito.

Bhargava, Aditya Y.. Entendendo Algoritmos (p. 75). Novatec Editora. Edição do Kindle. '''

def regressiva(i):
    print(i)
    if i <= 1:
        return
    else:
        regressiva(i - 1)

print(regressiva(i=0))

# A pilha de chamada com recursão

def fat(x):
    if x == 1:
        return 1
    else: 
        return x * fat(x-1)

print(fat(5))


'''Notas: 
• Recursão é quando uma função chama a si mesma.
• Toda função recursiva tem dois casos: o caso-base e o caso recursivo. 
• Uma pilha tem duas operações: push e pop. 
• Todas as chamadas de função vão para a pilha de chamada. 
• A pilha de chamada pode ficar muito grande e ocupar muita memória.

Bhargava, Aditya Y.. Entendendo Algoritmos (p. 100). Novatec Editora. Edição do Kindle. '''
