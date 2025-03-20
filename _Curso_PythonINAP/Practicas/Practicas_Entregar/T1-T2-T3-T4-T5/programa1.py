#### Programa 1 
#### CONVERSOR DE SEGUNDOS A MINTUOS
#### Solicitud de valor en segundos por teclado y devolución de minitus

#### Alumno: VICENTE LUIS CÁNOVAS GIL

print("CONVERSOR DE SEGUNDOS A MINTUOS:")

segundos=0
segundos = input("Escriba la cantidad de segundos:\n")
int_segundos= int (segundos)
minutos= int_segundos //60
segundos_restantes =  int_segundos % 60


print(f"{int_segundos} segundos son " +  f"{minutos} minutos y " + f"{segundos_restantes} segundos." )

##print(f"{int_segundos} segundos son" f"{minutos}  "+ minutos+ "y  f"{segundos_restantes}  segundos"))