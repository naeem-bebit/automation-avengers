import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Hello, World!', result.data)
        self.assertIn(b'Go to New Page', result.data)

    def test_new_page(self):
        result = self.app.get('/newpage')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Welcome to the new page!', result.data)

if __name__ == '__main__':
    unittest.main()