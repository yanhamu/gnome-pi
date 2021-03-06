"""Tests for authentication controller"""

import unittest
from flask import json
import api


class AuthenticationTestCase(unittest.TestCase):
    """Authentication test case"""

    def test_post_200(self):
        """Testing with correct credentials"""

        test_app = api.app.test_client()

        data = json.dumps(dict(email='email', password='password'))

        response = test_app.post(
            '/gettoken',
            data=data,
            content_type='application/json')

        self.assertEqual(response.status, '200 OK')
