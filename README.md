# Automation Python

This repository contains a small collection of Python automation and CLI utilities built for learning, experimentation, and practical file/API workflows.

The project currently includes two main mini-apps:

- `files_organizer`: a menu-driven file management tool for copying, moving, renaming, trashing, processing directories, and zipping files.
- `api_client`: a terminal-based API client for weather, rate limits, and GitHub data access.

---

## Repository structure

```text
automation_python/
├── .gitignore
├── README.md
├── api_client/
│   ├── main.py
│   └── api/
│       ├── __init__.py
│       ├── github.py
│       ├── rate.py
│       ├── render_screen.py
│       ├── setup_logger.py
│       └── weather.py
├── files_organizer/
│   ├── organize_cli.py
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── copy.py
│   │   ├── move.py
│   │   ├── rename.py
│   │   ├── process_directory.py
│   │   ├── trash.py
│   │   └── zip_unzip_path.py
│   └── organize_util/
│       ├── __init__.py
│       ├── check_status.py
│       ├── formatter.py
│       ├── loading_animation.py
│       ├── parser.py
│       ├── patterns.py
│       ├── render_screen.py
│       └── setup_logger.py
└── tests/   # optional test folder for future coverage
```

---

## Project overview

### 1) files_organizer

This tool provides a command-line menu to organize files and folders quickly from the terminal. Supported actions include:

- copy files
- move files
- rename files
- delete or trash files
- process whole directories
- zip/unzip-related path actions

Run it from inside the project folder:

```bash
cd automation_python/files_organizer
python organize_cli.py
```

The code relies on local imports such as `from commands import ...` and `from organize_util import ...`, so executing the script from inside `files_organizer` is the recommended workflow.

### 2) api_client

This app is a terminal interface for requesting external API data. It currently includes access to:

- weather data
- rate-limit information
- GitHub data

Run it from inside the project folder:

```bash
git clone https://github.com/samuel-2-adom/automation_python.git
cd automation_python/api_client
python main.py
```

This project uses local imports such as `from api import ...`, so it should also be launched from inside `api_client`.

---

## Prerequisites

- Python 3.8+
- pip
- internet access for API calls

Check your Python version:

```bash
python --version
```

---

## Quick start

### File organizer

```bash
cd automation_python/files_organizer
python organize_cli.py
```

### API client

```bash
cd automation_python/api_client
python main.py
```

---

## Learning goals

This repository demonstrates several Python concepts:

- CLI menu design and interactive user input
- file and directory manipulation with `os`, `shutil`, and `pathlib`
- modular project organization using packages and subfolders
- API requests and JSON parsing
- terminal UI patterns, loading animations, and formatted output
- small, real-world automation scripts in a single repo

---

## Suggested next steps

- Add tests under a top-level `tests/` directory for both mini-projects.
- Convert the project folders into installable packages if you want to run them from the repo root.
- Add a GitHub Actions workflow to run automated checks on push and pull requests.
- Expand each project with additional commands or API integrations.

---

## Contributing

Contributions are welcome. If you want to improve a tool:

1. Create a feature branch.
2. Add or update tests where possible.
3. Keep functions modular and focused.
4. Open a pull request with a short explanation of the change.

---

## License

MIT

---

## Contact

- GitHub: @samuel-2-adom
