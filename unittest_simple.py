import unittest

class SimpleTest(unittest.TestCase):

    def test(self):
        self.failUnless(true)

if __name__ == '__main__':
    unittest.main()
