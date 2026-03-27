import unittest
import datetime
from Person import Person

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.p = Person('Mark', 2000)

    def test_get_name(self):
        self.assertEqual(self.p.get_name(), 'Mark')

    def test_set_name(self):
        self.p.set_name('Max')
        self.assertEqual(self.p.get_name(), 'Max')

    def test_get_age(self):
        current_year = datetime.datetime.now().year
        self.assertEqual(self.p.get_age(), current_year - 2000)

    def test_get_address_default(self):
        self.assertEqual(self.p.get_address(), '')

    def test_set_address(self):
        self.p.set_address('Ekaterinburg')
        self.assertEqual(self.p.get_address(), 'Ekaterinburg')

    def test_is_homeless_true(self):
        self.p.set_address(None)
        self.assertEqual(self.p.is_homeless(), True)

    def test_is_homeless_false(self):
        self.p.set_address('Ekaterinburg')
        self.assertEqual(self.p.is_homeless(), False)

if __name__ == '__main__':
    unittest.main()