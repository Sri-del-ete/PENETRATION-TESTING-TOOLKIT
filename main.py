from port_scanner import port_scan
from brute_forcer import brute_force
from ping_sweep import ping_sweep

def show_menu():
    print("""
[1] Port Scanner
[2] Brute Force HTTP Login
[3] Ping Sweep (LAN Scanner)
[4] Exit
""")

while True:
    show_menu()
    choice = input("Choose module: ")

    if choice == "1":
        target = input("Enter IP/Domain: ")
        port_scan(target)

    elif choice == "2":
        url = input("Login URL: ")
        username = input("Username: ")
        passwords = ["1234", "admin123", "password", "letmein", "toor"]
        brute_force(url, username, passwords)

    elif choice == "3":
        base = input("Enter base IP (e.g., 192.168.1): ")
        ping_sweep(base)

    elif choice == "4":
        print("Exiting toolkit. Bye!")
        break

    else:
        print("Invalid choice. Try again.")
