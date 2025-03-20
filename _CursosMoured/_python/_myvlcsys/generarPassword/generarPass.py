import string
import random

# Getting password length
length = int(input("Longitud de Password: "))

print('''Choose character set for password from these : 
		1. Numeros
		2. Letras
		3. Especial Caracteres
		4. Exit''')

characterList = ""

# Getting character set for password
while(True):
	choice = int(input("Selecciona una opción:"))
	if(choice == 1):
		
		# Adding letters to possible characters
		characterList += string.ascii_letters
	elif(choice == 2):
		
		# Adding digits to possible characters
		characterList += string.digits
	elif(choice == 3):
		
		# Adding special characters to possible
		# characters
		characterList += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Selecione una opción valida!")

password = []

for i in range(length):

	# Picking a random character from our 
	# character list
	randomchar = random.choice(characterList)
	
	# appending a random character to password
	password.append(randomchar)

# printing password as a string
print("\nLa contraseña autogenerada es " + "".join(password)+"\n")
