"""
This module contains the integration tests for the main.py script.
"""
import unittest
import subprocess


class IntegrationTests(unittest.TestCase):
    """
    Integration tests for the main.py script.
    """
    def test_invalid_arguments(self):
        """
        Run the script with invalid arguments ('new list')
        """
        command = 'python main.py new list'
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check if the exit code indicates an error
        self.assertNotEqual(result.returncode, 0)

        # Check if the stderr contains the expected error message
        expected_error_message = "usage: main.py\nWrapper for Bored API: error: unrecognized arguments: list\n"
        self.assertIn(expected_error_message, result.stderr)


if __name__ == '__main__':
    unittest.main()