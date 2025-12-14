# inherit_skill/main.py Usage Guide

This guide explains how to use the `main.py` script, which calculates the cost of leveling up inherit skills, or determines the maximum level achievable with a given budget.

## Prerequisites

- Python 3.x
- The script requires a data file named `shard_cost.csv` located in a `data` subdirectory. This file should contain the cost information for each skill level and quality.

## Running the Script

The script is executed from the command line with various arguments to specify the calculation mode and parameters. It can be run as a module from the project root.

```bash
python -m inherit_skill.main -m <mode> [options]
```

## Available Arguments

The script uses `argparse` for command-line argument parsing. Here's a breakdown of the available arguments:

### Required Arguments

- `-m`, `--mode`: Specifies the calculation mode. Must be either `cost` or `invest`.
    - `cost`: Calculates the total cost to level up skills from a starting level to an ending level.
    - `invest`: Determines the maximum level achievable with a given budget, starting from a specific level.
- `-q`, `--quality`: The quality of the inherit skill.
    - `1`: Passive 3 slot
    - `2`: Passive 4 slot
    - `3`: Active 7 slot

### Optional Arguments

- `-s`, `--start`: The starting level for the calculation. Defaults to 0.
- `-e`, `--end`: The ending level for the calculation (used with `cost` mode). Defaults to 10.
- `-b`, `--budget`: The amount of budget you have (used with `invest` mode). Defaults to 0.

## Examples

1. **Calculate the cost to level up a quality 3 skill from level 0 to 10:**

   ```bash
   python -m inherit_skill.main -m cost -q 3 -s 0 -e 10
   ```

2. **Determine the maximum level achievable for a quality 1 skill from level 0 with a budget of 50000:**

   ```bash
   python -m inherit_skill.main -m invest -q 1 -s 0 -b 50000
   ```

## Output

The script will print the results of the calculation to the console. The output format depends on the chosen mode:

- **`cost` mode:** Prints the total cost required to level up from the start level to the end level.
- **`invest` mode:** Prints the maximum level achievable with the given budget and the leftover budget.

## For Development/Testing
The `main` function can be imported and called with a list of arguments for testing purposes.
```python
from inherit_skill.main import main

# example
main(['-m', 'cost', '-q', '3', '-s', '1', '-e', '10'])
```

## Notes
- The maximum level is defined as a constant `MAX_LEVEL` in the script.
- The cost data is loaded from `data/shard_cost.csv`.