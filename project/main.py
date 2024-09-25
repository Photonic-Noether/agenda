import interface
from logic import command_interface
from utils import crear_interfaz

def main():
    print(interface.INTERFAZ_BASE)
    eleccion = crear_interfaz()
    while not 1 <= eleccion <= 5:
        print(interface.INTERFAZ_ELECCION_ERRONEA)
        eleccion = crear_interfaz()
    comando = command_interface[eleccion]
    comando()
    eleccion_salir = input(interface.INTERFAZ_SALIDA)
    if eleccion_salir.lower() in ("si", "s", "yes", "y"):
        main()

if __name__ == "__main__":
    main()
