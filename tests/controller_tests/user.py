"""Tests for users controller"""

import unittest
from flask import json
import api


class UserTestCase(unittest.TestCase):
    """User test case"""

    def test_post_200(self):
        """ Tests creation of new user"""
        test_app = api.app.test_client()
        data = json.dumps(dict(email='email@email.com', password='password'))
        response = test_app.post(
            '/users',
            data=data,
            content_type='application/json')

        self.assertEqual(response.status, '200 OK')
