edad=int(input("Hola, escribe tu edad: "))

if ((edad >=20) and (edad<=100)):
    print("Ya eres mayor de edad")
    print("Naciste en el año:" + str (2020-edad))
elif ((edad>0) and (edad<100)):
    print("Eres menor de edad")
    print("Naciste en el año:" + str (2020-edad))
else: 
    print("Edad no es valida")