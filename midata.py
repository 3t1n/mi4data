#!/usr/bin/env python3
__author__ = "Tadeu Mansi"

import time
from datetime import datetime
from miband import miband  # classe responsavel pela conexao com a mi band
from bluepy.btle import BTLEDisconnectError

# Mac address e hash da mi band
MAC_ADD = 'F5:DC:A3:BC:E6:59'
AUTH_KEY = '397c6e9241c30267c202022fe60043f0'

if AUTH_KEY:
    AUTH_KEY = bytes.fromhex(AUTH_KEY)


def heart_logger(data):
    print('Batimento cardiaco BPM:', data)


# Needs Auth
def get_realtime():
    band.start_heart_rate_realtime(heart_measure_callback=heart_logger)
    input('Aperte Enter para iniciar')


if __name__ == "__main__":
    sucess = False
    while not sucess:
        try:
            if (AUTH_KEY):
                band = miband(MAC_ADD, AUTH_KEY, debug=True)
                sucess = band.initialize()
            else:
                band = miband(MAC_ADD, debug=True)
                sucess = True
            break
        except BTLEDisconnectError:
            print('[Falha] - Falha ao se conectar com sua Mi Band, tentando denovo em 3 segundos')
            time.sleep(3)
            continue
        except KeyboardInterrupt:
            print("\n Saindo")
            exit()
    get_realtime()
	# print('MI band Serial', band.get_serial())
    input('Aperte uma tecla para continuar')
