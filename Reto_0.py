# Reto #0
 # EL FAMOSO "FIZZ BUZZ"
 # Fecha publicación enunciado: 27/12/21
 # Fecha publicación resolución: 03/01/22
 # Dificultad: FÁCIL
 # Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea
 # entre cada impresión), sustituyendo los siguientes:
 # - Múltiplos de 3 por la palabra "fizz".
 # - Múltiplos de 5 por la palabra "buzz".
 # - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 #
 # Información adicional:
 # - Ejercicio sacado de:
 # - https://github.com/mouredev/Weekly-Challenge-2022-Kotlin/blob/main/app/src/main/java/com/mouredev/weeklychallenge2022/Challenge0.kt
 # - https://retosdeprogramacion.com/semanales2022
 #

def multiplos()->None:
    """
    Funcion que sustituye los multiplos de 3 por la plabra fizz,
    los multiplos de 5 por la palabra buzz y los multiplos de 
    ambos por la palabra fizzbuzz

    parametros: None

    return: None
    """
    for i in range(1,101):
        if i % 3 == 0 and i % 5 ==0:
            print("fizzbuzz\n")
        elif i % 3 == 0:
            print("fizz\n")
        elif i % 5 == 0:
            print("buzz\n")
        else:
            print(f"{i}\n")


if __name__ == '__main__':
    multiplos()
