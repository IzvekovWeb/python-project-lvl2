#!/usr/bin/env python
import argparse

def main():
    """Some documentation about gendiff"""

    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    print(args)

    gendiff()


if __name__ == '__main__':
    main()

def gendiff(first_file, second_file):
    """Compares two configuration files and shows a difference."""

