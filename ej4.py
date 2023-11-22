#Hay n parejas sentadas en 2n asientos dispuestos en fila y quieren darse la mano.
#Las personas y los asientos están representados por un array de números enteros row
#donde row[i] contiene el ID de la persona sentada en el asiento. Las parejas están
#numeradas en orden, siendo la primera pareja (0,1), la segunda pareja (2,3), y así
#sucesivamente hasta que la última pareja sea (2n - 2, 2n - 1)
#Devuelve el número mínimo de intercambios para que cada pareja esté sentada una al lado
#de la otra . Un intercambio consiste en elegir a dos personas cualesquiera, luego se
#levantan y cambian de asiento

def minSwapsCouples(row):
    n = len(row)
    pos = [0] * n
    for i in range(n):
        pos[row[i]] = i
    ans = 0
    for i in range(0, n, 2):
        seat = row[i]
        if seat % 2 == 0:
            couple = seat + 1
        else:
            couple = seat - 1
        if row[i+1] != couple:
            j = pos[couple]
            row[i+1], row[j] = row[j], row[i+1]
            pos[row[j]] = j
            pos[row[i+1]] = i+1
            ans += 1
    return ans

entrada_usuario = input("Ingrese el array de parejas: ")
row = eval(entrada_usuario)
resultado = minSwapsCouples(row)
print(resultado)
