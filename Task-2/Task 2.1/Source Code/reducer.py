import sys

def reducer():
    total_requests = 0
    total_bytes = 0
    for line in sys.stdin:
        requests, bytes_transferred = line.split("\t")
        total_requests += int(requests)
        total_bytes += int(bytes_transferred)
    
    # Convert bytes to GB (1 GB = 1024^3 bytes)
    total_gb = total_bytes / (1024 ** 3)
    cost_requests = total_requests * 0.001
    cost_data = total_gb * 0.08
    
    print(f"Total Requests: {total_requests}")
    print(f"Total Data Transferred: {total_gb:.2f} GB")
    print(f"Cost for Requests: {cost_requests:.3f} EUR")
    print(f"Cost for Data: {cost_data:.3f} EUR")

if __name__ == "__main__":
    reducer()
