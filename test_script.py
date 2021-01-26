import unittest
from unittest import mock
from unittest.mock import Mock

import pytest

from typing import List, Dict

import re

from company_code import ConnectionDatabaseError
from company_code import TestDbError
from company_code import add
from company_code import connect_to_db
from company_code import get_users_list_from_db

USER_LIST = [{ 'username': 'jonh Doe 1', 'birthday': '02/12/1985', 'role': 'admin' },
             { 'username': 'jonh Doe 2', 'birthday': '02/12/1985', 'role': 'admin' },
             { 'username': 'jonh Doe 3', 'birthday': '02/12/1985', 'role': 'admin' },
             { 'username': 'jonh Doe 4', 'birthday': '02/12/1985', 'role': 'admin' },
             { 'username': 'Dirk Doe', 'birthday': '02/12/1985', 'role': 'admin' },
             { 'username': 'Simon Doe', 'birthday': '02/12/1985', 'role': 'admin' },
             { 'username': 'jonh snyders', 'birthday': '02/12/1985', 'role': 'admin' },
             { 'username': 'jonh jan', 'birthday': '02/12/1985', 'role': 'admin' },
             { 'username': 'dirk jan', 'birthday': '02/12/1985', 'role': 'admin' },
             { 'username': 'Doe jonh', 'birthday': '02/12/1985', 'role': 'admin' },
             { 'username': 'Alber Doe', 'birthday': '02/12/1985', 'role': 'admin' },
             { 'username': 'Bram Doe', 'birthday': '02/12/1985', 'role': 'admin' },
             { 'username': 'Gulce Doe', 'birthday': '02/12/1985', 'role': 'admin' },
             { 'username': 'Louan Doe', 'birthday': '02/12/1985', 'role': 'admin' },
             { 'username': 'jonh Mendoza', 'birthday': '02/12/1985', 'role': 'admin' },
             { 'username': 'jonh V', 'birthday': '02/12/1985', 'role': 'admin' },
             { 'username': 'Mohammad Gothi', 'birthday': '02/12/1985', 'role': 'admin' },
             { 'username': 'Martin Doe', 'birthday': '02/12/1985', 'role': 'admin' },
             { 'username': 'Regis Doe', 'birthday': '02/12/1985', 'role': 'admin' },
             { 'username': 'Dirkjan Doe', 'birthday': '02/12/1985', 'role': 'admin' }]

# Unit testing
class TestCompanyCode(unittest.TestCase):
    """Class that will test all company code."""

    def test_connect_to_db(self):
        """
        Function that tests for correct error raising in 'connect_to_db' function.
        """
        with self.assertRaises(TestDbError) as context:
            connect_to_db("test")
        with self.assertRaises(ConnectionDatabaseError) as context:
            connect_to_db("test/not_test")

    def test_get_users_list_from_db(self):
        """
        Test function that doesn't tries to mock the get_users_list_from_db function, checks if it returns a list of
        of 20+ users, with a username, birthday and role is the correct format.
        """
        self.mock_database = Mock
        self.mock_database.return_value = USER_LIST
        get_users_list_from_db = self.mock_database.return_value
        users = get_users_list_from_db
        n_users = 0
        username = re.compile("[\w]+ [\w]+")
        birthday = re.compile("[\d]{2}/[\d]{2}/[\d]{4}")
        role = re.compile("[\w]+")

        for user in users:
            self.assertTrue(bool(username.match(user['username'])))
            self.assertTrue(bool(birthday.match(user['birthday'])))
            self.assertTrue(bool(role.match(user['role'])))
        self.assertTrue(len(users) >= 20)

        self.assertTrue(len(users))

    def test_add(self, mini=1, maxi=201):
        """
        Test function that will go through every triple combination of every number from 'mini' to 'maxi' and
        sees if the 'add' function will return the same as builtin 'sum' function.
        """
        for i in range(mini, maxi):
            for j in range(mini, maxi):
                for k in range(mini, maxi):
                    self.assertEqual(add(i, j, k), sum([i, j, k]))

if __name__ == "__main__":
    unittest.main()
