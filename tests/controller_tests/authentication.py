import api
import unittest
import flask
from flask import json


class AuthenticationTestCase(unittest.TestCase):
    def test_post_200(self):

        test_app = api.app.test_client()

        data = json.dumps(dict(email='email', password='password'))

        response = test_app.post(
            '/gettoken',
            data=data,
            content_type='application/json')

        self.assertEqual(response.status, '200 OK')
