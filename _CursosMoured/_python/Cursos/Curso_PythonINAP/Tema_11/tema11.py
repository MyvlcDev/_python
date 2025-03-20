import re
text = u'Bievenido al múdolo de expresiones regulares del curso "Introducción a Python"'
pattern = r'Python'
result = re.search(pattern, text)

print (result )

print("\n")

pattern = "f"
text1= "fresa"
text2= "coliflor"


print("Text1 :" , re.match(pattern, text1))
print("Text2 :" , re.match(pattern, text2))

print("\n")

text3=u'Lunes: 1, Martes: 2, Miércoles: 3, Jueves: 4, Viernes: 5, Sábado:6, Domingo: 7 '
pattern = r'[0-9]'
result = re.findall(pattern, text3 )
print (result)

print("\n")

text4=u'Lunes: 1, Martes: 2, Miércoles: 3, Jueves: 4, Viernes: 5, Sábado:6, Domingo: 7 '
pattern = r'\d'
result = re.findall(pattern, text4 )
print (result)

text5= u'1. Madrid: 3334730, 2. Barcelona: 1664182, 3 . Valenciaa: 800215, 4. Sevilla: 691395, 5. Zaragoza: 681877, 6. Málaga: 578460 7. Murcia: 459403, 8. Palma de Mallorca, 422587, 9. Las Palmas: 381223, 10. Bilbao: 350184'
pattern = r'\d{7}' ##cuales superan un millon, es decir 7 cifras
result = re.findall(pattern, text5 )
print (result)

re.search()