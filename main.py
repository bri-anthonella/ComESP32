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
    Break