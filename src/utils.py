import importlib
import json
from datetime import date
from pathlib import Path

import requests

SOLVE_FUNCTION = "solve"
FIRST_OF_DECEMBER = date(2020, 12, 1)
ROOT_FOLDER = Path("../")
DATA_DIR = ROOT_FOLDER / "data"
INPUT_URL = "https://adventofcode.com/{0}/day/{1}/input"
COOKIE_FILE_PATH = ROOT_FOLDER / "cookie.json"

def get_file_name(day):
    return "day{0}".format(day)


def load_solver(solver):
    package = "{0}.{1}".format("solvers", solver)
    try:
        return importlib.import_module(package)
    except ImportError as e:
        print("Solver {0} has not been implemented yet: {1}".format(solver, e))


def fetch_input(day):
    solver_name = get_file_name(day)
    input_file_path = DATA_DIR / "{0}.txt".format(solver_name)
    if input_file_path.exists():
        with open(input_file_path) as file:
            return [line.strip() for line in file]
    else:
        print(download_input(day, input_file_path))
        print("No input file found for {0}".format(solver_name))


def download_input(day, input_file_path):
    url = INPUT_URL.format(FIRST_OF_DECEMBER.year, day)
    if not COOKIE_FILE_PATH.exists():
        return ValueError("Could not download input because of missing cookie file")
    with open(COOKIE_FILE_PATH) as cookie_file:
        response = requests.get(url=url, cookies=json.load(cookie_file))
        if response.ok:
            with open(input_file_path, "w") as input_file:
                input_file.writelines(response.text)
            with open(input_file_path, "r") as input_file:
                return [line.strip() for line in input_file]
        if response.status_code == 404:
            return ValueError("Input not available yet for day {0}".format(day))
        return ValueError("Failed to download input for day {0}.\nStatus code: {1} response: {2} "
                          .format(day, response.status_code, response.text))


def invoke_solver(day):
    solver_name = "day{0}".format(day)
    solver = load_solver(solver_name)
    if solver is not None:
        solve_function_exist = SOLVE_FUNCTION in dir(solver) and callable(getattr(solver, SOLVE_FUNCTION))
        if solve_function_exist:
            data = fetch_input(day)
            if data is not None:
                solver.solve(data)
        else:
            print("Solver '{0}' does not contain a '{1}' function.".format(solver_name, SOLVE_FUNCTION))


def get_latest_day():
    today = date.today()
    return today if today.year == 2020 and today.month == 12 else date(2020, 12, 24)
