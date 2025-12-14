import argparse
import csv

from os.path import join,dirname
DETAIL_COST_FILE = join(dirname(__file__),"data/shard_cost.csv")
MAX_LEVEL = 10
MAX_QUALITY = 3

class Cost:
    quality = 0
    costs = [0]
    def __init__(self, quality, costs):
        self.quality = quality
        self.costs = costs

    def insert(self, level: int, value: int):
        self.costs[level-1] = value
    
    def total_cost(self, start_lvl:int, end_lvl:int) -> int:
        """Calculates the total cost for a range of levels."""
        if end_lvl <= start_lvl:
            raise ValueError("End level must be greater than start level.")
        elif start_lvl > MAX_LEVEL or end_lvl > MAX_LEVEL:
            raise ValueError(f"Level must be a number between 1 and {MAX_LEVEL}")
        elif start_lvl < 0 or end_lvl < 1:
            raise ValueError(f"Level must be a number between 0 and {MAX_LEVEL-1}")
        total = 0
        for i in range(start_lvl, end_lvl):
            total += self.costs[i]
        return total
    
    def invest(self, start_lvl: int, budget: int) -> tuple[int, int]:
        """Calculates the maximum level achievable with a given amount of budget."""
        if start_lvl >= MAX_LEVEL or start_lvl < 0:
            raise ValueError(f"Start level must be a number between 0 and {MAX_LEVEL-1}")
        elif budget < 0:
            raise ValueError(f"Budget must be a positive number")
        final_level = start_lvl
        for i in range(start_lvl, MAX_LEVEL):
            if self.costs[i] > budget:
                break    
            budget -= self.costs[i]
            final_level = i + 1
        return final_level, budget



def load_cost(path: str) -> list[Cost]:
    """Loads the cost data from the specified csv file."""
    cost_data:list[Cost] = []
    for q in range(0, MAX_QUALITY):
        cost_data.append(Cost(quality=q+1, costs=[0]*MAX_LEVEL))
    with open(path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not reader.fieldnames:
            return {}
        quality_col = reader.fieldnames[0]
        level_col = reader.fieldnames[1]
        cost_col = reader.fieldnames[2]
        for row in reader:
            c = cost_data[int(row[quality_col])-1]
            c.insert(int(row[level_col]), int(row[cost_col]))
            
    return cost_data
    

def main(args=None):
    costs = load_cost(DETAIL_COST_FILE)
    parser = argparse.ArgumentParser(description="Arcane rune Cost Calculator")
    parser.add_argument(
        "-m",
        "--mode",
        choices=["cost", "invest"],
        required=True,
        help="Calculation mode: 'cost' to calculate cost between levels, 'invest' to find max level with given Radiant Crystals.")
    parser.add_argument(
        "-s",
        "--start",
        type=int,
        help=f"start level, default 0 max {MAX_LEVEL-1}",
        default=0)
    parser.add_argument(
        "-e",
        "--end",
        type=int,
        help=f"end level, default {MAX_LEVEL}",
        default=MAX_LEVEL)
    parser.add_argument(
        "-b",
        "--budget",
        type=int,
        help="Amount of Budget you have. Used with 'invest' mode.",
        default=0
    )
    parser.add_argument(
        "-q",
        "--quality",
        choices=[1,2,3],
        type=int,
        required=True,
        help= "The quality of the inherit skill. Used with all mode. Active 7 slot = 3, Passive 4 slot = 2, Passive 3 slot = 1",
        default= 1
    )
    quality_text = ["Passive 3 slot", "Passive 4 slot", "Active 7 slot"] 

    parsed_args = parser.parse_args(args)

    quality = parsed_args.quality
    start = parsed_args.start

    print(f"with quality of inherit skill to be {quality_text[quality-1]}")

    if parsed_args.mode == "cost":
        end = parsed_args.end
        cost = costs[quality-1].total_cost(start, end)
        print(f"From level {start} to {end} need {cost}")
        
    elif parsed_args.mode == "invest":
        budget = parsed_args.budget
        level, leftover = costs[quality-1].invest(start, budget)
        print(f"From level {start} and you have {budget} budget, you can level up to {level} with leftover cost {leftover}")
    
    else:
        pass
    

if __name__ == '__main__':
    main()