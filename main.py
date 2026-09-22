import dns.resolver

domain_list = [
    'www.google.com', 'www.example.com', 'www.bluewateryachtdetailing.com',
]

# Resolve A records (IPv4 addresses)
try:
    for domain in domain_list:
        result = dns.resolver.resolve(domain, 'A')
        for ip in result:
            print("IP address: ", ip)
except Exception as e:
    print("Failed to resolve:", e)


