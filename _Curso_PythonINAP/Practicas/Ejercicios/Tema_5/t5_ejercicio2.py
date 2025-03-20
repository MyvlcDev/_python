def distancia(x1, y1, x2, y2):
    dx= x2 - x1
    dy= y2 - y1
    dist= (  dx**2 + dy**2)**0.5
    return dist

x1=float(input("Introduce la coordena x del primer punto: ")) 
y1=float(input("Introduce la coordena y del primer punto: ")) 
x2=float(input("Introduce la coordena x del segundo punto: ")) 
y2=float(input("Introduce la coordena y del segundo punto: ")) 

print("La distancia entre los dos puntos es ", distancia(x1,y1,x2,y2))