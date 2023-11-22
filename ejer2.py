
entrada_usuario = input("Ingrese el array de hambre: ")
hunger = eval(entrada_usuario)

def min_caramelos(hunger):
    n = len(hunger)
    caramelos = [1] * n 

    for i in range(1, n):
        if hunger[i] > hunger[i-1]:
            caramelos[i] = caramelos[i-1] + 1

    for i in range(n-2, -1, -1):
        if hunger[i] > hunger[i+1]:
            caramelos[i] = max(caramelos[i], caramelos[i+1] + 1)

    return sum(caramelos)

resultado = min_caramelos(hunger)
print("Cantidad mínima de caramelos:", resultado)
