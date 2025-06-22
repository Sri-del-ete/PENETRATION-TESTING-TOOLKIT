import os

def ping_sweep(base_ip):
    print(f"[+] Scanning active hosts in {base_ip}.0/24")
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        response = os.system(f"ping -c 1 -w 1 {ip} > /dev/null 2>&1")
        if response == 0:
            print(f"[ACTIVE] {ip}")
