import unittest
from flask import url_for
from src.apps import app

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SERVER_NAME'] = 'localhost:5000'
        self.client = app.test_client()

    def test_hello_world(self):
        with app.app_context():
            response = self.client.get(url_for('hello_world'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Hello, World!', response.data)

    def test_new_page(self):
        with app.app_context():
            response = self.client.get(url_for('new_page'))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b'Welcome to the new page!')

if __name__ == '__main__':
    unittest.main()
