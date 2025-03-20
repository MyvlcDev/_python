
def quitar_carcter(frase, letra):
    caracteres = list(frase)
    nueva_frase = []
    
    for caracter in caracteres:
        if caracter != letra:
            nueva_frase.append(caracter)
    

    return ''.join(nueva_frase)


frase_original = "uno, dos, tres, cuatro, cinco"
letra_a_eliminar = "o"
frase_sin_letra = quitar_carcter(frase_original, letra_a_eliminar)
print("Frase original:", frase_original)
print("Frase sin la letra '", letra_a_eliminar, "':", frase_sin_letra)