cond="si"
def primo(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True
while cond == "si":
    numero=int(input("ingrese un Número: "))
    if primo(numero):
        print("El número es primo")
    else:
        print("El número no es primo")
    cond=input("¿Desea ingresar otro Número? ")
    if cond == "no":
        print("La ejecución finalizo.")
