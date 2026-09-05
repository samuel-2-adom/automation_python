# automation_python

A small collection of tiny file-organizer CLI tools (copy / move / rename / trash / process-directory) grouped under files_organizer. This repo is intentionally minimal and designed for experimenting with modules, imports, and packages in Python.

[![tests](https://img.shields.io/badge/tests-pytest-blue)]()
[![license](https://img.shields.io/badge/license-MIT-lightgrey)]()


## Quick overview
- Single repository that holds multiple small CLI utilities in files_organizer/.
- The interactive entrypoint is files_organizer/organize_cli.py which presents a terminal menu and delegates work to modules under files_organizer/commands.
- This repo prefers the simple run method: change into the package folder and execute the script. That keeps imports local and is convenient while learning packages and imports.

## Run (recommended for this repo)
From a fresh clone, run the interactive CLI with the exact commands below:

```bash
cd files_organizer
python organize_cli.py
```

Notes:
- The code currently imports modules using local names (e.g. `from commands import copy`). Running from inside files_organizer makes those imports resolve against the current working directory.
- If you later want to run the CLI from the repo root or install it, see the "Make it importable" section below.

## What's in this repo
- files_organizer/
  - organize_cli.py        — interactive menu and main() entrypoint
  - commands/              — implementations for copy, move, rename, trash, process_directory
  - organize_util/         — shared helpers: parsers, renderers, logger setup, status checks
- README.md                — this file
- test.py                  — placeholder (no tests yet)

## Usage examples
After running the CLI, choose one of the numbered options in the menu. Example: to copy files, choose option 1 and follow the prompts.

If you want to run a single command module directly while inside files_organizer for quick testing, you can do:

```bash
python -c "from commands.copy import copy; print(copy)"    # quick import test
```

(Prefer running the interactive menu for normal use.)

## Tests
This repo uses a single test suite for simplicity. Suggested layout:

```
tests/
  test_parser.py
  test_check_status.py
  test_commands_integration.py  # if you add small integration tests
```

Run tests locally:

```bash
pip install -U pytest
pytest -q
```

Testing notes:
- Focus unit tests on deterministic utilities in `files_organizer/organize_util` (parsing, patterns, status checks).
- For commands that touch the filesystem, use pytest's `tmp_path` and `monkeypatch` fixtures to avoid changing real files.
- Keep integration tests short; e.g., test that copy_selected copies expected files under a temporary tree.

## Make it importable (optional)
If you want to run the CLI from the repo root (or `python -m`), convert `files_organizer` to a proper package and use package imports:

1. Add an empty `files_organizer/__init__.py` file.
2. Change imports in `organize_cli.py` and modules to use the package name: e.g.
   - `from files_organizer.commands import copy, move, ...`
   - `from files_organizer.organize_util import parser, patterns, ...`
3. Run the CLI with:

```bash
python -m files_organizer.organize_cli
```

This approach is slightly more work but makes the project behave like an installable package.

## How to add a new CLI tool
1. Add a new module under `files_organizer/commands/` implementing the feature. Follow the pattern used by existing modules (provide `<feature>_main()` for interactive submenus and helper functions for logic).
2. Export the new functions in `files_organizer/commands/__init__.py`.
3. Add a menu entry in `files_organizer/organize_cli.py` to call the new `<feature>_main()`.
4. Add unit tests to `tests/` covering any parsing/utility logic.

## Development & style
- Formatter: black
- Linting: flake8 (optional)
- Keep functions small and testable; push filesystem operations behind small helper functions so you can mock them in tests.

## License
MIT © Your Name

## Contact
- GitHub: @samuel-2-adom

