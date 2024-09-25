import database, interface
from logic import command_interface
from utils import crear_interfaz

def main():
    print(interface.INTERFAZ_BASE)
    eleccion = crear_interfaz()
    while not 1 <= eleccion <= 5:
        print(interface.INTERFAZ_ELECCION_ERRONEA)
        eleccion = crear_interfaz()
    comando = command_interface[eleccion]

if __name__ == "__main__":
    main()
