import random

#Funciones

def Generar_preguntas(eleccion):
    
    try:
        if eleccion == 0:
            pregunta=open("Deportes.txt","r",encoding="utf-8")
        if eleccion == 1:
            pregunta=open("Arte.txt","r",encoding="utf-8")
        if eleccion == 2:
            pregunta=open("Geografia.txt","r",encoding="utf-8")
        if eleccion == 3:
            pregunta=open("Espectaculo.txt","r",encoding="utf-8")
        if eleccion == 4:
            pregunta=open("Historia.txt","r",encoding="utf-8")
            
        inicio=1
        final=3
        pos=0
        randomizador=random.randint(inicio,final)
        linea=pregunta.readline()
        while linea:
            linea=linea.strip()
            linea=linea.split(";")
            if linea[0] == str(randomizador):
                pos+=1
                hacer_preguntas(linea,pos)
                inicio+=3
                final+=3
                randomizador=random.randint(inicio,final)
            linea=pregunta.readline()
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:",mensaje)
    except OSError as mensaje:
        print("no se pudo leer el archivo",mensaje)
    finally:
        try:
            pregunta.close()
        except NameError:
            pass

def hacer_preguntas(preguntas_generadas,pos):
    puntos=0
    pregunta_original=preguntas_generadas[1]
    respuesta_verdadera=preguntas_generadas[2]
    procesar_respuesta(pregunta_original,respuesta_verdadera,puntos,pos)


def procesar_respuesta(pregunta_original,respuesta_verdadera,puntos,pos):
    
    pistas_usadas=0
    cont2=0
    escondida=""
    for letra in respuesta_verdadera:
        if letra.isalpha():
            letra=letra.replace(letra,"?")
            escondida=escondida+letra
        else:
            escondida=escondida+letra
                
    while True:
        print("\n"*4)
        print("*"*100)
        print("*",("La pregunta es: ").center(96),"*".rjust(0))
        print("*"*100)
        print("*",pregunta_original.center(96),"*".rjust(0))
        print("*"*100)
        print("*escriba \"PISTA\" para revelar una letra*".center(100," "))
        respuesta_del_jugador=input(f"{escondida} (+{10 - pistas_usadas}Pts):")
        
        
        if respuesta_del_jugador.lower() == "pista" and pistas_usadas < len(escondida):
            escondida=list(escondida)
            pistas_usadas+=1
            escondida[cont2]=respuesta_verdadera[cont2]
            escondida="".join(escondida)
            cont2+=1
            if pistas_usadas > 10:
                pistas_usadas = 10

        if respuesta_del_jugador.lower() == respuesta_verdadera.lower():            
            puntos=10-pistas_usadas
            print("\n")
            print("*"*100)
            print(("CORRECTO").center(100))
            print("*"*100)
            break
        
        if respuesta_del_jugador.lower() != respuesta_verdadera.lower() and respuesta_del_jugador.lower() != "pista":
            print("\n")
            print("*"*100)
            print("*",("INCORRECTO").center(96),"*".rjust(0))
            print("*",(f"La respuesta era: {respuesta_verdadera}").center(96),"*".rjust(0))
            print("*"*100)
            puntos=0
            break
        
    mostrar_matriz(matriz,puntos,eleccion,pos,respuesta_verdadera)
    generar_diccionario(diccionario,matriz,eleccion,pos,respuesta_verdadera,tupla)
    print("\n")
    print(f"*Los puntos totales son: {sumar_matriz(matriz)}*".center(100))
    input(("*oprima \"ENTER\" para continuar*").center(100))

def mostrar_matriz(matriz,puntos,eleccion,pos,respuesta_verdadera):    
    matriz[eleccion][pos]=puntos
    for b in range(len(matriz)):
        print("\n")
        for c in range(len(matriz)):
            print((f"{matriz[b][c]}"), end=" ")
            
def generar_diccionario(diccionario,matriz,eleccion,pos,respuesta_verdadera,tupla):
    tupla=tupla+(f"{matriz[eleccion][pos]} | {respuesta_verdadera}",)
#    diccionario.add(f"({matriz[eleccion][pos]} | {respuesta_verdadera})")
    diccionario[f"{matriz[eleccion][0]} (Pts | Respuesta)"]=tupla
    print("\n",diccionario)
    #([f"({matriz[eleccion][pos]} | {respuesta_verdadera})"])

    


def sumar_matriz(matriz,suma=0,fila=0,columna=0):
    
    longitud=len(matriz)
    if columna < longitud:
        try:
            suma=suma+matriz[fila][columna]
        except TypeError:
            pass
        return sumar_matriz(matriz,suma,fila,columna+1)
    if columna == longitud and fila < longitud-1:
