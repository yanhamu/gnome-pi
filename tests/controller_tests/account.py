"""Tests for account controller"""

import unittest
from flask import json
import api


class AccountTestCase(unittest.TestCase):
    """Account test case"""

    def test_post_200(self):
        """Should create new account for user"""

        test_app = api.app.test_client()
        data = self.__get_data()
        response = test_app.post(
            '/accounts',
            data=data,
            content_type='application/json')
        self.assertEqual("200 OK", response.status)

    def __get_data(self):
        return json.dumps(dict(
            name="new account",
            token="emptytoken"))