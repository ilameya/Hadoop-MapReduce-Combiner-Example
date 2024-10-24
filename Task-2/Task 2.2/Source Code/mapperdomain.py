import sys
import re

def mapper():
    for line in sys.stdin:
        parts = line.split()
        
        # Check if there are sufficient parts in the line
        if not parts:
            continue  # Skip empty lines
        
        client = parts[0]  # Assuming client name or IP is the first field
        
        # Ignore lines with only IP addresses
        if not re.match(r'\d+\.\d+\.\d+\.\d+', client):
            # Check if client has at least 2 parts for domain extraction
            domain_parts = client.split('.')
            if len(domain_parts) >= 2:
                domain = '.'.join(domain_parts[-2:])  # Join the last two parts for domain
                print(f"{domain}\t1")
            else:
                # If not enough parts, log an error to stderr
                sys.stderr.write(f"Invalid domain format: {client}\n")
        else:
            # If needed, log or handle IP addresses here
            # sys.stderr.write(f"IP address detected, ignoring: {client}\n")
            continue  # Skip IP addresses

if __name__ == "__main__":
    mapper()
