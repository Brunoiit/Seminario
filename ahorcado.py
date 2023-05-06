import random

def get_word():
    # Esta función devuelve una palabra aleatoria de una lista de palabras.
    words = ["abanico", "araña", "banco", "bicicleta", "brujula", "calcetines", "camioneta", "candado", "caramelo", "carretera", "casa", "cebra", "círculo", "cloro", "conejo", "corona", "dinosaurio", "diente", "elefante", "estrella", "fresa", "fruta", "galleta", "gato", "guitarra", "helado", "hipopotamo", "iglesia", "insecto", "jirafa", "juguete", "laberinto", "limon", "luna", "madera", "mariposa", "maiz", "mesa", "murcielago", "naranja", "oveja", "pelota", "perro", "piano", "rana", "rueda", "sol", "tigre", "tortuga", "zanahoria"]

    return random.choice(words)

def play_hangman():
    word = get_word()
    word_letters = set(word)  # Letras únicas de la palabra
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()  # Letras que el jugador ya ha adivinado
    tries = 6

    while len(word_letters) > 0 and tries > 0:
        # Mostrar el estado actual del juego
        print('Intentos restantes:', tries)
        print('Letras utilizadas:', ' '.join(used_letters))

        # Mostrar la imagen del ahorcado
        print(display_hangman(tries))

        # Mostrar la palabra a adivinar (con guiones en lugar de letras no adivinadas)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Palabra: ', ' '.join(word_list))

        # Obtener la letra del jugador
        user_letter = input('Adivina una letra: ').lower()

        # Verificar si la letra ya ha sido adivinada anteriormente
        if user_letter in used_letters:
            print('Ya has adivinado esa letra antes. Intenta otra.')
        # Verificar si la letra está en la palabra
        elif user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                tries -= 1
                print('La letra', user_letter, 'no está en la palabra.')
        # Verificar si la letra ya ha sido utilizada antes, pero no adivinada
        else:
            print('Caracter inválido. Intenta otra letra.')

    # Salir del bucle while cuando el usuario adivina la palabra o se quedan sin intentos
    if tries == 0:
        print(display_hangman(tries))
        print('¡Agotaste todos los intentos! La palabra era', word)
    else:
        print('¡Felicidades! Adivinaste la palabra', word, '!')

def display_hangman(tries):
    # Esta función muestra el dibujo del ahorcado según el número de intentos que quedan.
    stages = [  # La imagen del ahorcado en cada intento.
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |      
                   |     
                   |     
                   -
                """
            ]
    return stages[tries]


play_hangman()
