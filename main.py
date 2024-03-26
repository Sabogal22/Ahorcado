import random

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + ' '
        else:
            displayed_word += '_ '
    return displayed_word

def hangman():
    print("Bienvenido al juego del ahorcado!")
    
    # Pedir al usuario que ingrese una palabra
    word = input("Ingresa la palabra para que alguien más la adivine: ").lower()
    # Limpiar la pantalla
    print("\n" * 50)
    
    # Lista de letras ya adivinadas
    guessed_letters = []
    
    # Número máximo de intentos
    max_attempts = 6
    attempts = 0
    
    while attempts < max_attempts:
        # Mostrar la palabra oculta con las letras adivinadas
        print(display_word(word, guessed_letters))
        
        # Mostrar el número de intentos restantes
        print("Intentos restantes:", max_attempts - attempts)
        
        # Pedir al usuario que ingrese una letra
        guess = input("Adivina una letra: ").lower()
        
        # Validar que la entrada sea una sola letra
        if len(guess) != 1:
            print("Por favor, ingresa solo una letra.")
            continue
        
        # Si la letra ya fue adivinada
        if guess in guessed_letters:
            print("Ya has adivinado esa letra. ¡Intenta con otra!")
            continue
        
        # Añadir la letra a la lista de letras adivinadas
        guessed_letters.append(guess)
        
        # Si la letra no está en la palabra
        if guess not in word:
            print("¡Incorrecto!")
            attempts += 1
        else:
            print("¡Correcto!")
        
        # Verificar si se ha adivinado toda la palabra
        if display_word(word, guessed_letters).replace(' ', '') == word:
            print("¡Felicidades! ¡Has adivinado la palabra correctamente!")
            break
    
    if attempts == max_attempts:
        print("Lo siento, has agotado todos tus intentos. La palabra era:", word)

# Ejecutar el juego
hangman()
