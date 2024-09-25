import interface
import database
from settings import VERSION
from models import Contacto

def read():
    pass

def create():
    print(interface.CREAR_CONTACTO)
    nombre_contacto = input(interface.CREAR_CONTACTO_NOMBRE)
    telefono_contacto = input(interface.CREAR_CONTACTO_TELEFONO)
    email_contacto = input(interface.CREAR_CONTACTO_EMAIL)
    contacto = Contacto(nombre_contacto, telefono_contacto, email_contacto)
    # De momento solo esto de pruebas
    print(contacto)  # test
    print(contacto.nombre, contacto.telefono, contacto.email)

def update():
    pass

def delete():
    pass

def about():
    print(f"La version actual es {VERSION}")

command_interface = {
    1: read,
    2: create,
    3: update,
    4: delete,
    5: about
}