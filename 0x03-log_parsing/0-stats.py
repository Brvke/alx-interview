#!/usr/bin/python3
"""A log parsing script"""

import sys
import signal
from datetime import datetime

def check_ip(ip: str):
    """ Returns True if the IP address is valid """
    ip_list = ip.split('.')
    if len(ip_list) != 4:
        return False
    for part in ip_list:
        try:
            if int(part) < 1 or int(part) > 255:
                return False
        except ValueError:
            return False
    return True

def check_date(year: str, time: str):
    """ Returns True if the date is in the correct format """
    try:
        date_str = f"{year} {time}".strip("[]")
        datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
        return True
    except ValueError:
        return False

def check_code(code: str):
    """ Returns the code if it's valid, False otherwise """
    valid_codes = {200, 301, 400, 401, 403, 404, 405, 500}
    try:
        code_no = int(code)
        return code_no if code_no in valid_codes else False
    except ValueError:
        return False

def check_size(size: str):
    """ Returns the size if it's a valid integer, False otherwise """
    try:
        return int(size)
    except ValueError:
        return False

def check_line(line: str):
    """ Validates the input line """
    line_list = line.split()

    if len(line_list) != 9:
        return None

    if not check_ip(line_list[0]):
        return None

    if line_list[1] != '-':
        return None

    if not check_date(line_list[2], line_list[3]):
        return None

    if f"{line_list[4]} {line_list[5]} {line_list[6]}" != "\"GET /projects/260 HTTP/1.1\"":
        return None

    code = check_code(line_list[7])
    if not code:
        return None

    size = check_size(line_list[8])
    if size is False:
        return None

    return [code, size]

def print_metrics(size, code_dict):
    """ Prints the accumulated metrics """
    print(f'File size: {size}', flush=True)
    for key, value in sorted(code_dict.items()):
        if value > 0:
            print(f'{key}: {value}', flush=True)

if __name__ == "__main__":
    line_count = 0
    total_size = 0
    code_dict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    def sigint_handler(sig, frame):
        print_metrics(total_size, code_dict)
        sys.exit(0)

    signal.signal(signal.SIGINT, sigint_handler)

    for line in sys.stdin:
        cline = check_line(line)

        if cline:
            line_count += 1
            total_size += cline[1]
            code_dict[cline[0]] += 1

        if line_count == 10:
            print_metrics(total_size, code_dict)
            line_count = 0

    print_metrics(total_size, code_dict)
