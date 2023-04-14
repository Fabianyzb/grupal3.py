encuestas = ["encuesta alimenticia" , "experiencia laboral" , "actividades recreativas" , "atletismo" , "natacion", "deportes en general"]
edad = int(input("Ingrese su edad: "))
origen = input("Eres de LATAM?, Si/No:  ")
deporte = input("tiene afinidad con el deporte?, Si/No: ")

if origen == "Si": 
    print(encuestas[0])

    if edad >= 30 and edad < 60:
        print(encuestas[1])

    elif edad >= 60:
        print(encuestas[2])

    if edad > 60 and deporte =="Si":
        print(encuestas[4])