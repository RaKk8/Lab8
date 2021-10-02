def primo(num): 
   for i in range(2,num): 
       if num%i==0:            
           return False 
   return True 
def frecuencia(numero,digito): 
   cantidad=0 
   while numero!=0: 
       ultDigito=numero%10 
       if ultDigito==digito: 
           cantidad+=1 
       numero=numero//10 
   return cantidad 
def factorial(numero): 
   f=1 
   if numero!=0: 
       for i in range(1,numero+1): 
           f=f*i 
   return f 
def sumaDigitos(numero): 
  suma=0 
  while numero!=0: 
      digito=numero%10 
      suma=suma+digito 
      numero=numero//10 
  return suma 
mayor=0 
agregar = "si" 
while agregar == "si": 
    numero=int(input("Ingrese un número primo: ")) 
    while primo(numero): 
        digito=int(input("Dígito: ")) 
        print("Suma de los dígitos:",sumaDigitos(numero)) 
        print("El",digito,"aparece",frecuencia(numero,digito),"veces") 
        if numero > mayor: 
            mayor=numero 
        break 
    else: 
        print("Factorial de",mayor,":",factorial(mayor)) 
        print("El número ingresado no es primo.") 
        print("La ejecución finalizó") 
        break 
    agregar = input("¿Desea ingresar otro número? si o no = ") 
    if agregar == "no": 
        print("Factorial de",mayor,":",factorial(mayor)) 
        print("La ejecución finalizo") 
        break 
