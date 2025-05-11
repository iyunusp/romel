import regex
import argparse
from sys import argv

RADIANT_TXT = "radiant"
ZENY_TXT = "zeny"
DETAIL_COST_FILE = "data/detail_cost.txt"

# Compile regular expressions once at the module level
LEVEL_RE = regex.compile(r"Level (\d+):")
RADIANT_RE = regex.compile(r"(\d+) Radiant Crystals")
ZENY_RE = regex.compile(r"(\d+) Zeny")


def load_cost(path: str):
    """Loads the cost data from the specified file."""
    costs = {}
    with open(path, "r") as f:
        for line in f:
            level_match = LEVEL_RE.search(line)
            if level_match:
                level = int(level_match.group(1))
                radiant = 0
                zeny = 0

                radiant_match = RADIANT_RE.search(line)
                if radiant_match:
                    radiant = int(radiant_match.group(1))

                zeny_match = ZENY_RE.search(line)
                if zeny_match:
                    zeny = int(zeny_match.group(1))

                costs[level] = {RADIANT_TXT: radiant, ZENY_TXT: zeny}
    return costs


def validate_level(max_level: int):
    """Returns a function to validate level input."""

    def level_validator(level_str: str):
        try:
            level = int(level_str)
        except ValueError:
            raise argparse.ArgumentTypeError(
                f"Invalid level type, must be a number between 1 and {max_level}"
            )

        if not (1 <= level <= max_level):
            raise argparse.ArgumentTypeError(
                f"Level must be a number between 1 and {max_level}"
            )
        return level

    return level_validator


def calculate_cost_range(start: int, end: int, all_costs: dict):
    """Calculates the total cost for a range of levels."""
    if end <= start:
        raise ValueError("End level must be greater than start level.")

    radiant_cost = 0
    zeny_cost = 0
    for level in range(start, end):
        curr_cost = all_costs.get(level)
        if curr_cost is None:
            raise ValueError(f"Cost data not found for level {level}")
        radiant_cost += curr_cost[RADIANT_TXT]
        zeny_cost += curr_cost[ZENY_TXT]
    return radiant_cost, zeny_cost


def total_cost(start: int, end: int, all_costs: dict):
    """Calculates and prints the total cost for a range of levels."""
    try:
        radiant_cost, zeny_cost = calculate_cost_range(start, end, all_costs)
        print(
            f"From level {start} to {end} need {radiant_cost} holyglow and {zeny_cost:,} zeny"
        )
    except ValueError as e:
        print(e)


def invest_radiant(start: int, radiant: int, max_level: int, all_costs: dict):
    """Calculates the maximum level achievable with a given amount of radiant."""
    radiant_cost = 0
    zeny_cost = 0
    result = start
    for level in range(start, max_level):
        curr_cost = all_costs.get(level)
        if curr_cost is None:
            raise ValueError(f"Cost data not found for level {level}")
        radiant_cost += curr_cost[RADIANT_TXT]
        zeny_cost += curr_cost[ZENY_TXT]
        if radiant < radiant_cost:
            radiant_cost -= curr_cost[RADIANT_TXT]
            zeny_cost -= curr_cost[ZENY_TXT]
            result = level
            break
    print(
        f"From level {start} and you have {radiant} holyglow, you can level up to {result} with cost {radiant_cost} holyglow and {zeny_cost:,} zeny"
    )


if __name__ == "__main__":
    all_costs = load_cost(DETAIL_COST_FILE)
    MAX_LEVEL = len(all_costs)
    parser = argparse.ArgumentParser(description="Arcane rune Cost Calculator")
    parser.add_argument(
        "-m",
        "--mode",
        choices=["cost", "invest"],
        required=True,
        help="cost need start and end while invest need holyglow and start",
    )
    parser.add_argument(
        "-s",
        "--start",
        type=validate_level(MAX_LEVEL),
        help=f"start level, default 1 max {MAX_LEVEL}",
        default=1,
    )
    parser.add_argument(
        "-e",
        "--end",
        type=validate_level(MAX_LEVEL),
        help=f"end level, default {MAX_LEVEL} max {MAX_LEVEL}",
        default=MAX_LEVEL,
    )
    parser.add_argument(
        "-r", "--radiant", type=int, help="has radiant, default 0", default=0
    )
    args = parser.parse_args()

    mode = args.mode
    start = args.start
    end = args.end
    radiant = args.radiant

    if mode == "cost":
        total_cost(start=start, end=end, all_costs=all_costs)
    elif mode == "invest":
        invest_radiant(start=start, radiant=radiant, max_level=MAX_LEVEL, all_costs=all_costs)
