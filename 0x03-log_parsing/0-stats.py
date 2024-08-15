#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
line_count = 0

def print_stats():
    """Prints the total file size and the count of status codes in ascending order."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handles the CTRL+C signal to print stats before exiting."""
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Function to parse each line and validate the format
def parse_line(line):
    try:
        parts = line.split()
        if len(parts) < 7:
            return None, None

        ip_address = parts[0]
        dash = parts[1]
        date = parts[2] + " " + parts[3]
        method = parts[4]
        path = parts[5]
        protocol = parts[6]
        status_code = parts[-2]
        file_size = parts[-1]

        if dash != "-" or not date.startswith('[') or not date.endswith(']'):
            return None, None

        if method != '"GET' or path != "/projects/260" or protocol != 'HTTP/1.1"':
            return None, None

        # Convert and return the status code and file size if they are valid
        if status_code in status_codes:
            return status_code, int(file_size)
    except (IndexError, ValueError):
        return None, None

    return None, None

# Read stdin line by line
try:
    for line in sys.stdin:
        status_code, file_size = parse_line(line)
        if status_code and file_size is not None:
            # Update total size and count for the status code
            total_size += file_size
            status_codes[status_code] += 1
            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats()
except Exception:
    pass

# Print final stats if the script ends normally
print_stats()
