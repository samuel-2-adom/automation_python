import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch, MagicMock

# Add both project directories to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'files_organizer'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'api_client'))

# Import utilities from files_organizer
from organize_util.parser import parse_file_path
from organize_util.patterns import get_patterns
from organize_util.check_status import check_file_exists, check_dir_exists, is_valid_path

# Import utilities from api_client
from api.github import fetch_github_user, fetch_github_repos
from api.weather import fetch_weather
from api.rate import fetch_rate_limit


class TestFilesOrganizerUtilities(unittest.TestCase):
    """Test suite for files_organizer utility functions"""

    def test_parse_file_path_valid(self):
        """Test parsing a valid file path"""
        path = "/home/user/documents/file.txt"
        result = parse_file_path(path)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, tuple)

    def test_parse_file_path_empty(self):
        """Test parsing an empty file path"""
        path = ""
        result = parse_file_path(path)
        self.assertEqual(result, ("", ""))

    def test_parse_file_path_no_extension(self):
        """Test parsing a path without file extension"""
        path = "/home/user/README"
        result = parse_file_path(path)
        self.assertIsNotNone(result)

    def test_get_patterns_returns_dict(self):
        """Test that get_patterns returns a dictionary"""
        patterns = get_patterns()
        self.assertIsInstance(patterns, dict)

    def test_get_patterns_has_keys(self):
        """Test that patterns dictionary has expected keys"""
        patterns = get_patterns()
        self.assertGreater(len(patterns), 0)

    def test_check_file_exists_nonexistent(self):
        """Test checking if a nonexistent file exists"""
        result = check_file_exists("/tmp/nonexistent_file_xyz_12345.txt")
        self.assertFalse(result)

    def test_check_dir_exists_nonexistent(self):
        """Test checking if a nonexistent directory exists"""
        result = check_dir_exists("/tmp/nonexistent_dir_xyz_12345/")
        self.assertFalse(result)

    def test_check_dir_exists_tmp_exists(self):
        """Test checking if /tmp directory exists (should be true on most systems)"""
        result = check_dir_exists("/tmp")
        self.assertTrue(result)

    def test_is_valid_path_empty(self):
        """Test validating an empty path"""
        result = is_valid_path("")
        self.assertFalse(result)

    def test_is_valid_path_valid(self):
        """Test validating a potentially valid path format"""
        result = is_valid_path("/tmp")
        self.assertTrue(result)


class TestAPIClientWeather(unittest.TestCase):
    """Test suite for API Client weather functions"""

    @patch('api.weather.requests.get')
    def test_fetch_weather_success(self, mock_get):
        """Test successful weather API call"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'main': {'temp': 25},
            'weather': [{'description': 'Clear sky'}]
        }
        mock_get.return_value = mock_response

        result = fetch_weather("London")
        self.assertIsNotNone(result)

    @patch('api.weather.requests.get')
    def test_fetch_weather_failure(self, mock_get):
        """Test failed weather API call"""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = fetch_weather("NonexistentCity123")
        self.assertIsNone(result)

    @patch('api.weather.requests.get')
    def test_fetch_weather_empty_city(self, mock_get):
        """Test weather API with empty city name"""
        result = fetch_weather("")
        # Should handle gracefully or return None
        self.assertIsNone(result)


class TestAPIClientGitHub(unittest.TestCase):
    """Test suite for API Client GitHub functions"""

    @patch('api.github.requests.get')
    def test_fetch_github_user_success(self, mock_get):
        """Test successful GitHub user fetch"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'login': 'octocat',
            'name': 'The Octocat',
            'public_repos': 2,
            'followers': 3938
        }
        mock_get.return_value = mock_response

        result = fetch_github_user("octocat")
        self.assertIsNotNone(result)

    @patch('api.github.requests.get')
    def test_fetch_github_user_not_found(self, mock_get):
        """Test GitHub user fetch for nonexistent user"""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = fetch_github_user("nonexistentuser123xyz")
        self.assertIsNone(result)

    @patch('api.github.requests.get')
    def test_fetch_github_repos_success(self, mock_get):
        """Test successful GitHub repos fetch"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {'name': 'repo1', 'url': 'https://github.com/user/repo1'},
            {'name': 'repo2', 'url': 'https://github.com/user/repo2'}
        ]
        mock_get.return_value = mock_response

        result = fetch_github_repos("octocat")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, (list, dict))


class TestAPIClientRate(unittest.TestCase):
    """Test suite for API Client rate limit functions"""

    @patch('api.rate.requests.get')
    def test_fetch_rate_limit_success(self, mock_get):
        """Test successful rate limit API call"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'resources': {
                'core': {'limit': 60, 'remaining': 59, 'reset': 1234567890}
            }
        }
        mock_get.return_value = mock_response

        result = fetch_rate_limit()
        self.assertIsNotNone(result)

    @patch('api.rate.requests.get')
    def test_fetch_rate_limit_failure(self, mock_get):
        """Test failed rate limit API call"""
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        result = fetch_rate_limit()
        self.assertIsNone(result)

    @patch('api.rate.requests.get')
    def test_fetch_rate_limit_timeout(self, mock_get):
        """Test rate limit API call with timeout"""
        mock_get.side_effect = Exception("Connection timeout")

        with self.assertRaises(Exception):
            fetch_rate_limit()


class TestIntegration(unittest.TestCase):
    """Basic integration tests"""

    def test_files_organizer_imports(self):
        """Test that files_organizer modules can be imported"""
        try:
            from organize_util import check_status
            self.assertIsNotNone(check_status)
        except ImportError:
            self.fail("Could not import files_organizer utilities")

    def test_api_client_imports(self):
        """Test that api_client modules can be imported"""
        try:
            from api import weather, github, rate
            self.assertIsNotNone(weather)
            self.assertIsNotNone(github)
            self.assertIsNotNone(rate)
        except ImportError:
            self.fail("Could not import api_client modules")


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
