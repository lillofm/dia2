'''def retrocontador(e):
    print("{},".format(e), end="")
    retrocontador(e-1)
    
retrocontador(10)'''
#estamos haciendo llamadas hasta el infinito

'''def retrocontador(e):
    print("{},".format(e), end="")
    if e==0:
        return
    retrocontador(e-1)
    
retrocontador(10)'''
#esta es una forma. S e==0 entonces te sales (return). Pero hay otra forma:

def retrocontador(e):
    print("{},".format(e), end="")
    if e > 0:
        
        retrocontador(e-1)
    
retrocontador(10)

#Si e esdistinto de 0 e vuelves a invocar a ti misma restandote 1
'''la condicion de salida es importante, si hubiera hecho con:
if e != 0 y en la shell pongon -1 me vulelva meter en bucle sin fin.
if e > = me va a poner -1 y se sale por que -1 es menor y sale'''

