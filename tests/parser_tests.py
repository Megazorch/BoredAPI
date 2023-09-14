"""
Tests for Bored API wrapper
"""

import unittest
from bored_api import bored_arg_parse


class Parser_Correct_Test(unittest.TestCase):
    def setUp(self):
        self.parser = bored_arg_parse.create_parser()

    def test_new_argument(self):
        """
        Test the new argument
        """
        parsed = self.parser.parse_args(['new'])
        self.assertEqual(parsed.action, 'new')

    def test_type_argument(self):
        """
        Test the type argument
        """
        parsed = self.parser.parse_args(['new', '--type', 'education'])
        self.assertEqual(parsed.type, 'education')

    def test_participants_argument(self):
        """
        Test the participants argument
        """
        parsed = self.parser.parse_args(['new', '--participants', '1'])
        self.assertEqual(parsed.participants, 1)

    def test_price_min_argument(self):
        """
        Test the price_min argument
        """
        parsed = self.parser.parse_args(['new', '--price_min', '0.1'])
        self.assertEqual(parsed.minprice, 0.1)

    def test_price_max_argument(self):
        """
        Test the price_max argument
        """
        parsed = self.parser.parse_args(['new', '--price_max', '0.2'])
        self.assertEqual(parsed.maxprice, 0.2)

    def test_accessibility_argument(self):
        """
        Test the accessibility argument
        """
        parsed = self.parser.parse_args(['new', '--accessibility', '0.3'])
        self.assertEqual(parsed.accessibility, 0.3)

    def test_accessibility_min_argument(self):
        """
        Test the accessibility_min argument
        """
        parsed = self.parser.parse_args(['new', '--accessibility_min', '0.4'])
        self.assertEqual(parsed.accessibility_min, 0.4)

    def test_accessibility_max_argument(self):
        """
        Test the accessibility_max argument
        """
        parsed = self.parser.parse_args(['new', '--accessibility_max', '0.5'])
        self.assertEqual(parsed.accessibility_max, 0.5)
