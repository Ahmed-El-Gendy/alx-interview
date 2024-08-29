#!/usr/bin/python3
"""
Log parsing
"""

import sys
import re
import signal


regex = re.compile(
    r'^\d{1,3}(?:\.\d{1,3}){3} - \[.*?\] "GET /projects/260 HTTP/1\.1" '
    r'(\d{3}) (\d+)$'
)

status_counts = defaultdict(int)
total_file_size = 0
line_counter = 0


def print_statistics():
    """
    Helper function to display stats
    """
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_counts):
        print(f"{code}: {status_counts[code]}")


def handle_interrupt(sig, frame):
    """
    Signal handler for keyboard interruption
    """
    print("\nKeyboardInterrupt received. Printing statistics...")
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)


for line in sys.stdin:
    match = regex.match(line.strip())
    if match:
        line_counter += 1
        status_code, file_size = match.groups()
        try:
            file_size = int(file_size)
            status_code = int(status_code)
            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                status_counts[status_code] += 1
                total_file_size += file_size
        except ValueError:
            continue

    if line_counter % 10 == 0:
        print_statistics()
