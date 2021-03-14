import unittest

class MynotiftTest(unittest.TestCase):
    def test_mynotify(self):
        from notification.core import mynotify
        self.assertIsNone(mynotify())