import dns.resolver

# Reading a list of specified domains from the file
with open('domain_list.txt', 'r') as file:
    domain_list=file.read().strip().split('\n')

# Resolve A records (IPv4 addresses)
try:
    for domain in domain_list:
        result = dns.resolver.resolve(domain, 'A')
        for ip in result:
            print("IP address: ", ip)
except Exception as e:
    print("Failed to resolve:", e)


