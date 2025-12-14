# element_coef Module

This module provides the elemental data for the project, including the `Element` enum and the `ElementCoef` class, which contains the elemental damage coefficient table.

## Element Enum

The `Element` enum defines all the available elemental types:

- `FIRE`
- `WIND`
- `WATER`
- `EARTH`
- `HOLY`
- `DARK`
- `POISON`
- `GHOST`
- `NEUTRAL`
- `UNDEAD`

## ElementCoef Class

The `ElementCoef` class holds the elemental damage coefficients.

### COEF_TABLE

The `COEF_TABLE` is a dictionary that stores the damage coefficients between attacking and defending elements. The structure is as follows:

`COEF_TABLE[ATTACKING_ELEMENT][DEFENDING_ELEMENT] = [Lvl 1, Lvl 2, Lvl 3, Lvl 4]`

The list of four numbers represents the damage multiplier for four different levels of enemy armor.

### COEF_LoV

A constant `COEF_LoV` is also defined in this class, representing the "Lord of Vein" coefficient.

## Data Source

The data in `COEF_TABLE` is hardcoded in the `element.py` file. It was derived from the images located in the `img_coef` directory.

## Usage

This module is intended to be used as a library by other modules. Here's how you can import and use it:

```python
from element_coef.element import Element, ElementCoef

# Get the damage coefficient for a Fire attack against a level 4 Earth monster
coef = ElementCoef.COEF_TABLE[Element.FIRE][Element.EARTH][3] # Index 3 for level 4

print(f"Fire vs Earth (Lvl 4) coefficient: {coef}")
```
