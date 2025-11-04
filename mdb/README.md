 # mdb/main.py Usage Guide
 
 This guide explains how to use the `main.py` script, which calculates and compares damage outputs for different skills against various elemental targets.
 
 ## Prerequisites
 
 - Python 3.x
 - The `element.py` file (containing the `Element` and `ElementCoef` classes) must be in the same directory as `main.py`.
 
 ## Running the Script
 
 The script is executed from the command line, with the target element(s) provided as arguments.
 
 ```bash
 python main.py <element1> <element2> ...
 ```
 
 Replace `<element1>`, `<element2>`, etc. with the desired target elements.  Element names are case-insensitive.
 
 ## Available Arguments
 
 The script accepts the following element names as arguments:
 
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
 
 Additionally, you can use the special argument `ALL` to calculate damage outputs against all elements.
 
 ## Examples
 
 1. **Calculate damage against Fire element:**
 
    ```bash
    python main.py fire
    ```
 
 2. **Calculate damage against Water and Wind elements:**
 
    ```bash
    python main.py water wind
    ```
 
 3. **Calculate damage against all elements:**
 
    ```bash
    python main.py all
    ```
 
 ## Output
 
 The script will print a comparison of damage outputs for "Ronin Slash-Light", "Ronin SSFS", and "RM MDB" skills against the specified element(s).  The output includes:
 
 - Base damage multipliers.
 - Total damage over multiple ticks.
 - Damage per second (DPS) considering cooldowns.
 - Identification of the skill with the highest damage in each category.
 
 The calculations take into account:
 
 - Element coefficients based on the `ElementCoef.COEF_TABLE` in `element.py`.
 - An optional "LoV" ("Lord of Vein") bonus to element coefficients (default: `True`, configurable within the script).
 - Cooldown reduction (default: 26%, configurable within the script).
 - Skill-specific multipliers and tick counts (defined as constants in the script).
 - A dark MDB rune value (default: 89%, configurable within the script).
 - Enemy lvl armor from 1-4 (this was based on the latest of romel update)
 
 ## Notes
 
 - The script assumes the presence of a T5 weapon for RM MDB damage calculation.
 - The script's behavior can be customized by modifying the constants at the beginning of the `main.py` file (e.g., `LOV`, `CD_REDUCE`, `RM_MDB_RUNE_VALUE`, skill multipliers, and tick counts).
 - Ensure that the `element.py` file accurately reflects the desired element relationships and coefficients for correct damage calculations.
 - Thanks to @cremisi for the updated table for new armor lvl table