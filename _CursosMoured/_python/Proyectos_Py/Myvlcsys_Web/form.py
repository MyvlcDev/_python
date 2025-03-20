import tkinter as tk
from tkinter import messagebox

class TresEnRaya:
    def __init__(self, root):
        self.root = root
        self.root.title("Tres en Raya")
        self.jugador = "X"
        self.tablero = [""] * 9
        self.botones = []
        self.crear_interfaz()
    def crear_interfaz(self):
            for i in range(9):
                boton = tk.Button(self.root, text="", font=("Helvetica", 24), height=2, width=5, command=lambda i=i: self.hacer_movimiento(i))
                boton.grid(row=i // 3, column=i % 3)
                self.botones.append(boton)

def main():
    root = tk.Tk()
    tres_en_raya = TresEnRaya(root)
    root.mainloop()

if __name__ == '__main__':
    main()