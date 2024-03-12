import re

import pytest

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

class TestNameRegEx:
    @pytest.mark.name_regex
    def test_matches_john_cena(self):
        '''matches the string "John Cena".'''
        assert name_regex.fullmatch("John Cena")

name = r""
name_regex = re.compile(r'^[a-zA-Z\'-]+$')

phone_number = r"5555555555"
phone_regex = re.compile(r'^\d{10}$|^\d{3}-\d{3}-\d{4}$|^\(\d{3}\) \d{3}-\d{4}$')

email_address = r"john.cena@wwe.com"
email_regex = re.compile(r'^[a-zA-Z.0-9]+@[a-zA-Z]+\.[a-zA-Z]+$')

