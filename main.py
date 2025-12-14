import sys
from arcane_rune import arcane_main
from mdb import mdb_main

def print_usage():
    """Prints the usage instructions for the main script."""
    print("Usage: python main.py [module] [args...]")
    print("\nAvailable modules:")
    print("  arcane    - Arcane Rune cost calculator")
    print("  mdb       - MDB damage calculator")
    print("\nRun 'python main.py [module] --help' for module-specific options.")

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] == '--help':
        print_usage()
        sys.exit(1)

    module = sys.argv[1]
    args = sys.argv[2:]

    if module == 'arcane':
        arcane_main(args)
    elif module == 'mdb':
        mdb_main(args)
    else:
        print(f"Error: Unknown module '{module}'\n")
        print_usage()
        sys.exit(1)