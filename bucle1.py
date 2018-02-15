sad=int(input("Escriba un numero entero: "))
sad1=int(input("Escriba otro: "))
num=0
num1=0

if (sad>sad1):
    print("No run")
else:
    for n in range (sad,sad1+1):
        num1=n*2
        if n%2==0:
            print("Es par", n)
        else:
            print("No es par",n)
                
    
