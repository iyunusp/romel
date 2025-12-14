import argparse
import sys
from arcane_rune import arcane_main
from mdb import mdb_main

def main():
    """Main function to handle command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Main script to run different modules.",
        epilog="Run 'python main.py [module] --help' for module-specific options."
    )
    subparsers = parser.add_subparsers(dest='module', help='Available modules')

    # Arcane module
    parser_arcane = subparsers.add_parser('arcane', help='Arcane Rune cost calculator', add_help=False)
    parser_arcane.add_argument('arcane_args', nargs=argparse.REMAINDER)

    # MDB module
    parser_mdb = subparsers.add_parser('mdb', help='MDB damage calculator', add_help=False)
    parser_mdb.add_argument('mdb_args', nargs=argparse.REMAINDER)

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    # Use parse_known_args to avoid argparse from complaining about --help from submodules
    args, unknown = parser.parse_known_args()

    if args.module == 'arcane':
        arcane_main(sys.argv[2:])
    elif args.module == 'mdb':
        mdb_main(sys.argv[2:])
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()