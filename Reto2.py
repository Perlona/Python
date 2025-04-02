contactos = {}
def agregar_contacto ():
    nombre=input("Ingrese el nombre ")
    telefono=input("Ingrese el telefono")
    correo=input("Ingrese el correo")
    contactos[nombre]={"telefono":telefono , "correo":correo}
    print(f"el contacto {nombre} se a agregado correctamente")

def eliminar_contactos () : 
    nombre =input("Ingrese el nombre del contacto a eliminar ")
    if nombre in contactos:
        del contactos[nombre]
        print(f"El contacto {nombre} fue eliminado correctamente ")

def lista_contactos () : 
    if not contactos:
        print("No hay contactos guardados")
    for nombre ,datos in contactos.items():
        print(f"{nombre},{datos["telefono"]} | {datos["correo"]}")

while True : 
    print("Menu")
    print("***************************************************")
    print("1-Agregar contactos")
    print("2-Listar contactos")
    print("3-Eliminar contactos")
    print("Salir")
    opcion=input("Elija una opcion")
    if opcion=="1":
        agregar_contacto()
    elif opcion=="2":
        lista_contactos()
    elif opcion=="3":
        eliminar_contactos()
    elif opcion=="4":
        break
    else:
        print("Opcion no valida")