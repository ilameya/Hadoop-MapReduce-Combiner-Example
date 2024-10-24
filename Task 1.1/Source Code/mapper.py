# mapper.py
import sys
from collections import Counter
import re

def mapper():
    word_count = Counter()
    for line in sys.stdin:
        words = re.findall(r"\w+", line.lower())
        word_count.update(words)
    for word, count in word_count.items():
        print(f"{word}\t{count}")

if __name__ == "__main__":
    mapper()
