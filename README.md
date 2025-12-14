# Romel Project

This project is a collection of Python submodules with different functionalities.

## Project Structure

```
.
├── arcane_rune/
│   ├── main.py
│   └── ...
├── element_coef/
│   ├── element.py
│   └── ...
├── mdb/
│   ├── main.py
│   └── ...
└── main.py
```

- **`main.py`**: The main entry point of the project. It can be used to run the submodules.
- **`arcane_rune/`**: A submodule for arcane rune calculations.
- **`element_coef/`**: A submodule for element coefficient calculations.
- **`mdb/`**: A submodule for MDB-related functionalities.

## How to Run

### Main Script

The main script can be used to run the submodules.

To see the available modules, run:

```bash
python main.py --help
```

To run a specific module, use the module name as a subcommand. For example, to run the `mdb` module:

```bash
python main.py mdb --help
python main.py mdb holy
```

To run the `arcane_rune` module:

```bash
python main.py arcane_rune --help
```

### Submodules

Each submodule can also be run directly.

#### MDB

```bash
cd mdb
python main.py --help
python main.py holy
```

#### Arcane Rune

```bash
cd arcane_rune
python main.py --help
```