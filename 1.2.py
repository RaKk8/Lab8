def validar(email):
    respuesta=False
    if "@" in email:
        respuesta=True
    return respuesta
direccion=input("Por favor ingrese una dirección de correo electronico activa: ")
if validar(direccion):
    print("La dirección de correo electronico es valida")
else:
    print("La dirección de correo electronico es invalida, por favor intentelo nuevamente")
