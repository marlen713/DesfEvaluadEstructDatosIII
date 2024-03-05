
def validate(opciones, eleccion):
    while eleccion not in opciones:
        print("Opcion no valida. Por favor, ingresa una opcion válida")
        eleccion = input("Ingresa una Opción: ").lower()
    return eleccion


if __name__ == '__main__':
    numeros = ['0','1']
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.

    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    eleccion = validate(numeros, eleccion)
    
    
