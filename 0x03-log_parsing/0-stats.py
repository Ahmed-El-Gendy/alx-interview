#!/usr/bin/python3
"""
Log parsing
"""

import sys
import re
from collections import defaultdict

def display_statistics(file_size: int, code_frequency: defaultdict) -> None:
    """
    Displays the statistics of the log data.
    """
    print(f"File size: {file_size}")
    for code in sorted(code_frequency):
        count = code_frequency[code]
        if count > 0:
            print(f"{code}: {count}")

def main():
    regex = re.compile(
        r'^\d{1,3}(?:\.\d{1,3}){3} - \[.*?\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
    )

    line_count = 0
    file_size = 0
    code_frequency = defaultdict(int)

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if match:
                line_count += 1
                status_code, size_str = match.groups()
                size = int(size_str)

                file_size += size
                code_frequency[status_code] += 1

                if line_count % 10 == 0:
                    display_statistics(file_size, code_frequency)
    except BrokenPipeError:
        pass
    finally:
        display_statistics(file_size, code_frequency)

if __name__ == "__main__":
    main()
