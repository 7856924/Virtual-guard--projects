import socket
from IPy import IP

class PortScanner:
    open_ports = []
    software_versions = {}

    def _init_(self, target, port_num):
        self.target = target
        self.port_num = port_num

    def scan(self):
        for port in range(1, self.port_num + 1):
            self.scan_port(port)

    def check_ip(self):
        try:
            IP(self.target)
            return self.target
        except ValueError:
            return socket.gethostbyname(self.target)

    def scan_port(self, port):
        try:
            converted_ip = self.check_ip()
            sock = socket.socket()
            sock.settimeout(1)
            result = sock.connect_ex((converted_ip, port))
            if result == 0:
                self.open_ports.append(port)
                try:
                    banner = sock.recv(1024).decode().strip('\n').strip('\r')
                    self.software_versions[port] = banner
                except:
                    self.software_versions[port] = 'Unknown'
            sock.close()
        except Exception as e:
            print(f"[-] Error scanning port {port}: {e}")

def main():
    try:
        targets_ip = input('[+] * Enter Target To Scan For Vulnerable Open Ports: ')
        port_number = int(input('[+] * Enter Amount Of Ports You Want To Scan (500 - First 500 Ports): '))
        if port_number > 500:
            print("[-] Please enter a number less than or equal to 500.")
            return

        print('\n')

        target = PortScanner(targets_ip, port_number)
        target.scan()

        # Print open ports and software versions
        print('\n[+] Open Ports:')
        for port in target.open_ports:
            version = target.software_versions.get(port, 'Unknown')
            print(f"Port {port}: {version}")

    except ValueError as ve:
        print(f"[-] Invalid input: {ve}")
    except Exception as e:
        print(f"[-] An error occurred: {e}")

if __name__ == "_main_":
    main()