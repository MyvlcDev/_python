#### Programa 2
#### AREA DE UN TRIANGULO Y CIRCULO
#### Solicitud de valor en segundos por teclado y devolución de minitus

#### Alumno: VICENTE LUIS CÁNOVAS GIL

print("CÁLCULO DE AREAS DE TRIANGULO Y CIRCULO:")

print("Elija la figura geométrica: ")
print("1) Triángulo (T)") 
print("2) Circulo (C)") 
op=input("¿Qué figura quiere calcular (Escriba T o C)? ")
opcion = op.upper()

match opcion:
    case "T":
        print("Cálculo del area de un triángulo ")
        base=input("Cuál es la base: ")
        altura= input ("Cuál es la altura: ")
        area_triangulo = float (base) * float (altura) / 2.0
        print("El area del triángulo indicado es " + str (area_triangulo))
    
    case "C":
        print("Dentro de la opicoón C")
        Pi= 3.1416
        radio= input("Cuál es el radio: ")
        area_circulo= (float(radio) * float(radio) )* Pi
        print("El área del circulo indicado es " + str (area_circulo) )
