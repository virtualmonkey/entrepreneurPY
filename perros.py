with open('Mascotas.csv', encoding='utf-8') as f:
    texto = f.read() #leer el contenido completo
f.close()

print('Contenido del archivo:')

print('===================================')
lineas = texto.split('\n')

losPerros = []
for linea in lineas:
    columnas = linea.split(',')
    losPerros.append(columnas)
    print(columnas)
losPerros.pop()
        
nombre = input("ingrese el nombre del perro: ")
raza = input("ingrese la raza del perro: ")
peso = input("ingrese el peso del perro: ")
nuevoPerro = [nombre, raza, peso]

losPerros.append(nuevoPerro)
print(losPerros)

with open('Mascotas.csv', 'a', encoding='utf-8') as f:
    #nuevaLinea = ','.join(nuevoPerro)
    #nuevaLinea += '\n'
    nuevaLinea = nombre + "," + raza + "," + peso + "\n"

    f.write(nuevaLinea) #escribir
f.close()



