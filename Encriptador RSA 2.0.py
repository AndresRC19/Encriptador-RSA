import tkinter as tk

print("Bienvenido al encriptador RSA.")
palabra=str(input("Digite la palabra que desea encriptar: "))
lista=list(palabra)
asciis=[]
for i in range(0,len(lista)):
    print(f"{lista[i]}= ",(ord(lista[i])))
    asciis.append(ord(lista[i]))
print(asciis)

print("Para p,q y n ingrese un número primo.")
c=0
while c<1:
    p=int(input("p = "))
    cont=0
    if p<23:
        print("El número debe ser igual o mayor a 23")
        continue
    elif p>=23:
        for i in range(1,p):
            d=p%i
            if d==0:
                cont=cont+1
        if cont==1:
            g=0
        else:
            g=1
    if g==1:
        print("El número en p no es primo o igual/mayor a 23")
        continue
    elif g==0:
        c=c+1
c=0
while c<1:
    q=int(input("q = "))
    cont=0
    if q<23:
        print("El número debe ser igual o mayor a 23")
        continue
    elif q>=23:
        for i in range(1,q):
            d=q%i
            if d==0:
                cont=cont+1
        if cont==1:
            g=0
        else:
            g=1
    if g==1:
        print("El número en q no es primo o igual/mayor a 23")
        continue
    elif g==0:
        c=c+1
c=0
while c<1:
    n=int(input("n = "))
    cont=0
    if n<23:
        print("El número debe ser igual o mayor a 23")
        continue
    elif n>=23:
        for i in range(1,n):
            d=n%i
            if d==0:
                cont=cont+1
        if cont==1:
            g=0
        else:
            g=1
    if g==1:
        print("El número en n no es primo o igual/mayor a 23")
        continue
    elif g==0:
        c=c+1
fi=(p-1)*(q-1)
z=p*q
s=0
while True:
    (n*s)%fi!=1
    s=s+1
    if (n*s)%fi==1:
        break
Ve=[]
Vd=[]
for i in range(0,len(asciis)):
    Va=(asciis[i]**n)%z
    Ve.append(Va)
    print(f"{lista[i]} = ",Ve[i])

for i in range(0,len(Ve)):
    Vc=(Ve[i]**s)%z
    Vd.append(Vc)
    print(f"{Ve[i]} = ",chr(Vd[i]))
