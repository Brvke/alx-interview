#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status_codes = {code: 0 for code in ["200", "301", "400", "401", "403", "404", "405", "500"]}

def print_stats():
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

# Signal handler to catch keyboard interruption
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Function to parse each line
def parse_line(line):
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = parts[-2]
        file_size = int(parts[-1])

        # Validate specific format
        if len(parts) >= 7 and parts[1] == '-' and parts[2].startswith('[') and parts[3].endswith(']') and parts[4].startswith('"GET') and parts[4].endswith('"'):
            return status_code, file_size
    except (IndexError, ValueError):
        return None, None
    return None, None

# Read stdin line by line
line_count = 0
try:
    for line in sys.stdin:
        status_code, file_size = parse_line(line)
        if status_code in status_codes and file_size is not None:
            total_size += file_size
            status_codes[status_code] += 1

            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats()
except Exception:
    sys.exit(1)

# Print final stats if the script ends normally
print_stats()
