#EJERCICIOS BUCLE FOR BASICO 1

# 1. Básico: imprime todos los números enteros del 0 al 150: 
for num in range(151):
    print(num)

print("-----------------------------------------")

# 2. Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1000: 
for num in range(5, 1001, 5):
    print(num)

print("-----------------------------------------")

# 3. Contar a la manera del Dojo: imprime números enteros del 1 al 100. 
# si es divisible por 5, imprime "coding", si es divisible por 10, imprime "coding dojo":
for num in range(1, 101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)

print("-----------------------------------------")        


# 4. Whoa es un gran idiota: agrega los enteros impares del 0 al 500000 e imprime la suma final:
total = 0
for num in range(1, 500001, 2):
    total += num
print(total)

print("-----------------------------------------")

# 5. Cuenta regresiva de a 4: imprime números positivos desde el 2018, en cuenta regresiva de 4 en 4:
for num in range(2018, 0, -4):
    print(num)

print("-----------------------------------------")

#6. Contador flexible: establece tres variables: lowNum, highNum, mult
# comenzando en lowNum y pasando por highNum imprime solo los enteros que sean múltiplos de mult:
lowNum = 2
highNum = 9
mult = 3
for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)
