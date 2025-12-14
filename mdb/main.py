import os
import sys
from sys import argv

# This ensures the parent directory is in the path for imports.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from element_coef import Element, ElementCoef



ELEMENT = "element"
VALUE = "value"

class MdbCalculator:
    def __init__(self, Element, ElementCoef):
        self.Element = Element
        self.ElementCoef = ElementCoef

        # Constants for skill data
        self.RM_MDB_RUNE_VALUE = 0.89
        self.RONIN_SSFS_SKILL_MULTIPLIER = 1.8
        self.RONIN_SLASH_TICK = 3
        self.RONIN_SSFS_TICK = 1
        self.RM_MDB_TICK = 1.6
        self.RONIN_CD = 1.5
        self.RM_MDB_CD = 1.0
        self.ENEMY_LVL_ARMOR = 4

        self.SKILLS = {
            "RM MDB": (
                {ELEMENT: self.Element.FIRE, VALUE: 1},
                {ELEMENT: self.Element.WATER, VALUE: 1},
                {ELEMENT: self.Element.DARK, VALUE: self.RM_MDB_RUNE_VALUE},
            ),
            "Ronin Slash-Light": (
                {ELEMENT: self.Element.FIRE, VALUE: 1},
                {ELEMENT: self.Element.HOLY, VALUE: 0.5},
            ),
        }

        self.RONIN_SSFS = tuple(
            {ELEMENT: el[ELEMENT], VALUE: el[VALUE] * self.RONIN_SSFS_SKILL_MULTIPLIER}
            for el in self.SKILLS["Ronin Slash-Light"]
        )
        
        self.LOV = True
        self.CD_REDUCE = 0.26

    def calc_target(self, skill_elements: tuple, target, use_lov: bool = False) -> float:
        """Calculates the total damage multiplier against a target element."""
        total = 0
        for element_data in skill_elements:
            if isinstance(element_data, dict):
                value = element_data[VALUE]
                if value == 0:
                    continue
                source = element_data[ELEMENT]
                coef = self.ElementCoef.COEF_TABLE[source][target][self.ENEMY_LVL_ARMOR - 1]
                if use_lov:
                    coef += self.ElementCoef.COEF_LoV
                value *= coef
                total += value
        return total

    def print_comparison_header(self):
        """Prints the header for the element comparison."""
        print("Element Benefit Comparison")
        print("Assume:")
        print("\tUsing LoV: ", self.LOV)
        print("\tWith CD reduce: {:.0f}%".format(self.CD_REDUCE * 100))
        print("\tDark MDB Rune: {:.0f}%".format(self.RM_MDB_RUNE_VALUE * 100))
        print("\tEnemy lvl armor: Lvl-{}".format(self.ENEMY_LVL_ARMOR))
        print("-----------------------------\n\n")

    def comparison_mdb(self, ronin_ss: float, ronin_ssfs: float, rm_mdb: float, prefix_str: str):
        """Compares the damage outputs and prints the winner."""
        damages = {"Ronin Slash-Light": ronin_ss, "Ronin SSFS": ronin_ssfs, "RM MDB": rm_mdb}
        winner = max(damages, key=damages.get)
        print(f"{prefix_str} Winner: {winner}\n")

    def calc_total_tick(self, base_damage: float, tick_n: float, job: str) -> float:
        """Calculates the total damage over multiple ticks."""
        total_damage = base_damage * tick_n
        print(f"{job} Total x{tick_n} output: {total_damage:.2f}")
        return total_damage

    def calc_cd_minute(self, base_damage: float, cd: float, job: str) -> float:
        """Calculates the total damage output per minute considering cooldown."""
        if self.CD_REDUCE > 0:
            cd *= 1.0 - self.CD_REDUCE
        dps = base_damage * (60 / cd)
        print(f"{job} CD {cd:.2f}s Total output: {dps:.2f}")
        return dps

    def calc_all_element(self, target_element):
        """Calculates and compares damage outputs against a specific element."""
        _RONIN_SS = "Ronin Slash-Light"
        _RONIN_SSFS = "Ronin SSFS"
        _RM_MDB = "RM MDB"

        print("Enemy: ", target_element.name)
        print("")

        ronin = self.calc_target(self.SKILLS[_RONIN_SS], target_element, self.LOV)
        print(f"{_RONIN_SS}: {ronin:.3f}")
        ronin_2 = self.calc_target(self.RONIN_SSFS, target_element, self.LOV)
        print(f"{_RONIN_SSFS}: {ronin_2:.3f}")
        rm = self.calc_target(self.SKILLS[_RM_MDB], target_element, self.LOV)
        print(f"{_RM_MDB}: {rm:.3f}")
        self.comparison_mdb(ronin, ronin_2, rm, "Base damage")

        ronin = self.calc_total_tick(ronin, self.RONIN_SLASH_TICK, _RONIN_SS)
        ronin_2 = self.calc_total_tick(ronin_2, self.RONIN_SSFS_TICK, _RONIN_SSFS)
        rm = self.calc_total_tick(rm, self.RM_MDB_TICK, _RM_MDB + " with T5 weapon")
        self.comparison_mdb(ronin, ronin_2, rm, "Total damage")

        print("1 Minute DPS")
        ronin = self.calc_cd_minute(ronin, self.RONIN_CD, _RONIN_SS)
        ronin_2 = self.calc_cd_minute(ronin_2, self.RONIN_CD, _RONIN_SSFS)
        rm = self.calc_cd_minute(rm, self.RM_MDB_CD, _RM_MDB)
        self.comparison_mdb(ronin, ronin_2, rm, "Total damage in 1 minute DPS")

        print("-----------------------------\n")

    def main(self, elements=None):
        if elements is None:
            elements = argv[1:]
            
        self.print_comparison_header()
        ele_param = [e.upper() for e in elements]
        if len(ele_param) == 1 and ele_param[0] == "ALL":
            for element in self.Element:
                self.calc_all_element(element)
        else:
            for element_name in ele_param:
                try:
                    element = self.Element[element_name]
                    self.calc_all_element(element)
                except KeyError:
                    print(f"Invalid element: {element_name}")

def main(args=None):
    """
    Main function to run the MDB calculator.
    Initializes the calculator and runs the calculations based on provided arguments.
    """
    calculator = MdbCalculator(Element, ElementCoef)
    calculator.main(args)

if __name__ == "__main__":
    main()
