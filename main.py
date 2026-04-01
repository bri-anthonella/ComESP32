import tkinter as tk
from tkinter import Tk
import socket
import threding
import time


IP_ESP32 = "192.168.20.18"
PUERTO = 80

Class DatosSensor:
def__init__(self, valor);
self.valor = valor 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def conectar():
    try:
        sock.connect((IP_ESP32, PUERTO))
        print("Conectado al ESP32")
        threading.Thead(target=recibir_datos, daemon=True).start()
    except :
        print(f"Error al conectar")
def recibir_datos():
    while True:
        try:
            data = sock.recv(1024).decode().strip()
            if data:
                sensor = DatosSensor(int(data))
                progress['value'] = sensor.valor
                lbl_valor.config(text=f"Potenciometro: {sensor.valor}")
        except:
            break
def led_on(): sock.send(b'ON')
def led_off(): sock.send(b'OFF')

root = tk.Tk()
root.title("Control ESP32")
 
# Diseño con GRID
tk.Label(root, text="CONTROL DE DISPOSITIVO", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
# Potenciómetro (Fila 1)
lbl_valor = tk.Label(root, text="Potenciómetro: 0")
lbl_valor.grid(row=1, column=0, columnspan=2)
progress = ttk.Progressbar(root, length=200, maximum=4095)
progress.grid(row=2, column=0, columnspan=2, padx=20, pady=10)
# Botones LED (Fila 3)
tk.Button(root, text="Encender LED", command=led_on, bg="green", fg="white").grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Apagar LED", command=led_off, bg="red", fg="white").grid(row=3, column=1, padx=10, pady=10)
 
# Iniciar conexión al abrir
threading.Thread(target=conectar, daemon=True).start()
 
root.mainloop()
            