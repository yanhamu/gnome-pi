"""Tests for account controller"""

import unittest
from unittest.mock import patch
from flask import json, g
from api import app
from tests.controller_tests import fake


class AccountTestCase(unittest.TestCase):
    """Account test case"""

    @patch('api.get_user_data')
    @patch('api.get_db_connection')
    def test_post_200(self, get_user, get_db_connection):
        """Should create new account for user"""

        # mocking to be fixed!
        get_user.return_value = fake.get_fake_user()
        #get_db_connection.side_effect = fake.get_fake_db

        test_app = app.test_client()

        response = test_app.post(
            '/accounts',
            data=self.__get_data(),
            content_type='application/json')

        self.assertEqual("200 OK", response.status)

    def __get_data(self):
        return json.dumps(dict(
            name="new account",
            token="emptytoken"))
