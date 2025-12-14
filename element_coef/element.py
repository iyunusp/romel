from enum import Enum


class Element(Enum):
    """Represents the different elemental types."""

    FIRE = "FIRE"
    WIND = "WIND"
    WATER = "WATER"
    EARTH = "EARTH"
    HOLY = "HOLY"
    DARK = "DARK"
    POISON = "POISON"
    GHOST = "GHOST"
    NEUTRAL = "NEUTRAL"
    UNDEAD = "UNDEAD"


class ElementCoef:
    """Represents the elemental coefficient table."""

    COEF_LoV = 0.15
    # COEF_TABLE[ATTACKING_ELEMENT][DEFENDING_ELEMENT] = [Lvl 1, Lvl 2, Lvl 3, Lvl 4]
    # Data is populated directly from the provided images (lvl-1.jpg, lvl-2.jpg, lvl-3.jpg, lvl-4.jpg)
    # Rows = Attacking Element (based on image row), Cols = Defending Element
    #
    # Image Row Mapping:
    # Row 1: WIND, Row 2: EARTH, Row 3: WATER, Row 4: FIRE, Row 5: NEUTRAL,
    # Row 6: HOLY, Row 7: DARK, Row 8: POISON, Row 9: UNDEAD, Row 10: GHOST
    COEF_TABLE = {
        # Attacker: FIRE (Image Row 4)
        Element.FIRE: {
            Element.FIRE: [0.25, 0.00, 0.000, 0.00],
            Element.WIND: [1.00, 0.75, 0.625, 0.50],
            Element.WATER: [0.50, 0.25, 0.125, 0.00],
            Element.EARTH: [2.00, 1.75, 1.625, 1.50],
            Element.HOLY: [0.75, 0.50, 0.375, 0.25],
            Element.DARK: [1.00, 0.75, 0.625, 0.50],
            Element.POISON: [0.75, 0.50, 0.375, 0.25],
            Element.GHOST: [1.00, 0.75, 0.625, 0.50],
            Element.NEUTRAL: [1.00, 0.75, 0.625, 0.50],
            Element.UNDEAD: [2.00, 1.75, 1.625, 1.50],
        },
        # Attacker: WIND (Image Row 1)
        Element.WIND: {
            Element.FIRE: [1.00, 0.75, 0.625, 0.50],
            Element.WIND: [0.25, 0.00, 0.000, 0.00],
            Element.WATER: [2.00, 1.75, 1.625, 1.50],
            Element.EARTH: [0.50, 0.25, 0.125, 0.00],
            Element.HOLY: [0.75, 0.50, 0.375, 0.25],
            Element.DARK: [1.00, 0.75, 0.625, 0.50],
            Element.POISON: [0.75, 0.50, 0.375, 0.25],
            Element.GHOST: [1.00, 0.75, 0.625, 0.50],
            Element.NEUTRAL: [1.00, 0.75, 0.625, 0.50],
            Element.UNDEAD: [1.00, 0.75, 0.625, 0.50],
        },
        # Attacker: WATER (Image Row 3)
        Element.WATER: {
            Element.FIRE: [2.00, 1.75, 1.625, 1.50],
            Element.WIND: [0.50, 0.25, 0.125, 0.00],
            Element.WATER: [0.25, 0.00, 0.000, 0.00],
            Element.EARTH: [1.00, 0.75, 0.625, 0.50],
            Element.HOLY: [0.75, 0.50, 0.375, 0.25],
            Element.DARK: [1.00, 0.75, 0.625, 0.50],
            Element.POISON: [0.75, 0.50, 0.375, 0.25],
            Element.GHOST: [1.00, 0.75, 0.625, 0.50],
            Element.NEUTRAL: [1.00, 0.75, 0.625, 0.50],
            Element.UNDEAD: [1.50, 1.25, 1.125, 1.00],
        },
        # Attacker: EARTH (Image Row 2)
        Element.EARTH: {
            Element.FIRE: [0.50, 0.25, 0.125, 0.00],
            Element.WIND: [2.00, 1.75, 1.625, 1.50],
            Element.WATER: [1.00, 0.75, 0.625, 0.50],
            Element.EARTH: [0.25, 0.00, 0.000, 0.00],
            Element.HOLY: [0.75, 0.50, 0.375, 0.25],
            Element.DARK: [1.00, 0.75, 0.625, 0.50],
            Element.POISON: [0.75, 0.50, 0.375, 0.25],
            Element.GHOST: [1.00, 0.75, 0.625, 0.50],
            Element.NEUTRAL: [1.00, 0.75, 0.625, 0.50],
            Element.UNDEAD: [1.00, 0.75, 0.625, 0.50],
        },
        # Attacker: HOLY (Image Row 6)
        Element.HOLY: {
            Element.FIRE: [1.00, 0.75, 0.625, 0.50],
            Element.WIND: [1.00, 0.75, 0.625, 0.50],
            Element.WATER: [1.00, 0.75, 0.625, 0.50],
            Element.EARTH: [1.00, 0.75, 0.625, 0.50],
            Element.HOLY: [0.25, 0.00, 0.000, 0.00],
            Element.DARK: [2.00, 1.75, 1.625, 1.50],
            Element.POISON: [1.25, 1.00, 0.875, 0.75],
            Element.GHOST: [1.00, 0.75, 0.625, 0.50],
            Element.NEUTRAL: [1.00, 0.75, 0.625, 0.50],
            Element.UNDEAD: [2.00, 1.75, 1.625, 1.50],
        },
        # Attacker: DARK (Image Row 7)
        Element.DARK: {
            Element.FIRE: [1.00, 0.75, 0.625, 0.50],
            Element.WIND: [1.00, 0.75, 0.625, 0.50],
            Element.WATER: [1.00, 0.75, 0.625, 0.50],
            Element.EARTH: [1.00, 0.75, 0.625, 0.50],
            Element.HOLY: [2.00, 1.75, 1.625, 1.50],
            Element.DARK: [0.25, 0.00, 0.000, 0.00],
            Element.POISON: [0.25, 0.00, 0.000, 0.00],
            Element.GHOST: [1.00, 0.75, 0.625, 0.50],
            Element.NEUTRAL: [1.00, 0.75, 0.625, 0.50],
            Element.UNDEAD: [0.25, 0.00, 0.000, 0.00],
        },
        # Attacker: POISON (Image Row 10 - Ghost icon)
        Element.POISON: {
            Element.FIRE: [1.25, 1.00, 0.875, 0.75],
            Element.WIND: [1.25, 1.00, 0.875, 0.75],
            Element.WATER: [1.00, 0.75, 0.625, 0.50],
            Element.EARTH: [1.25, 1.00, 0.875, 0.75],
            Element.HOLY: [0.50, 0.25, 0.125, 0.00],
            Element.DARK: [0.25, 0.00, 0.000, 0.00],
            Element.POISON: [0.25, 0.00, 0.000, 0.00],
            Element.GHOST: [0.50, 0.25, 0.125, 0.00],
            Element.NEUTRAL: [1.00, 0.75, 0.625, 0.50],
            Element.UNDEAD: [0.25, 0.00, 0.000, 0.00],
        },
        # Attacker: GHOST (Image Row 8 - Pink icon)
        Element.GHOST: {
            Element.FIRE: [1.00, 0.00, 0.000, 0.00],
            Element.WIND: [1.00, 0.75, 0.625, 0.50],
            Element.WATER: [1.00, 0.75, 0.625, 0.50],
            Element.EARTH: [1.00, 0.75, 0.625, 0.50],
            Element.HOLY: [0.75, 0.50, 0.375, 0.25],
            Element.DARK: [0.75, 0.50, 0.375, 0.25],
            Element.POISON: [0.75, 0.50, 0.375, 0.25],
            Element.GHOST: [2.00, 1.75, 1.625, 1.50],
            Element.NEUTRAL: [0.25, 0.00, 0.000, 0.00],
            Element.UNDEAD: [1.75, 1.50, 1.375, 1.25],
        },
        # Attacker: NEUTRAL (Image Row 5)
        Element.NEUTRAL: {
            Element.FIRE: [1.00, 0.75, 0.625, 0.50],
            Element.WIND: [1.00, 0.75, 0.625, 0.50],
            Element.WATER: [1.00, 0.75, 0.625, 0.50],
            Element.EARTH: [1.00, 0.75, 0.625, 0.50],
            Element.HOLY: [1.00, 0.75, 0.625, 0.50],
            Element.DARK: [1.00, 0.75, 0.625, 0.50],
            Element.POISON: [1.00, 0.75, 0.625, 0.50],
            Element.GHOST: [0.25, 0.00, 0.000, 0.00],
            Element.NEUTRAL: [1.00, 0.75, 0.625, 0.50],
            Element.UNDEAD: [1.00, 0.75, 0.625, 0.50],
        },
        # Attacker: UNDEAD (Image Row 9)
        Element.UNDEAD: {
            Element.FIRE: [0.50, 0.25, 0.125, 0.00],
            Element.WIND: [0.50, 0.25, 0.125, 0.00],
            Element.WATER: [0.50, 0.25, 0.125, 0.00],
            Element.EARTH: [0.50, 0.25, 0.125, 0.00],
            Element.HOLY: [1.75, 1.50, 1.375, 1.25],
            Element.DARK: [0.25, 0.00, 0.000, 0.00],
            Element.POISON: [0.25, 0.00, 0.000, 0.00],
            Element.GHOST: [1.00, 0.75, 0.625, 0.50],
            Element.NEUTRAL: [1.00, 0.75, 0.625, 0.50],
            Element.UNDEAD: [0.25, 0.00, 0.000, 0.00],
        },
    }