#        print(fila,columna)
        return sumar_matriz(matriz,suma,fila+1,columna=0)
    else:
        return suma   

def filtrar_eleccion(categorias):
    
    try:
        opcion=input(f"* Ingrese la categoria del 1 al 5 y luego aprete ENTER * \n".center(100))
        assert opcion.isdigit(),"**Solo se aceptan los numeros del 1 al 5**".center(100)
        assert 1 <= int(opcion) <= 5,"**Solo se aceptan los los numeros del 1 al 5**".center(100)
    except AssertionError as mensaje:
            print(mensaje,"\n")
            print(":'(".center(100),"\n"*2)
            print("*"*100)
            print("*"*3,"1.",categorias[0],"*"*5,"2.",categorias[1],"*"*5,"3.",categorias[2],"*"*5,"4.",categorias[3],"*"*5,"5.",categorias[4],"*"*3)
            print("*"*100)
            return filtrar_eleccion(categorias)
    return opcion

def verificar_ultima_opcion():
    
    try:
        print(("*"*90).center(100))
        print((f"* 1) Ingrese \"RESET\" para volver a empezar.  |  2) Presione \"ENTER\" para cerrar el juego *").center(100))
        print(("*"*90).center(100))
        ultima_opcion=input("\n".center(100))
        ultima_opcion=ultima_opcion.lower()
        assert ultima_opcion == "reset" or ultima_opcion == "","**Solo se acepta RESET o ENTER**".center(100)
    except AssertionError as mensaje:
        print(mensaje,"\n")
        return verificar_ultima_opcion()
    return ultima_opcion

#Programa Principal
    
print("*"*100)
print("BIENVENIDO AL MEMORIOSO".center(100,"*"))
print("*"*100)
print("*","*".rjust(98))
print("*","#","Es un juego clasico de preguntas y respuestas en el que usted selecciona que categoria jugar.","*".rjust(2))
print("*","*".rjust(98))
print("*","#","Consta de 4 preguntas por cada una de las 5 categorias, cada pregunta correcta vale 10 puntos.","*".rjust(1))
print("*","*".rjust(98))
print("*","#","Si se contesta la pregunta de forma erronea se dara esa pregunta por perdida con 0 puntos","*".rjust(6))
print("*","*".rjust(98))
print("*","#","Si no la sabe puede tener una pista, pero por cada ayuda se le restara 1 punto.","*".rjust(16))
print("*","*".rjust(98))
print("*"*100)
nada=input(f"* Para comenzar oprima solo ENTER *".center(100))
if nada != "":
    print("Era solo ENTER, pero bueno... ¡A jugar!".center(100))
else:
    print("¡A jugar!".center(100),"\n")
    print("*"*100)

while True:
    
    categorias=["Deportes","Arte y Musica","Geografia","Espectaculo","Historia"]
    matriz=[[f"{categorias[0]}:","-","-","-","-"],[f"{categorias[1]}:","-","-","-","-"],[f"{categorias[2]}:","-","-","-","-"],[f"{categorias[3]}:","-","-","-","-"],[f"{categorias[4]}:","-","-","-","-"]]
    tupla=()
    diccionario={}
    cont=5
    puntos=0
    sumapuntos=0
    while cont > 0:
        print(" Las categorias disponibles son ".center(100,"*"))            
        print("*"*100)
        print("*"*3,"1.",categorias[0],"*"*5,"2.",categorias[1],"*"*5,"3.",categorias[2],"*"*5,"4.",categorias[3],"*"*5,"5.",categorias[4],"*"*3)
        print("*"*100)
        eleccion=filtrar_eleccion(categorias)       
        eleccion=int(eleccion)-1

        if categorias[eleccion].count("*") > 0:
            print("*"*100)
            print("*","Esta opcion ya no esta disponible".center(96),"*".rjust(0))
            print("*"*100)
        else:
            sumapuntos=Generar_preguntas(eleccion)
            vacio="*"*len(categorias[eleccion])
            categorias[eleccion]=vacio
            cont-=1
                
    print(f"\n"*10)
    print(("*"*(43+int(len(f"{sumar_matriz(matriz)}")))).center(100))
    print(f"**Felicidades, usted hizo: {sumar_matriz(matriz)} de 200 puntos**".center(100))
    print(("*"*(43+int(len(f"{sumar_matriz(matriz)}")))).center(100))
#    for cat in diccionario:
#        print(cat)#,diccionario[cat])
#    print(diccionario)
    
    ultima_opcion=verificar_ultima_opcion()
        
    if ultima_opcion == "reset":
        continue
    else:
        break
    
print(("*"*90).center(100))
print((f"MUCHAS GRACIAS POR JUGAR!!! :)").center(100," "))
print(("*"*90).center(100))
