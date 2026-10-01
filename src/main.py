import dns.resolver

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
                print("IPv4 address:", ip)
        except Exception as e:
            print("Failed to resolve A records:", e)
    return

# Resolve AAAA records (IPv6 addresses)
def aaaa_record():
    for domain in domain_list():
        try:
            result = dns.resolver.resolve(domain, 'AAAA')
            for ip in result:
                print("IPv6 address:", ip)
        except Exception as e:
            print("Failed to resolve AAAA records:", e)
    return

record_type=input("Please enter the type of record: A, AAAA, NC, CNAME or ALL:\n")
if record_type=="A":
    a_record()
elif record_type=="AAAA":
    aaaa_record()