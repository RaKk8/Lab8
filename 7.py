cond="si"
def sumaDigitos(numero):
  suma=0
  while numero!=0:
      digito=numero%10
      suma=suma+digito
      numero=numero//10
  return suma
cantidad=0
mayor=-1
numero=int(input("Ingrese un número positivo: "))
while cond=="si":
    if numero>=0:
        while numero>=0:
            suma=sumaDigitos(numero)
            if suma > mayor:
                mayor=suma
                n_mayorsuma=numero
            if suma < 10:
                cantidad+=1
            print("Sumatoria de dígitos de",n_mayorsuma,":",mayor)
            print("Cantidad con sumatoria menor a 10:",cantidad)
            cond=input("¿Desea ingresar un nuevo número? ")
            numero=int(input("Número positivo: "))
    else:
        print("el numero ingresado es incorrecto")
        cond=="si"
