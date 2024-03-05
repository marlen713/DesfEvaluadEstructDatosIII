def choose_level(n_pregunta, p_level):
    """
    Devuelve el nivel de la pregunta, según el número de pregunta y la cantidad de preguntas por nivel.
    ------------
    Parameter
    ------------
    n_pregunta
        Type:   Int
        Descripción:    Número de pregunta (cantidad)
    p_level:
        Type: Int
        Descripción:    Cantidad de preguntas por nivel, nivel 1 a 3
    Return
    ------------
    level
        Type:   String
        Posibles valores:   'basicas', 'intermedias', 'avanzadas'
    """
    # Construir lógica para escoger el nivel
    ##################################################
    level = ""
    if p_level == 1:
        if n_pregunta <= 2:
            level = "basicas"
        elif 2 < n_pregunta <= 4:
            level = "intermedias"
        else:
            level = "avanzadas"
    elif p_level == 2:
        if n_pregunta <= 2:
            level = "basicas"
        elif 2 < n_pregunta <= 4:
            level = "intermedias"
        else:
            level = "avanzadas"
    elif p_level == 3:
        if n_pregunta <= 3:
            level = "basicas"
        elif 3 < n_pregunta <= 6:
            level = "intermedias"
        else:
            level = "avanzadas"
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias