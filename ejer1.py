#Se le proporciona una matriz entera height de longitud n. Hay n líneas verticales dibujadas
#de manera que los dos puntos finales de la i-ésima línea sean (i, 0) y (i, height[i]).
#Encuentre dos líneas que junto con el eje x formen un recipiente, de modo que el recipiente
#contenga la mayor cantidad de agua.
#Devuelve la cantidad máxima de agua que un recipiente puede almacenar



def max_area(altura):
    max_agua = 0
    izq = 0
    der = len(altura) - 1
    while izq < der:
        h= min(altura[izq], altura[der])
        max_agua = max(max_agua, h * (der - izq))
        if altura[izq] < altura[der]:
            izq += 1
        else:
            der -= 1
    return max_agua


altura_input = input()
altura = eval(altura_input)
print(max_area(altura))

