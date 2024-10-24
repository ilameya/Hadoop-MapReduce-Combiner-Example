import sys
from collections import Counter

def reducer():
    domain_count = Counter()
    for line in sys.stdin:
        domain, count = line.split("\t")
        domain_count[domain] += int(count)
    
    # Output the 5 most popular domains
    for domain, count in domain_count.most_common(5):
        print(f"{domain}\t{count}")

if __name__ == "__main__":
    reducer()
