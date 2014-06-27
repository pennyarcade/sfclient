import unittest


class TestSuite(unittest.TestCase):

    def test(self):
        self.assert(True)


def main():
    unittest.main()

if __name__ == "__main__":
    main()
