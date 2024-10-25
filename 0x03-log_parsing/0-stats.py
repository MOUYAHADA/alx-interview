#!/usr/bin/python3
"""
Log Parser Module

This module reads log entries from standard input, extracts relevant
information such as the total file size and the number of occurrences
of each HTTP status code, and prints this information to the standard
output. The log entries are expected to follow a specific format, which
is defined by a regular expression.

The module handles keyboard interrupts gracefully, allowing the user to stop
the log parsing and view the collected statistics at any time.

Usage:
    Run the script and pipe log data into it, for example:
    $ cat access.log | python3 log_parser.py
"""
import sys
import re
import signal
from typing import Dict


# Regular expression to match log lines
regex = re.compile(
    r'(\d{1,3}\.?){4}\s-\s$$\d{4}(-?\d{2}){2}\s(\d{2}:?){3}\.\d{6}$$\s'
    r'"GET\s\/projects\/260\sHTTP\/1\.1"\s(?P<status>\d{3})\s(?P<size>\d+)'
)

# Global variables to store total file size and lines by status code
total_file_size: int = 0
lines_by_status_code: Dict[str, int] = {}


def print_data() -> None:
    """Print the total file size and the number of lines by status code."""
    print(f'File size: {total_file_size}')
    # Printing number of lines by status code
    for key in sorted(lines_by_status_code):
        print(f'{key}: {lines_by_status_code[key]}')


def handle_interrupt(sig: int, frame) -> None:
    """Handle the interrupt signal and print the collected data."""
    print_data()


def parse_log() -> None:
    """Parse the log from standard input and collect statistics."""
    global total_file_size, lines_by_status_code

    line_count = 0
    signal.signal(signal.SIGINT, handle_interrupt)

    while True:
        try:
            line_count += 1
            line = sys.stdin.readline()
            if not line:
                break

            match = regex.match(line)
            if not match:
                continue

            total_file_size += int(match.group('size'))
            status_code = match.group('status')

            lines_by_status_code[status_code] \
                = lines_by_status_code.get(status_code, 0) + 1

            if line_count % 10 == 0:
                print_data()
        except KeyboardInterrupt:
            print_data()
            break
        except Exception as e:
            print(e)


if __name__ == '__main__':
    parse_log()
