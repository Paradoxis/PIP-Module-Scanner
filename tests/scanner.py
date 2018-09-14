from os.path import dirname, join
from unittest import TestCase

from pip_module_scanner import Scanner, ScannerException


class ScannerTestCase(TestCase):
    PROJECT_PATH = join(dirname(__file__), 'project')
    OUTPUT_PATH = 'requirements-test.txt'

    def test_scanner(self):
        for out in (self.OUTPUT_PATH, None):
            scanner = Scanner(path=self.PROJECT_PATH, output=out)
            scanner.run()
            scanner.output()

        with open(self.OUTPUT_PATH) as file:
            data = file.read().splitlines(False)

        self.assertEqual(set(data), {'requests==2.19.1', 'flask==1.0.2'})

        with self.assertRaises(ScannerException):
            scanner = Scanner(path='/foo/bar/baz', output=out)
            scanner.run()
            scanner.output()
