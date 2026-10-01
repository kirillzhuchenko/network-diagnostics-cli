# Network Diagnostics CLI
This is project is a simple Python script that takes a list of domains and for each on of them does the following:
    Resolves DNS and reports the IP address
    Checks if the port 433 is open
    Fetches SSL certificate and reports status code + latency
    Outputs a clean health report pass/fair per domain

The script reads the domain_list.txt document but can accept a simple list if needed.
