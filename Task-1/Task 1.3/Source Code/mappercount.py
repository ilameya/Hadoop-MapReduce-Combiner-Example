import sys
import re

def mapper():
    for line in sys.stdin:
        # Extract words from the line
        words = re.findall(r"\w+", line.lower())
        for word in words:
            # Output words of length 3 or 5
            if len(word) in [3, 5]:
                print(f"{word}\t1")

if __name__ == "__main__":
    mapper()
