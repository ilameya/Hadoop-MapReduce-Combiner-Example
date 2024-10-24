# reducer.py
import sys
from collections import Counter

def reducer():
    word_count = Counter()
    for line in sys.stdin:
        word, count = line.split("\t")
        word_count[word] += int(count)
    # Get top 100 most frequent words
    for word, count in word_count.most_common(100):
        print(f"{word}\t{count}")

if __name__ == "__main__":
    reducer()
