#!/usr/bin/python3
import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):

    def test_assign_id(self):
        test = Base(50)
        self.assertEqual(test.id, 50)

    def test_no_id_assigned(self):
        test = Base()
        self.assertEqual(test.id, 1)

if __name__ == '__main__':
    unittest.main()
