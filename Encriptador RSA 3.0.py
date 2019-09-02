import tkinter as tk
def encriptar():
    palabra=str(campo1.get())
    lista=list(palabra)
    asciis=[]
    for i in range(0,len(lista)):
        result1.set(lista)
        asciis.append(ord(lista[i]))
        result2.set(asciis)

    print("Para p,q y n ingrese un número primo.")
    c=0
    while c<1:
        p=int(campo2.get())
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
        q=int(campo3.get())
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
        n=int(campo4.get())
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
        result3.set(Ve)

    for i in range(0,len(Ve)):
        Vc=(Ve[i]**s)%z
        Vd.append(chr(Vc))
        result4.set(Vd)

marco = tk.Tk()
marco.title("Encriptador RSA")
marco.geometry('600x600')
marco.configure (background = '#fafad2')

result1=tk.StringVar()
result2=tk.StringVar()
result3=tk.StringVar()
result4=tk.StringVar()


l1=tk.Label(marco, text="Palabra a encriptar: ").grid(row=0)
l2=tk.Label(marco, text="p: ").grid(row=1)
l3=tk.Label(marco, text="q: ").grid(row=2)
l4=tk.Label(marco, text="n: ").grid(row=3)
l5=tk.Label(marco, textvariable=result1).grid(row=4,column=0)
l6=tk.Label(marco, textvariable=result2).grid(row=5,column=0)
l7=tk.Label(marco, textvariable=result3).grid(row=6,column=0)
l8=tk.Label(marco, textvariable=result4).grid(row=7,column=0)

campo1=tk.Entry(marco)
campo2=tk.Entry(marco)
campo3=tk.Entry(marco)
campo4=tk.Entry(marco)

campo1.grid(row=0,column=1)
campo2.grid(row=1,column=1)
campo3.grid(row=2,column=1)
campo4.grid(row=3,column=1)

tk.Button(marco, text="Encriptar",command=encriptar).grid(row=9, column=5,sticky=tk.W,pady=4)

marco.mainloop()