from port_scanner import scan_ports
from brute_forcer import ssh_brute_force

def menu():
    print("""
===== Penetration Testing Toolkit =====
1. Port Scanner
2. SSH Brute Force
3. Exit
""")
    choice = input("Choose an option (1/2/3): ")
    return choice

while True:
    option = menu()
    if option == '1':
        ip = input("Enter Target IP: ")
        ports = list(range(20, 1025))
        scan_ports(ip, ports)
    elif option == '2':
        ip = input("Enter Target IP: ")
        user = input("Enter SSH Username: ")
        wordlist = input("Enter path to wordlist file: ")
        ssh_brute_force(ip, user, wordlist)
    elif option == '3':
        print("👋 Exiting Toolkit.")
        break
    else:
        print("⚠ Invalid option!")