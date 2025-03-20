print ("Programa de evaluacion de notas")

nota_alumno=input()


def evalauacion (nota):
    valoracion= "aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion




print(evalauacion(int(nota_alumno)))