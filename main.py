import sys
import os

# Check if the script is running in a directory that is not the project root
# and add the project root to the path.
if sys.path[0] not in ('.', ''):
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from arcane_rune.main import main as arcane_main
from mdb.main import MdbCalculator
from element_coef.element import Element, ElementCoef

def print_usage():
    """Prints the usage instructions for the main script."""
    print("Usage: python main.py [module] [args...]")
    print("\nAvailable modules:")
    print("  arcane    - Arcane Rune cost calculator")
    print("  mdb       - MDB damage calculator")
    print("\nRun 'python main.py [module] --help' for module-specific options.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    module = sys.argv[1]
    args = sys.argv[2:]

    if module == 'arcane':
        arcane_main(args)
    elif module == 'mdb':
        calculator = MdbCalculator(Element, ElementCoef)
        calculator.main(args)
    else:
        print(f"Error: Unknown module '{module}'\n")
        print_usage()
        sys.exit(1)