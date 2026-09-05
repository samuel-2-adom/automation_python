# 🛠️ Automation — Python CLI Tools

This repository is intentionally structured to host multiple small command-line tools (each a mini-project) under a single repo.

---

## 📚 What you'll learn

- CLI argument parsing and interactive menus
- Working with packages, modules, and imports in Python
- File I/O and filesystem operations (copy, move, rename, trash)
- Writing small, testable utilities (parsers, status checks)
- Unit testing with pytest and using tmp_path/monkeypatch for filesystem tests
- Basic terminal UI patterns (loading animations, simple renderers)

---

## 🧰 Projects included

This repo is designed to contain multiple small automation CLI tools. Right now it includes:

- files_organizer — a menu-driven file organizer (copy / move / rename / trash / process-directory)

Future mini-projects can be added as sibling folders at the top level.

---

## 📁 Project structure (recommended)

```
automation_python/
├── README.md                  # This file
├── files_organizer/           # First mini-project (file organizer)
│   ├── organize_cli.py        # interactive entrypoint (run from inside this folder)
│   ├── commands/              # command implementations (copy, move, rename, trash, ...)
│   └── organize_util/         # shared helpers (parsers, renderers, logger)
├── tests/                     # unified test suite for all mini-projects (pytest)
└── .gitignore
```

Each mini-project should follow the same internal layout (an entry script plus modular code under subpackages) so tests and CI can be shared.

---

## 🚀 Quick start — run the file organizer (recommended)

I recommend the simple workflow you chose while learning packages and imports: change into the package folder and execute the script so the local imports resolve naturally.

```bash
git clone https://github.com/samuel-2-adom/automation_python.git
cd automation_python/files_organizer
python organize_cli.py
```

Notes:
- The project currently uses local imports like `from commands import copy` so running from inside `files_organizer` makes those imports resolve.
- If you later want to run from repo root or install the package, convert `files_organizer` into a package (add `files_organizer/__init__.py`) and switch to package imports — instructions below.

---

## 🧪 Tests

This repo uses a single test suite for all mini-projects to keep things simple.

Suggested layout:

```
tests/
  test_parser.py
  test_check_status.py
  test_copy_selected.py
```

Run tests locally:

```bash
pip install -U pytest
pytest -q
```

Testing tips:
- Unit-test deterministic helpers in `files_organizer/organize_util` first (parser, patterns, check_status).
- For filesystem-affecting code, use `tmp_path` and `monkeypatch` to create temporary trees and avoid modifying real files.
- Keep integration tests short (e.g., verify that `copy_selected` copies expected files within a temp directory).

---

## ⚙️ Make a mini-project importable (optional)

If you later want to run a tool from the repository root or with `python -m`, convert a mini-project into a real package:

1. Add `files_organizer/__init__.py`.
2. Change imports to use the package name (example):
   - `from files_organizer.commands import copy` instead of `from commands import copy`
3. Run via:

```bash
python -m files_organizer.organize_cli
```

This is optional — the `cd`-into-folder pattern is fine for learning and small experiments.

---

## 🔧 How to add a new mini-project

1. Create a new top-level folder, e.g. `auto_rename/`.
2. Add an entry script (one-line menu) and modularize logic under subpackages (commands/ or lib/).
3. Add tests in `tests/` that cover utilities and small integration scenarios.
4. Add a short section to this README under "Projects included".

Suggested checklist for each new mini-project:
- [ ] Has a single interactive entrypoint or single CLI file
- [ ] Exposes small testable functions (avoid large monolithic scripts)
- [ ] Includes a brief README/usage snippet inside the folder
- [ ] Adds unit tests to the shared `tests/` folder

---

## 🛠 Built with

- Python 3.x (standard library: os, shutil, pathlib)
- pytest for tests
- Optional: rich for nicer terminal UIs

---

## 📝 Prerequisites

- Python 3.8+ (3.10+ recommended)
- pip

Check Python version:

```bash
python --version
```

---

## 🧭 Example usage (files_organizer)

After running `python organize_cli.py` inside `files_organizer`, choose menu options to copy, move, rename, or trash files. Example: choose option `1` to enter the copy submenu and follow prompts.

Quick import test while inside `files_organizer`:

```bash
python -c "from commands.copy import copy; print(copy.__name__)"
```

---

## 📦 CI & automation (suggestion)

When you're ready, add a simple GitHub Actions workflow that runs `pytest` on push and PR. Keep one job that sets up Python and runs `pytest`. Add the badge to this README so test status is visible.

---

## 🤝 Contributing

Contributions welcome — follow these steps:
1. Fork the repo
2. Create a feature branch
3. Add tests for new behavior
4. Open a PR

---

## 📄 License

MIT © Samuel Adom

---

## ✉️ Contact

- GitHub: @samuel-2-adom

