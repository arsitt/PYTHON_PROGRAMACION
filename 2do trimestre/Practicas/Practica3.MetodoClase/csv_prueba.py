import csv


def crea_csv():
    with open(r'C:\Users\Mañana\Desktop\Alejandro Rodriguez Curso 21-22\PROGRAMACIONGIT\PYTHON_PROGRAMACION\2do trimestre\Practicas\Practica3.MetodoClase\alumno.txt') as f:
        reader = csv.DictReader(f)
        for row in reader:
            alumno = row['alumno']
            boletin1 = row['boletin1']
            boletin2 = row['boletin2']
            boletin3 = row['boletin3']
            boletin4 = row['boletin4']
    return print(f'Nombre: {alumno}\nLM: {boletin1}\n Entorno: {boletin2}')

crea_csv()



