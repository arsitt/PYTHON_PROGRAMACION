from ctypes import LibraryLoader
from xml.dom import NotFoundErr


def lector(fichero):
    f = open(fichero)
    return f

def lee_fichero2(nombre):
    lector(r"C:\Users\Mañana\Descargas\hola.txt")
    print("-----------------")
    try:
        raise FileNotFoundError("Este es un error provocado.")
    except FileNotFoundError as e:
        print(f"Error abriendo el archivo: {type(e).__name__}")
        print (e)

    
lee_fichero2("archivo.txt")
