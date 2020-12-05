#!/usr/bin/env python3
import argparse

from utils import get_latest_day, invoke_solver, FIRST_OF_DECEMBER


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", metavar="d", type=int, nargs="+", dest="days",
                        default=list(range(FIRST_OF_DECEMBER.day, get_latest_day().day + 1)),
                        help="specify which day(s) solution should be printed for")
    parser.add_argument("-f", action="store_true", default=False, dest="fetch_resource",
                        help="flag for downloading the data from the advent of code web page for the given day(s)")
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()

    for day in args.days:
        print("--------------------")
        invoke_solver(day)
        print("--------------------")
        print()


if __name__ == "__main__":
    main()
