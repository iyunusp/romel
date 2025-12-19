import argparse
from arcane_rune import arcane_main
from mdb import mdb_main
from inherit_skill import inherit_main

def entry_point():
    """Main function to handle command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Main script to run different modules.",
        epilog="Run 'python main.py [module] --help' for module-specific options."
    )
    # By adding required=True, argparse will handle cases where no module is specified.
    subparsers = parser.add_subparsers(dest='module', help='Available modules', required=True)

    # Arcane module - we only define the command, not its arguments.
    # add_help=False prevents this parser from handling --help.
    subparsers.add_parser('arcane', help='Arcane Rune cost calculator', add_help=False)

    # MDB module
    subparsers.add_parser('mdb', help='MDB damage calculator', add_help=False)

    # Inherit module
    subparsers.add_parser('inherit_skill', help='Inherit skill cost calculator', add_help=False)


    # parse_known_args will separate the known 'module' arg from the unknown ones
    # intended for the sub-module (e.g. '--help', element names, etc.).
    args, unknown = parser.parse_known_args()

    # Call the appropriate submodule's main function with its arguments.
    if args.module == 'arcane':
        # Pass the unknown arguments to the arcane_main function.
        arcane_main(unknown)
    elif args.module == 'mdb':
        # Pass the unknown arguments to the mdb_main function.
        mdb_main(unknown)
    elif args.module == 'inherit_skill':
        # Pass the unknown arguments to the inherit_main function.
        inherit_main(unknown)

if __name__ == '__main__':
    entry_point()
