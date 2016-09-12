# testing api rest provider model
import os
import unittest

class ProviderTestCase(unittest.TestCase):
    # 0
    def test_success(self):
        from provider import app
        with app.test_client() as client:
            response = client.get('/apis/providers')
            self.assertEqual(200,response.status_code)


if __name__ == '__main__':
    unittest.main()
