#Se te proporciona un array de números enteros nums. Inicialmente te ubicas en el primer
#índice del array y cada elemento del array representa la longitud máxima de salto desde esa
#posición.
#Devuelve true si puedes llegar al último índice, o false en caso contrario .

def canJump(nums):
    n = len(nums)
    max_pos = 0
    for i in range(n):
        if i > max_pos:
            return False
        max_pos = max(max_pos, i + nums[i])
    return True

entrada_usuario = input("Ingrese el array de saltos: ")
nums = eval(entrada_usuario)
resultado = canJump(nums)
print(resultado)