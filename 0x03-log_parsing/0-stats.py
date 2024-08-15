#!/usr/bin/python3
"""A log parsing interview answer"""
import sys
import signal
from datetime import datetime


def check_ip(ip: str):
    """Returns true if IP is correct."""
    if ip is None:
        return False

    ip_list = ip.split('.')
    if len(ip_list) != 4:
        return False
    for ips in ip_list:
        try:
            if int(ips) < 1 or int(ips) > 255:
                return False
        except ValueError:
            return False
    return True


def check_date(year: str, time: str):
    """Returns true if date is in the correct format."""
    if year is None or time is None:
        return False

    date = year + ' ' + time
    date = date[1:-1]  # Correctly remove the brackets
    format = "%Y-%m-%d %H:%M:%S.%f"
    try:
        date_format = datetime.strptime(date, format)
    except ValueError:
        return False

    if date_format > datetime.now():
        return False

    return True


def check_code(code: str):
    """Checks if code is in correct format."""
    if code is None:
        return False

    code_list = [200, 301, 400, 401, 403, 404, 405, 500]

    try:
        code_no = int(code)
        if code_no not in code_list:
            return False
    except ValueError:
        return False

    return code_no


def check_size(size: str):
    """Checks if the size is in correct format."""
    if size is None:
        return False

    try:
        int_size = int(size)
    except ValueError:

        return False

    return int_size


def check_line(line: str):
    """Checks the input line for conformity."""
    line_list = line.split()

    # Check the number of arguments
    if len(line_list) != 9:
        return None

    # Check for proper IP address in IPv4 format
    if check_ip(line_list[0]) is False:
        return None

    # Check for correct character after IP address
    if line_list[1] != '-':
        return None

    # Check for correct date format
    if check_date(line_list[2], line_list[3]) is False:
        return None

    # Check for correct GET request
    get_request = line_list[4] + ' ' + line_list[5] + ' ' + line_list[6]
    if get_request != "\"GET /projects/260 HTTP/1.1\"":
        return None

    # Check for correct status code
    code = check_code(line_list[7])
    if code is False:
        return None

    # Check for correct size
    size = check_size(line_list[8])
    if size is False:
        return None

    # If all checks pass, return size and code
    return [code, size]


if __name__ == "__main__":
    line_count = 0
    size = 0
    code_dict = {200: 0, 301: 0, 400: 0, 401: 0,
                 403: 0, 404: 0, 405: 0, 500: 0}

    def myfunction():
        print('File size: {}'.format(size), flush=True)
        for key, values in sorted(code_dict.items()):
            if values != 0:
                print('{}: {}'.format(key, values), flush=True)

    def sigint_handler(signal, frame):
        myfunction()
        sys.exit(0)

    signal.signal(signal.SIGINT, sigint_handler)

    for line in sys.stdin:
        cline = check_line(line)

        if cline is None:
            continue

        line_count += 1
        size += cline[1]
        code_dict[cline[0]] += 1

        if line_count == 10:
            myfunction()
            line_count = 0

    myfunction()
