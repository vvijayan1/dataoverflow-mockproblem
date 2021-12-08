# DO NOT MODIFY this script
from code.script import location_aggregation
from argparse import ArgumentParser
from tests.test import TestLocationAggregation
import os
import unittest
import sys

def file_check(file_path):
    if os.path.isfile(file_path):
        return file_path
    raise FileNotFoundError(f"File {file_path} is not found")


def main():
    parser = ArgumentParser(description="This script is a wrapper which runs/tests the location aggregation code")
    subparsers = parser.add_subparsers(help="sub-commands available", dest="mode")
    subparsers.required = True
    parser_run = subparsers.add_parser("run", help="Use this subcommand to run the program")
    parser_test = subparsers.add_parser("test", help="Use this subcommand to test the program")
    parser_run.add_argument("-i", "--input_files", required=True, nargs="+", type=file_check, help="TSV file paths to input files")
    parser_run.add_argument("-o", "--output_file", required=True, help="TSV file path to output aggregated file")
    args = parser.parse_args()
    if args.mode == "run":
        location_aggregation(args.input_files, args.output_file)
    else:
        suite = unittest.TestSuite()
        suite.addTests(unittest.makeSuite(TestLocationAggregation))
        test_runner = unittest.TextTestRunner(verbosity=2).run(suite)
        if not test_runner.wasSuccessful():
            sys.exit(2)


if __name__ == "__main__":
    main()
