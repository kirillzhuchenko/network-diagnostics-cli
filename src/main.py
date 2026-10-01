import dns.resolver
import socket

PORT=443

def domain_list():
# Reading a list of specified domains from the file
    with open('domain_list.txt', 'r') as file:
        domain_list=file.read().strip().split('\n')
    return domain_list


# Resolve A records (IPv4 addresses)
def a_record():
    for domain in domain_list():
        try:
            result = dns.resolver.resolve(domain, 'A')
            for ip in result:
                print(f"IPv4 address for {domain}:", ip)
        except Exception as e:
            print("Failed to resolve A records:", e)
    return

def check_port():
    for domain in domain_list():
        try:
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            result = sock.connect_ex((domain, PORT))
            sock.close()
            if result == 0:
                    print(f"Port {PORT} on {domain} is OPEN.")
            else:
                print(f"Port {PORT} on {domain} is CLOSED (Error code: {result}).")
        except Exception as e:
            print(f"Failed to connect to {domain}:", e)
a_record()
check_port()
