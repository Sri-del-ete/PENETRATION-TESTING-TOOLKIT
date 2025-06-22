import socket

def port_scan(target):
    print(f"[+] Scanning {target} for open ports (1-1024)...")
    for port in range(1, 1025):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            print(f"[OPEN] Port: {port}")
            s.close()
        except:
            pass
