num1=int(input("Ingrese el numero 1 "))
operador= ""
resu=0
while operador != "salir"  :
    operador=input("Que operador requieres hacer : ")
    num2=int(input("Ingrese el numero 2 "))
    if operador == "+":
        resu= num1 + num2
    elif operador == "-":
        resu =num1 - num2
    elif operador == "/":
        resu = num1 / num2 
    elif operador == "*":
        resu =num1 * num2
    print(resu)
    num1=resu
