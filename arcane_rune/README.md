# arcane_rune/main.py Usage Guide

This guide explains how to use the `main.py` script, which calculates the cost of leveling up arcane runes in a game, or determines the maximum level achievable with a given amount of resources.

## Prerequisites

- Python 3.x
- The script requires a data file named `detail_cost.txt` located in a `data` subdirectory. This file should contain the cost information for each rune level in the format:

  ```
  Level 1: Free
  Level 5: 5 Radiant Crystals + 100000 Zeny
  ...
  ```

## Running the Script

The script is executed from the command line with various arguments to specify the calculation mode and parameters.

```bash
python arcane_rune/main.py -m <mode> [options]
```

## Available Arguments

The script uses `argparse` for command-line argument parsing. Here's a breakdown of the available arguments:

### Required Arguments

- `-m`, `--mode`:  Specifies the calculation mode.  Must be either `cost` or `invest`.
    - `cost`: Calculates the total cost (Radiant Crystals and Zeny) to level up runes from a starting level to an ending level.
    - `invest`: Determines the maximum rune level achievable with a given amount of Radiant Crystals, starting from a specific level.

### Optional Arguments

- `-s`, `--start`: The starting level for the calculation. Defaults to 1.  Must be an integer between 1 and the maximum level defined in `detail_cost.txt`.
- `-e`, `--end`: The ending level for the calculation (used with `cost` mode). Defaults to the maximum level defined in `detail_cost.txt`. Must be an integer between 1 and the maximum level.
- `-r`, `--radiant`: The amount of Radiant Crystals available (used with `invest` mode). Defaults to 0.

## Examples

1. **Calculate the cost to level up from level 10 to 20:**

   ```bash
   python arcane_rune/main.py -m cost -s 10 -e 20
   ```
   **Output:**
   ```
   From level 10 to 20 need 15 Radiant Crystals and 1,200,000 zeny
   ```

2. **Calculate the cost to level up from level 1 to the maximum level:**

   ```bash
   python arcane_rune/main.py -m cost
   ```

3. **Determine the maximum level achievable from level 5 with 1000 Radiant Crystals:**

   ```bash
   python arcane_rune/main.py -m invest -s 5 -r 1000
   ```
   **Output:**
   ```
   From level 5 and you have 1000 Radiant Crystals, you can level up to 95 with cost 980 Radiant Crystals and 58,600,000 zeny
   ```

## Output

The script will print the results of the calculation to the console. The output format depends on the chosen mode:

- **`cost` mode:**  Prints the total Radiant Crystals and Zeny required to level up from the start level to the end level.
- **`invest` mode:** Prints the maximum level achievable with the given Radiant Crystals, the total Radiant Crystals spent, and the total Zeny spent.

If an error occurs (e.g., invalid level range, missing cost data), an error message will be printed.

## For Development/Testing
The `main` function can be imported and called with a list of arguments for testing purposes.
```python
from arcane_rune.main import main

# example
main(['-m', 'cost', '-s', '1', '-e', '10'])
```

## Notes

- The maximum level is determined dynamically based on the data in `detail_cost.txt`.
- Ensure that `detail_cost.txt` accurately reflects the cost information for your game or application.
- The script uses regular expressions to parse the cost data from `detail_cost.txt`. If the file format changes, the regular expressions in the script may need to be updated.
