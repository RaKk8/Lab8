def factorial(numero):
   f=1
   if numero!=0:
       for i in range(1,numero+1):
           f=f*i
   return f
cantidad=0
num=int(input("Ingrese un número para conocer su factorial, si desea finalizar la ejecución ingrese '-1': "))
while num!=-1:
    print("Factorial:", factorial(num))
    cantidad+=1
    num=int(input("Ingrese un número para conocer su factorial, si desea finalizar la ejecución ingrese '-1': "))
print("Se procesaron",cantidad,"números ingresados")
