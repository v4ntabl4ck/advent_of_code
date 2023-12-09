import logging

from aocd.models import Puzzle
from aocd import submit
import re

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

def parse_input(data: object) -> object:
    splits = data.split("\n")
    logging.debug(f"Lines {splits}")
    return splits

def parse_games(games):
    parsed_games = []
    for game in games:
        game_id, game_data = game.split(": ", 1)
        sub_games = game_data.split("; ")
        parsed_games.append((game_id, sub_games))
    return parsed_games
def calc_color_total(parsed_games):
    possible_games = []
    limits = {'red': 12, 'green': 13, 'blue': 14}

    for game_id, sub_games in parsed_games:
        is_possible = True
        for sub_game in sub_games:
            color_count = re.findall(r'(\d+) (\w+)', sub_game)
            game_totals = {}
            for count, color in color_count:
                game_totals[color] = game_totals.get(color, 0) + int(count)
                if color in limits and game_totals[color] > limits[color]:
                    is_possible = False
                    break
            if not is_possible:
                break
        if is_possible:
            possible_games.append(int(game_id.split()[1]))
            logging.debug(f"Game {game_id} is possible")
    return sum(possible_games)

def calculate_minimum_cubes_and_power(parsed_games):
    total_power = 0
    for game_id, sub_games in parsed_games:
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}
        for sub_game in sub_games:
            current_cubes = {'red': 0, 'green': 0, 'blue': 0}
            color_count = re.findall(r'(\d+) (\w+)', sub_game)
            for count, color in color_count:
                current_cubes[color] += int(count)
            for color in min_cubes:
                min_cubes[color] = max(min_cubes[color], current_cubes[color])
        game_power = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']
        total_power += game_power
        logging.debug(f"Game: {game_id}, Min Cubes: {min_cubes}, Power: {game_power}")
    return total_power

if __name__ == "__main__":
    # get puzzle and parse data
    puzzle = Puzzle(year=2023, day=2)
    data = puzzle.input_data

    parsed_data = parse_input(data)
    parsed_games = parse_games(parsed_data)

    answer_a = calc_color_total(parsed_games)
    # part a:
    logging.info(f"answer part a: {answer_a}")
    #submit(answer_a, part="a", day=2, year=2023)

    # part b:
    answer_b = calculate_minimum_cubes_and_power(parsed_games)
    logging.info(f"answer part b: {answer_b}")
    #submit(answer_b, part="b", day=2, year=2023)