import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyperclip

# Este programa es un generador de contraseñas seguras.
class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Generador de Contraseñas Seguras")
        self.ventana1.geometry("450x250")
        self.ventana1.resizable(False, False)
        
        self.generar_interfaz()
        
        self.ventana1.mainloop()

    # Metodo que genera la interfaz de la aplicacion dividida en dos secciones
    def generar_interfaz(self):
        # Seccion 1: Configuracion de la contraseña
        frame_config = ttk.LabelFrame(self.ventana1, text= "Configuracion")
        frame_config.pack(padx= 10, pady= 10, fill= "x")
        ttk.Label(frame_config, text= "Longitud:").grid(column= 0, row= 0, padx= 5, pady= 5, sticky= "w")
        self.entry_longitud = ttk.Entry(frame_config, width= 5)
        self.entry_longitud.insert(0, "12")
        self.entry_longitud.grid(column= 1, row= 0, padx= 5, pady= 5, sticky= "w")
        self.var_mayus = tk.BooleanVar(value= True)
        self.var_numeros = tk.BooleanVar(value= True)
        self.var_simbolos = tk.BooleanVar(value= True)
        ttk.Checkbutton(frame_config, text= "Incluir mayúsculas", variable= self.var_mayus).grid(column= 0, row= 1, columnspan= 2, padx= 5, sticky= "w")
        ttk.Checkbutton(frame_config, text= "Incluir números", variable= self.var_numeros).grid(column= 0, row= 2, columnspan= 2, padx= 5, sticky= "w")
        ttk.Checkbutton(frame_config, text= "Incluir símbolos", variable= self.var_simbolos).grid(column= 0, row= 3, columnspan= 2, padx= 5, sticky= "w")
        ttk.Button(frame_config, text= "Generar", command= self.generar_contraseña).grid(column= 0, row= 4, columnspan= 2, pady= 10)
        
        # Seccion 2: Resultado y opcion de copiado
        frame_resultado = ttk.Frame(self.ventana1)
        frame_resultado.pack(padx= 10, pady= 5, fill= "x")
        self.entry_contraseña = ttk.Entry(frame_resultado, width= 30, state= "readonly", font= ("Arial", 12))
        self.entry_contraseña.pack(side= "left", padx= 5)
        ttk.Button(frame_resultado, text= "Copiar", command= self.copiar_al_portapapeles).pack(side= "right", padx= 5)

    # Metodo que genera la contraseña
    def generar_contraseña(self):
        try:
            longitud = int(self.entry_longitud.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido para la longitud.")
            return
        
        incluir_mayus = self.var_mayus.get()
        incluir_numeros = self.var_numeros.get()
        incluir_simbolos = self.var_simbolos.get()
        
        caracteres = string.ascii_lowercase
        if incluir_mayus:
            caracteres += string.ascii_uppercase
        if incluir_numeros:
            caracteres += string.digits
        if incluir_simbolos:
            caracteres += string.punctuation
        
        if longitud < 4:
            messagebox.showwarning("Advertencia", "La contraseña debe tener al menos 4 caracteres.")
            return
        
        contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
        
        self.entry_contraseña.config(state= "normal")
        self.entry_contraseña.delete(0, tk.END)
        self.entry_contraseña.insert(0, contraseña)
        self.entry_contraseña.config(state= "readonly")

    # Metodo que copia la contraseña al portapapeles
    def copiar_al_portapapeles(self):
        contraseña = self.entry_contraseña.get()
        if contraseña:
            pyperclip.copy(contraseña)
            messagebox.showinfo("Copiado", "Contraseña copiada al portapapeles.")


if __name__ == "__main__":
    Aplicacion()