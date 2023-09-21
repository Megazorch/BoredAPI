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

        try:
            subprocess.run(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True,  # Explicitly set check to True
            )
        except subprocess.CalledProcessError as exc:
            # Handle the exception if the command exits with a non-zero status
            self.assertEqual(exc.returncode, 2)  # Replace with the expected return code

            # Check if the stderr contains the expected error message
            expected_error_message = "usage: main.py\nWrapper for Bored API: error: unrecognized arguments: list\n"
            self.assertEqual(exc.stderr, expected_error_message)


if __name__ == '__main__':
    unittest.main()
