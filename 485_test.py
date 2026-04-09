import serial
import time

# Configuración del puerto
PUERTO = 'COM5' 
BAUDIOS = 9600

try:
    with serial.Serial(PUERTO, BAUDIOS, timeout=1) as ser:
        print(f"--- Conectado con éxito a {PUERTO} ---")
        
        mensaje = b"HOLA 485"
        
        ser.write(mensaje)
        print(f"Enviando: {mensaje.decode()}")
        
        # Esperamos un poco para que los datos salgan físicamente
        time.sleep(0.1)
        
        print("Envío completado.")
        
except serial.SerialException as e:
    print(f"Error: No se pudo abrir el puerto. ¿Está siendo usado por otro programa? \n{e}")