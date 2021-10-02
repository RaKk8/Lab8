def sumaDigitos(numero):
    suma=0
    for x in range(numero):
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma
sumTotal=0
num=int(input("Digite el número que desea procesar, si desea finalizar la ejecución ingrese el número '0': "))
while num!=0:
    print("La suma de los digitos es:",sumaDigitos(num))
    sumTotal=sumTotal+num
    num=int(input("Digite el número que desea procesar, si desea finalizar la ejecución ingrese el número '0': "))
    print("La sumatoria es igual a: ", sumTotal)
    print("Dígitos: ",sumaDigitos(sumTotal))
    print("La ejecución finalizo")