#!/usr/bin/env python
import sys
import re
from collections import defaultdict

# Mapper Function
def mapper():
    word_count = defaultdict(int)  # Local aggregation in the mapper
    for line in sys.stdin:
        # Tokenize each line into words (split by non-word characters)
        words = re.findall(r"\w+", line.lower())
        for word in words:
            word_count[word] += 1  # Count each word
    
    # Emit the word counts after local aggregation (combiner behavior)
    for word, count in word_count.items():
        print(f"{word}\t{count}")

if __name__ == "__main__":
    mapper()
