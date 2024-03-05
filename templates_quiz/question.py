import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    """
    Escoge pregunta según dificultad, va de 1 a 3 preguntas y utiliza el indice de opciones para no repetir preguntas.
    Devuelve el enunciado de la pregunta y las alternativas mezcladas.
    ------------
    Parameter
    ------------
    dificultad
        Type:   String
        Posibles valores:   'basicas', 'intermedias', 'avanzadas'
    Return
    ------------
    pregunta['enunciado']
        Type:   Array
        Ejemplo:    ['Enunciado básico 1']
    
    alternativas
        Type:   Array
        Ejemplo:    [['alt_2', 0], 
                    ['alt_4', 1], 
                    ['alt_3', 0], 
                    ['alt_1', 0]]
    """

    #escoger preguntas por dificultad
    preguntas = p.pool_preguntas[dificultad]
    
    # usar opciones desde ambiente global
    global opciones
    # escoger una pregunta
    n_elegido = random.choice(opciones[dificultad])
    # eliminarla del ambiente global para no escogerla de nuevo|
    
    opciones[dificultad].remove(n_elegido)
    
    pregunta_index="pregunta_"+str(n_elegido)
    # escoger enunciado y alternativas mezcladas
    pregunta = preguntas[pregunta_index]
    alternativas = shuffle_alt(pregunta)
    
    
    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')