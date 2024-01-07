#!/usr/bin/env python3

import argparse
import logging
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(asctime)s\t%(message)s')


def parse_arguments():
    """parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Parses stenograms from PDF files from X Sejm RP. Available on: https://www.sejm.gov.pl/sejm10.nsf/stenogramy.xsp'
    )

    parser.add_argument(
        '--input', '-i',
        required=True,
        help='Filepath to PDF file to parse.')

    parser.add_argument(
        '--output', '-o',
        required=True,
        help='Filepath to XML file to save the parsed data.')

    args = parser.parse_args()

    return args


def main():
    args = parse_arguments()


main()
