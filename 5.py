cond="si"
def frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10 
   return cantidad
while cond=="si":
    num=int(input("Ingrese un número entero: "))
    un_digito=int(input("ingrese un Dígito: "))
    print("la frecuencia del dígito en el número ingresado es:",frecuencia(num,un_digito))
    cond=input("Desea ingresar nuevamente un número y un digito: ")
    if cond =="no":
        print("La ejecución finalizo")
