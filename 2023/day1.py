import logging

from aocd.models import Puzzle
from aocd import submit
import re

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

def parse_input(data: object) -> object:
    splits = data.split("\n")
    return splits


def get_coordinates(splits):
    value = 0
    for line in splits:
        # Extract only the digits from the line
        get_vals = "".join([char for char in line if char.isdigit()])

        # Check if there are no digits, one digit, or multiple digits
        if len(get_vals) == 0:
            continue  # Skip lines with no digits
        elif len(get_vals) == 1:
            sum_value = int(get_vals * 2)  # Duplicate the digit if there's only one
        else:
            sum_value = int(get_vals[0] + get_vals[-1])  # Concatenate the first and last digit

        logging.debug(f"Line: {line}, Sum: {sum_value}")
        value += sum_value
    return value


def replace_with_number(line):
    number_map = {
        'one': 'one1one', 'two': 'two2two', 'three': 'three3three',
        'four': 'four4four', 'five': 'five5five', 'six': 'six6six',
        'seven': 'seven7seven', 'eight': 'eight8eight', 'nine': 'nine9nine'
    }

    for key, value in number_map.items():
        line = line.replace(key, value)

    return line


if __name__ == "__main__":
    # get puzzle and parse data
    puzzle = Puzzle(year=2023, day=1)
    data = puzzle.input_data

    parsed_data = parse_input(data)
    # print(f"original data {parsed_data}")
    answer_a = get_coordinates(parsed_data)

    # part a: submit coordinats from numbers
    logging.info(f"answer part a: {answer_a}")
    # submit(answer_a, part="a", day=1, year=2023)

    # test_data = parsed_data[:5]  # Adjust the slice as needed
    # test_replaced_data = [replace_with_number(line) for line in test_data]
    # logging.debug("Test Replaced Data:", test_replaced_data)
    # part b:
    replaced_data = [replace_with_number(line) for line in parsed_data]
    answer_b = get_coordinates(replaced_data)
    logging.info(f"answer part b: {answer_b}")
    #submit(answer_b, part="b", day=1, year=2023)
