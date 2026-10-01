import unittest
import sys
import os
from unittest.mock import patch

# Add the repo root and the project package folders to the Python path
ROOT = os.path.dirname(__file__)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'files_organizer'))
sys.path.insert(0, os.path.join(ROOT, 'api_client'))

# Real imports from the repo structure
from files_organizer.organize_util import (
    check_f_status,
    check_d_status,
    check_fd_status,
    patterns,
    parser,
    formatter,
)
from files_organizer.commands import (
    copy,
    copy_selected,
    copy_main,
    rename,
    rename_selected,
    rename_main,
    move,
    move_selected,
    move_main,
    trash,
    trash_selected,
    trash_main,
    process_directory,
    process_directory_main,
    unzip_path,
    zip_selected,
    zip_file,
    zip_main,
)
from api import github_main, weather_main, rate_main


class TestFilesOrganizerUtilities(unittest.TestCase):
    """Smoke tests for the actual files_organizer modules."""

    def test_check_status_functions_exist(self):
        self.assertTrue(callable(check_f_status))
        self.assertTrue(callable(check_d_status))
        self.assertTrue(callable(check_fd_status))

    def test_patterns_parser_and_formatter_exist(self):
        self.assertTrue(callable(patterns))
        self.assertTrue(callable(parser))
        self.assertTrue(callable(formatter))

    def test_command_functions_exist(self):
        command_funcs = [
            copy, copy_selected, copy_main,
            rename, rename_selected, rename_main,
            move, move_selected, move_main,
            trash, trash_selected, trash_main,
            process_directory, process_directory_main,
            unzip_path, zip_selected, zip_file, zip_main,
        ]
        for fn in command_funcs:
            self.assertTrue(callable(fn))


class TestAPIEntryPoints(unittest.TestCase):
    """Smoke tests for the API package entry points."""

    def test_api_main_entry_points_exist(self):
        self.assertTrue(callable(github_main))
        self.assertTrue(callable(weather_main))
        self.assertTrue(callable(rate_main))


if __name__ == '__main__':
    unittest.main(verbosity=2)
