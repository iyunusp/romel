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
    COEF_TABLE = {
        Element.FIRE: {
            Element.FIRE: 0.25,
            Element.WIND: 1.0,
            Element.WATER: 0.5,
            Element.EARTH: 2.0,
            Element.HOLY: 0.75,
            Element.DARK: 1.0,
            Element.POISON: 0.75,
            Element.GHOST: 1.0,
            Element.NEUTRAL: 1.0,
            Element.UNDEAD: 2.0,
        },
        Element.WIND: {
            Element.FIRE: 1.0,
            Element.WIND: 0.25,
            Element.WATER: 2.0,
            Element.EARTH: 0.5,
            Element.HOLY: 0.75,
            Element.DARK: 1.0,
            Element.POISON: 0.75,
            Element.GHOST: 1.0,
            Element.NEUTRAL: 1.0,
            Element.UNDEAD: 1.0,
        },
        Element.WATER: {
            Element.FIRE: 2.0,
            Element.WIND: 0.5,
            Element.WATER: 0.25,
            Element.EARTH: 1.0,
            Element.HOLY: 0.75,
            Element.DARK: 1.0,
            Element.POISON: 0.75,
            Element.GHOST: 1.0,
            Element.NEUTRAL: 1.0,
            Element.UNDEAD: 1.5,
        },
        Element.EARTH: {
            Element.FIRE: 0.5,
            Element.WIND: 2.0,
            Element.WATER: 1.0,
            Element.EARTH: 0.25,
            Element.HOLY: 0.75,
            Element.DARK: 1.0,
            Element.POISON: 0.75,
            Element.GHOST: 1.0,
            Element.NEUTRAL: 1.0,
            Element.UNDEAD: 1.0,
        },
        Element.HOLY: {
            Element.FIRE: 1.0,
            Element.WIND: 1.0,
            Element.WATER: 1.0,
            Element.EARTH: 1.0,
            Element.HOLY: 0.25,
            Element.DARK: 2.0,
            Element.POISON: 1.25,
            Element.GHOST: 1.0,
            Element.NEUTRAL: 1.0,
            Element.UNDEAD: 2.0,
        },
        Element.DARK: {
            Element.FIRE: 1.0,
            Element.WIND: 1.0,
            Element.WATER: 1.0,
            Element.EARTH: 1.0,
            Element.HOLY: 2.0,
            Element.DARK: 0.25,
            Element.POISON: 0.25,
            Element.GHOST: 1.0,
            Element.NEUTRAL: 1.0,
            Element.UNDEAD: 0.25,
        },
        Element.POISON: {
            Element.FIRE: 1.25,
            Element.WIND: 1.25,
            Element.WATER: 1.0,
            Element.EARTH: 1.25,
            Element.HOLY: 0.5,
            Element.DARK: 0.25,
            Element.POISON: 0.25,
            Element.GHOST: 0.5,
            Element.NEUTRAL: 1.0,
            Element.UNDEAD: 0.25,
        },
        Element.GHOST: {
            Element.FIRE: 1.0,
            Element.WIND: 1.0,
            Element.WATER: 1.0,
            Element.EARTH: 1.0,
            Element.HOLY: 0.75,
            Element.DARK: 0.75,
            Element.POISON: 1.0,
            Element.GHOST: 2.0,
            Element.NEUTRAL: 0.25,
            Element.UNDEAD: 1.0,
        },
        Element.NEUTRAL: {
            Element.FIRE: 1.0,
            Element.WIND: 1.0,
            Element.WATER: 1.0,
            Element.EARTH: 1.0,
            Element.HOLY: 1.0,
            Element.DARK: 1.0,
            Element.POISON: 1.0,
            Element.GHOST: 0.25,
            Element.NEUTRAL: 1.0,
            Element.UNDEAD: 1.0,
        },
        Element.UNDEAD: {
            Element.FIRE: 0.5,
            Element.WIND: 0.5,
            Element.WATER: 0.5,
            Element.EARTH: 0.5,
            Element.HOLY: 1.75,
            Element.DARK: 0.25,
            Element.POISON: 0.25,
            Element.GHOST: 1.0,
            Element.NEUTRAL: 1.0,
            Element.UNDEAD: 0.25,
        },
    }
