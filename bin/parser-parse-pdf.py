#!/usr/bin/env python3

import argparse
import logging
import os
logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO').upper(), format='[%(levelname)s] %(asctime)s\t%(message)s')


from hipisejm.stenparser.sejm_parser import SejmParser


def parse_arguments():
    """parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Parses stenograms from PDF files from X Sejm RP. Available on: https://www.sejm.gov.pl/sejm10.nsf/stenogramy.xsp\n\n'
        + 'Usage example:\n'
        + '  ./parser-parse-pdf.py -i resources/test_data/01_j_ksiazka.pdf -o parsed.xml',
        formatter_class=argparse.RawTextHelpFormatter
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

    parser = SejmParser()
    parser.parse_file(args.input)
    # TODO


main()
