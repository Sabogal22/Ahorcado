import random

def seleccionar_palabra(nivel):
    palabras = {
        "facil": ["python", "programacion", "computadora", "juego"],
        "medio": ["ahorcado", "aprender", "desarrollo", "codigo"],
        "dificil": ["inteligencia", "artificial", "algoritmo", "complejidad"]
    }
    return random.choice(palabras[nivel])

def mostrar_tablero(palabra, letras_correctas):
    palabra_mostrada = ""
    for letra in palabra:
        if letra in letras_correctas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "
    print(palabra_mostrada)

def dibujar_ahorcado(intentos_restantes):
    partes_ahorcado = [
        """
           ------
           |    |
           |    
           |    
           |    
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    
           |    
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """
    ]
    print(partes_ahorcado[6 - intentos_restantes])

def jugar():
    nivel = input("Selecciona un nivel (fácil, medio, difícil): ").lower()
    if nivel not in ["facil", "medio", "dificil"]:
        print("Nivel no válido. Seleccionando nivel fácil por defecto.")
        nivel = "facil"
    
    palabra_secreta = seleccionar_palabra(nivel)
    letras_correctas = []
    intentos_restantes = 6
    
    print("¡Bienvenido al juego del ahorcado!")
    print("Adivina la palabra secreta.")
    mostrar_tablero(palabra_secreta, letras_correctas)
    
    while intentos_restantes > 0:
        intento = input("Introduce una letra: ").lower()
        
        if len(intento) != 1 or not intento.isalpha():
            print("Por favor, introduce una única letra válida.")
            continue
        
        if intento in letras_correctas:
            print("Ya has intentado esa letra. Intenta con otra.")
            continue
        
        if intento in palabra_secreta:
            letras_correctas.append(intento)
            print("¡Correcto!")
        else:
            intentos_restantes -= 1
            print("Incorrecto. Te quedan {} intentos.".format(intentos_restantes))
        
        dibujar_ahorcado(intentos_restantes)
        mostrar_tablero(palabra_secreta, letras_correctas)
        
        if all(letra in letras_correctas for letra in palabra_secreta):
            print("¡Felicidades! ¡Has adivinado la palabra secreta: {}!".format(palabra_secreta))
            break
    
    if intentos_restantes == 0:
        print("¡Oh no! Te has quedado sin intentos. La palabra secreta era: {}.".format(palabra_secreta))

if __name__ == "__main__":
    jugar()
