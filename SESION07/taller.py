print ("Lista sin modificar: ")
lista = list(range(1,101))
print (lista)

numeros = []
print ("\n Lista modificada")

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        numeros.append("fizzbuzz")
    elif i % 3 == 0:
        numeros.append("fizz")
    elif i % 5 == 0:
        numeros.append("buzz")
    else:
        numeros.append(i)


print(numeros)
