from capturador import capturar_pacotes
from analisador import analisar_pacotes

if __name__ == '__main__':
    while True :
        pacotes = capturar_pacotes()
        analisar_pacotes(pacotes)
