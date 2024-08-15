#!/usr/bin/python3
import sys
import signal

def print_stats(total_size, status_codes):
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

# Initialize variables
total_size = 0
status_codes = {}

# Signal handler to catch keyboard interruption
def signal_handler(sig, frame):
    print_stats(total_size, status_codes)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Function to parse each line
def parse_line(line):
    parts = line.split()
    if len(parts) < 7:
        return None, None

    ip_address = parts[0]
    status_code = parts[-2]
    try:
        file_size = int(parts[-1])
    except ValueError:
        return None, None

    return status_code, file_size

# Read stdin line by line
try:
    line_count = 0
    for line in sys.stdin:
        status_code, file_size = parse_line(line)
        if status_code and file_size is not None:
            total_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
except Exception as e:
    sys.exit(1)

# Print final stats if the script ends normally
print_stats(total_size, status_codes)
