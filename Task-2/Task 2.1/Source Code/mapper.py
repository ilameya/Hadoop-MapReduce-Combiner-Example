import sys

def mapper():
    for line in sys.stdin:
        parts = line.split()  # Assuming log file is space-separated
        if len(parts) > 9:  # Ensure there are enough fields
            try:
                # Try to convert the bytes_transferred field to an integer
                bytes_transferred = int(parts[9]) if parts[9] != '-' else 0
                print(f"1\t{bytes_transferred}")
            except (ValueError, IndexError) as e:
                # Log the error message to stderr if conversion or indexing fails
                sys.stderr.write(f"Error processing line: {line}\n")
                sys.stderr.write(f"Exception: {e}\n")

if __name__ == "__main__":
    mapper()
