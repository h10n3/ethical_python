#! /usr/bin/python3

from scapy.all import *

if __name__ == "__main__":
    src_ip = input("Source IP address:\n")
    dest_ip = input("Destination IP/Domain address:\n")
    ip_layer = IP(
        src=src_ip,
        dst=dest_ip
    )
    #print("IP Layer Information:\n"+ls(ip_layer.dst))
    icmp_req = ICMP(id=100)
    packet = ip_layer / icmp_req
    response = sr1(packet, iface="Wi-Fi")
    # to find/see available interfaces, write "ifconfig" command in Linux terminal
    # or "ipconfig" in windows command prompt window.
    if response:
        print("Ping response:\n" + response.show())
