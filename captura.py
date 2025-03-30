import socket
import struct
import ipaddress

# Função para converter IP em uma lista de inteiros (octetos)
def ip_to_features(ip):
    return [int(octeto) for octeto in ip.split('.')]

def capturar_pacotes(interface='ens33'):
    # Criação do socket bruto para captura de pacotes Ethernet
    raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    raw_socket.bind((interface, 0))
    print(f"Aguardando pacotes na interface {interface}...")

    pacotes = []
    while True:
        # Recebe um pacote
        packet, addr = raw_socket.recvfrom(65535)
        pacotes.append(packet)
        # Limite de pacotes para exemplo; remova ou ajuste conforme necessário
        if len(pacotes) >= 10:
            break
    return pacotes

