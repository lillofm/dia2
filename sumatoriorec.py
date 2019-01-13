def sumatorio(n):
    if n > 0:
        return n + sumatorio(n-1)
    else:
        return 0

print(sumatorio(4))
#tenemos que retornar un 0 porque si no va a retornar un None y va a cascar, porque a un numero nole pedes sumar un None