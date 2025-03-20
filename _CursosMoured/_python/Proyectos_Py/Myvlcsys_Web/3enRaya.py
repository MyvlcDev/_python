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

    def hacer_movimiento(self, indice):
        if self.tablero[indice] == "" and not self.verificar_ganador():
            self.tablero[indice] = self.jugador
            self.botones[indice]["text"] = self.jugador
            if self.verificar_ganador():
                messagebox.showinfo("Fin del juego", f"Ganador: Jugador {self.jugador}")
            elif "" not in self.tablero:
                messagebox.showinfo("Fin del juego", "Empate")
            else:
                self.jugador = "O" if self.jugador == "X" else "X"

    def verificar_ganador(self):
        combinaciones_ganadoras = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for a, b, c in combinaciones_ganadoras:
            if self.tablero[a] == self.tablero[b] == self.tablero[c] != "":
                return True
        return False

def main():
    root = tk.Tk()
    tres_en_raya = TresEnRaya(root)
    root.mainloop()

if __name__ == '__main__':
    main()