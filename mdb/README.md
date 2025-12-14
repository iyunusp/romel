# mdb/main.py Usage Guide

This guide explains how to use the `main.py` script, which calculates and compares damage outputs for different skills against various elemental targets.

## Prerequisites

- Python 3.x
- The script is part of a larger Python package and requires the `element_coef` module to be accessible.

## Running the Script

The script is executed from the command line, with the target element(s) provided as arguments.

```bash
python mdb/main.py [elements...]
```

By default (with no arguments), it will calculate for all elements.

## Arguments

The script uses `argparse` and accepts a list of elements as arguments.

- `elements`: One or more element names to calculate damage against. Element names are case-insensitive. If not provided, it defaults to `ALL`.

### Available Elements:

- `FIRE`
- `WATER`
- `EARTH`
- `WIND`
- `POISON`
- `HOLY`
- `DARK`
- `GHOST`
- `UNDEAD`
- `NEUTRAL`
- `ALL` (special argument to run for all elements)

## Examples

1. **Calculate damage against the Fire element:**

   ```bash
   python mdb/main.py fire
   ```

2. **Calculate damage against Water and Wind elements:**

   ```bash
   python mdb/main.py water wind
   ```

3. **Calculate damage against all elements:**

   ```bash
   python mdb/main.py
   ```
   or
   ```bash
   python mdb/main.py ALL
   ```

## Output

The script prints a comparison of damage outputs for "Ronin Slash-Light", "Ronin SSFS", and "RM MDB" skills against the specified element(s). The output includes:
- Base damage multipliers.
- Total damage over multiple ticks.
- Damage per second (DPS) considering cooldowns.
- The winning skill for each category.

The calculations are based on several configurable parameters within the `MdbCalculator` class.

## Configuration

To customize the calculations, you can modify the attributes of the `MdbCalculator` class within `mdb/main.py`. These are located in the `__init__` method of the class.

- `RM_MDB_RUNE_VALUE`: The value of the Dark MDB rune.
- `RONIN_SSFS_SKILL_MULTIPLIER`: The skill multiplier for Ronin SSFS.
- `RONIN_SLASH_TICK`, `RONIN_SSFS_TICK`, `RM_MDB_TICK`: The number of ticks for each skill.
- `RONIN_CD`, `RM_MDB_CD`: The cooldown for the skills.
- `ENEMY_LVL_ARMOR`: The enemy's armor level (from 1 to 4).
- `LOV`: Boolean to indicate if Lord of Vein is used.
- `CD_REDUCE`: The cooldown reduction percentage.

## For Development/Testing

The `main` function can be imported and called with a list of arguments. You can also import the `MdbCalculator` class and use it directly.

```python
from mdb.main import main, MdbCalculator
from element_coef import Element, ElementCoef

# Example of calling main
main(['fire', 'water'])

# Example of using MdbCalculator directly
calculator = MdbCalculator(Element, ElementCoef)
calculator.run_calculations(['holy'])
```

## Notes
- The script assumes the presence of a T5 weapon for RM MDB damage calculation.
- Thanks to @cremisi for the updated table for the new armor level table.