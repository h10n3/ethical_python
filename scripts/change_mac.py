#! usr/bin/python3

import subprocess

if __name__ == "__main__":

    interface = "eth0"
    new_mac = input("[?] What is the new MAC address?:\n[!] Format: xx:xx:xx:xx:xx:xx\n")
    print("[+] MAC address will be changed with", new_mac, "... \n[+} Shutting down the interface...")
    subprocess.run(["ifconfig", "eth0", "down"])
    print("[+] Changing the interface hw address of ", interface, "to ", new_mac)
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    print("[+] MAC address changed to ", new_mac, "\n[+] Turning on the interface...")
    subprocess.run(["ifconfig", interface, "up"])
    print("[+] Network interface turned on")
