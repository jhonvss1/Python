import tkinter as tk 
from random import randint
from time import sleep

def sortear_numero():
    label_resultado.config(text="Sorteando ... ")
    root.update()
    sleep(2)
    numero_sorteado = randint(0,20)
    label_resultado.config(text=f"O número sorteado foi {numero_sorteado} Parabéns!")

root = tk.Tk()
root.title("Sorteio de números")
root.geometry("300x200")

label_instruções = tk.Label(root, text="Clique no botão para sortear umnúmero entre 0 e 20.")
label_instruções.pack(pady=20)

botão_sorteio = tk.Button(root, text="Sortear", command=sortear_numero)
botão_sorteio.pack()

label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=20)

root.mainloop()