#!/usr/bin/env python

from importlib.metadata import metadata, PackageNotFoundError
import sys


def main():
    check_file = sys.argv[1]
    with open(check_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line[0] == '!':
                expected = False
                pkg = line[1:]
            else:
                expected = True
                pkg = line
            try:
                metadata(pkg)
                found = True
            except PackageNotFoundError:
                found = False
            if expected and not found:
                print(f"Expected package {pkg} not found")
                exit(1)
            if not expected and found:
                print(f"Unexpected package {pkg} found")
                exit(1)


if __name__ == '__main__':
    main()