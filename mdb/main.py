import os
import sys
from sys import argv

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from element_coef.element import Element, ElementCoef

ELEMENT = "element"
VALUE = "value"

# Constants for skill data
RM_MDB_RUNE_VALUE = 0.89
RONIN_SSFS_SKILL_MULTIPLIER = 1.8
RONIN_SLASH_TICK = 3
RONIN_SSFS_TICK = 1
RM_MDB_TICK = 1.6
RONIN_CD = 1.5
RM_MDB_CD = 1.0
ENEMY_LVL_ARMOR = 4


SKILLS = {
    "RM MDB": (
        {ELEMENT: Element.FIRE, VALUE: 1},
        {ELEMENT: Element.WATER, VALUE: 1},
        {ELEMENT: Element.DARK, VALUE: RM_MDB_RUNE_VALUE},
    ),
    "Ronin Slash-Light": (
        {ELEMENT: Element.FIRE, VALUE: 1},
        {ELEMENT: Element.HOLY, VALUE: 0.5},
    ),
}

RONIN_SSFS = tuple(
    {ELEMENT: el[ELEMENT], VALUE: el[VALUE] * RONIN_SSFS_SKILL_MULTIPLIER}
    for el in SKILLS["Ronin Slash-Light"]
)


def calc_target(skill_elements: tuple, target: Element, use_lov: bool = False) -> float:
    """Calculates the total damage multiplier against a target element."""
    total = 0
    for element_data in skill_elements:
        if isinstance(element_data, dict):
            value = element_data[VALUE]
            if value == 0:
                continue
            source = element_data[ELEMENT]
            coef = ElementCoef.COEF_TABLE[source][target][ENEMY_LVL_ARMOR - 1]
            if use_lov:
                coef += ElementCoef.COEF_LoV
            value *= coef
            total += value
    return total


LOV = True
CD_REDUCE = 0.26


def print_comparison_header():
    """Prints the header for the element comparison."""
    print("Element Benefit Comparison")
    print("Assume:")
    print("\tUsing LoV: ", LOV)
    print("\tWith CD reduce: {:.0f}%".format(CD_REDUCE * 100))
    print("\tDark MDB Rune: {:.0f}%".format(RM_MDB_RUNE_VALUE * 100))
    print("\tEnemy lvl armor: Lvl-{}".format(ENEMY_LVL_ARMOR))
    print("-----------------------------\n\n")


def comparison_mdb(
    ronin_ss: float, ronin_ssfs: float, rm_mdb: float, prefix_str: str
):
    """Compares the damage outputs and prints the winner."""
    damages = {"Ronin Slash-Light": ronin_ss, "Ronin SSFS": ronin_ssfs, "RM MDB": rm_mdb}
    winner = max(damages, key=damages.get)
    print(f"{prefix_str} Winner: {winner}\n")


def calc_total_tick(base_damage: float, tick_n: float, job: str) -> float:
    """Calculates the total damage over multiple ticks."""
    total_damage = base_damage * tick_n
    print(f"{job} Total x{tick_n} output: {total_damage:.2f}")
    return total_damage


def calc_cd_minute(base_damage: float, cd: float, job: str) -> float:
    """Calculates the total damage output per minute considering cooldown."""
    if CD_REDUCE > 0:
        cd *= 1.0 - CD_REDUCE
    dps = base_damage * (60 / cd)
    print(f"{job} CD {cd:.2f}s Total output: {dps:.2f}")
    return dps


def calc_all_element(target_element: Element):
    """Calculates and compares damage outputs against a specific element."""
    _RONIN_SS = "Ronin Slash-Light"
    _RONIN_SSFS = "Ronin SSFS"
    _RM_MDB = "RM MDB"

    print("Enemy: ", target_element.name)
    print("")

    ronin = calc_target(SKILLS[_RONIN_SS], target_element, LOV)
    print(f"{_RONIN_SS}: {ronin:.3f}")
    ronin_2 = calc_target(RONIN_SSFS, target_element, LOV)
    print(f"{_RONIN_SSFS}: {ronin_2:.3f}")
    rm = calc_target(SKILLS[_RM_MDB], target_element, LOV)
    print(f"{_RM_MDB}: {rm:.3f}")
    comparison_mdb(ronin, ronin_2, rm, "Base damage")

    ronin = calc_total_tick(ronin, RONIN_SLASH_TICK, _RONIN_SS)
    ronin_2 = calc_total_tick(ronin_2, RONIN_SSFS_TICK, _RONIN_SSFS)
    rm = calc_total_tick(rm, RM_MDB_TICK, _RM_MDB + " with T5 weapon")
    comparison_mdb(ronin, ronin_2, rm, "Total damage")

    print("1 Minute DPS")
    ronin = calc_cd_minute(ronin, RONIN_CD, _RONIN_SS)
    ronin_2 = calc_cd_minute(ronin_2, RONIN_CD, _RONIN_SSFS)
    rm = calc_cd_minute(rm, RM_MDB_CD, _RM_MDB)
    comparison_mdb(ronin, ronin_2, rm, "Total damage in 1 minute DPS")

    print("-----------------------------\n")


if __name__ == "__main__":
    print_comparison_header()
    ele_param = argv[1:]
    ele_param = [e.upper() for e in ele_param]
    if len(ele_param) == 1 and ele_param[0] == "ALL":
        for element in Element:
            calc_all_element(element)
    else:
        for element_name in ele_param:
            try:
                element = Element[element_name]
                calc_all_element(element)
            except KeyError:
                print(f"Invalid element: {element_name}")