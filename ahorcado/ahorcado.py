import random

imagenes_ahorcado = ['''     
    +---+
    |   |
        |
        |
        |
        |
    ==========
            ''',
'''     
    +---+
    |   |
    O   |
        |
        |
        |
    ==========
            ''',
'''     
    +---+
    |   |
    O   |
    |   |
        |
        |
    ==========
            ''',
'''     
    +---+
    |   |
    O   |
   /|   |
        |
        |
    ==========
            ''',
'''     
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    ==========
            ''',
'''     
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    ==========
            ''',
'''     
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    ==========
            '''
]

palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra '.split()

def obtenerPalabraAlAzar(listaPablabras):
    indiceDePalabras = random.randint(0, len(listaPablabras) -1 )
    return listaPablabras[indiceDePalabras]

def mostrarTablero(imagenes_ahorcado, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(imagenes_ahorcado[len(letrasIncorrectas)])
    print()
    print("Letras incorrectas: ", end="")
    for letra in letrasIncorrectas:
        print(letra, end=" ")
    print()

    espaciosVacios = '_' * len(palabraSecreta)

    for i in len(palabraSecreta):
        if palabraSecreta[i] in letrasCorrectas
    print("Palabra secreta: ", espaciosVacios)

print(mostrarTablero(imagenes_ahorcado, "AAAA", "BBBB", obtenerPalabraAlAzar(palabras)))