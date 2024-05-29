import subprocess
import ipaddress

def ping_sweep(network):
    alive_hosts = []
    for ip in ipaddress.IPv4Network(network).hosts():
        result = subprocess.run(['ping', '-c', '1', '-W', '1', str(ip)], stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            alive_hosts.append(str(ip))
    return alive_hosts

def main():
    cidr = input("Input CIDR: ")
    alive_hosts = ping_sweep(cidr)
    print("Alive hosts:")
    for host in alive_hosts:
        print(host)

if __name__ == "__main__":
    main()