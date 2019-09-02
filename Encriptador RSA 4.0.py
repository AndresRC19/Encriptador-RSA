import tkinter as tk

def cerrar():
    marco.destroy()

def encriptar():
    palabra=str(campo1.get())
    lista=list(palabra)
    asciis=[]
    for i in range(0,len(lista)):
        result1.set(lista)
        asciis.append(ord(lista[i]))
        result2.set(asciis)
    p=int(campo2.get())
    q=int(campo3.get())
    n=int(campo4.get())
 
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
    
    result4.set(lista)

marco = tk.Tk()
marco.title("Encriptador RSA")
marco.geometry('600x600')
marco.configure (background = '#fafad2')

result1=tk.StringVar()
result2=tk.StringVar()
result3=tk.StringVar()
result4=tk.StringVar()


l1=tk.Label(marco, text="Palabra a encriptar: ").grid(row=0,column=0)
l2=tk.Label(marco, text="p: ").grid(row=1,column=0)
l3=tk.Label(marco, text="q: ").grid(row=2,column=0)
l4=tk.Label(marco, text="n: ").grid(row=3,column=0)
l4=tk.Label(marco, text="Palabra a encriptar: ").grid(row=4,column=0)
l5=tk.Label(marco, textvariable=result1).grid(row=5,column=0)
l4=tk.Label(marco, text="Asciis correspondientes: ").grid(row=6,column=0)
l6=tk.Label(marco, textvariable=result2).grid(row=7,column=0)
l4=tk.Label(marco, text="Números de encriptación: ").grid(row=8,column=0)
l7=tk.Label(marco, textvariable=result3).grid(row=9,column=0)
l4=tk.Label(marco, text="Desencriptación de los números: ").grid(row=10,column=0)
l8=tk.Label(marco, textvariable=result4).grid(row=11,column=0)

campo1=tk.Entry(marco)
campo2=tk.Entry(marco)
campo3=tk.Entry(marco)
campo4=tk.Entry(marco)

campo1.grid(row=0,column=1,sticky=tk.N,pady=4)
campo2.grid(row=1,column=1,sticky=tk.N,pady=4)
campo3.grid(row=2,column=1,sticky=tk.N,pady=4)
campo4.grid(row=3,column=1,sticky=tk.N,pady=4)

tk.Button(marco, text="Encriptar",command=encriptar).grid(row=12, column=5,sticky=tk.N,pady=4)
tk.Button(marco, text="Cerrar",command=cerrar).grid(row=13, column=5,sticky=tk.N,pady=4)

marco.mainloop()