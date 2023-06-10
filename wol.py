#!/usr/bin/env python3

import argparse
from wakeonlan import send_magic_packet

def send_wol_packet(mac_address, broadcast_address):
    try:
        send_magic_packet(mac_address, ip_address=broadcast_address)
        print("Pacchetto WOL inviato con successo!")
    except Exception as e:
        print("Errore durante l'invio del pacchetto WOL:", str(e))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tool per inviare pacchetti Wake-on-LAN")
    parser.add_argument("mac_address", help="Indirizzo MAC del dispositivo di destinazione")
    parser.add_argument("-b", "--broadcast", default="255.255.255.255", help="Indirizzo di broadcast (default: 255.255.255.255)")
    args = parser.parse_args()

    send_wol_packet(args.mac_address, args.broadcast)
