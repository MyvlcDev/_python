def producto(a, b):
    return float(a) * float (b)

def main():
    a= input('Inserte el primer número:')
    b= input('Inserte el segundo número:')
    res= producto(a,b)
    print(f'El resultado del producto es: {res}')

if __name__ == '__main__':
    main()