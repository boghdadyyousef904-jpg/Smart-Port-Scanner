#!/usr/bin/env python3 """ Smart Port Scanner & Cybersecurity Utility Author: Yousef Boghdady Description: A simple network port checking tool with structured output for security assessments. """
import socket import sys from datetime import datetime
def scan_target(target_host, ports): print("-" * 50) print(f"Scanning target: {target_host}") print(f"Time started: {str(datetime.now())}") print("-" * 50)
try:
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target_host, port))
        if result == 0:
            print(f"[+] Port {port}: OPEN")
        else:
            print(f"[-] Port {port}: CLOSED")
        s.close()
        
except KeyboardInterrupt:
    print("\nExiting script. Stay secure!")
    sys.exit()
except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()
except socket.error:
    print("\nCould not connect to server.")
    sys.exit()
if name == "main": target = "127.0.0.1" default_ports = [21, 22, 80, 443, 8080] scan_target(target, default_ports)
