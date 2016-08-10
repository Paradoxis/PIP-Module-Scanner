import os
import argparse

from scanner import Scanner, ScannerException


def main():
    """
    Main entry point of the scanner
    :return: void
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--out", help="Output results to a file instead of stdout", default=None)
    parser.add_argument("-p", "--path", help="Specifies the target directory to search in", default=os.getcwd())
    options = parser.parse_args()

    try:
        scanner = Scanner(path=options.path, output=options.out)
        scanner.run()
        scanner.output()
    except ScannerException as e:
        print ("[!] Error, %s" % e.message)
        exit(1)


if __name__ == '__main__':
    main()

