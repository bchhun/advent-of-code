#!/usr/bin/env python3

import unittest

from functions import getOpcodeResult, changeNounAndVerb

class MyTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            getOpcodeResult("1,0,0,0,99"), 
            "2,0,0,0,99"
        )

    def test_2(self):
        self.assertEqual(
            getOpcodeResult("2,3,0,3,99"), 
            "2,3,0,6,99"
        )

    def test_3(self):
        self.assertEqual(
            getOpcodeResult("2,4,4,5,99,0"), 
            "2,4,4,5,99,9801"
        )

    def test_4(self):
        self.assertEqual(
            getOpcodeResult("1,1,1,4,99,5,6,0,99"),
            "30,1,1,4,2,5,6,0,99"
        )
    
    def test_changing_verb_and_noun(self):
        self.assertEqual(
            changeNounAndVerb("0,0,0,0", 1, 1),
            "0,1,1,0"
        )

if __name__ == '__main__':
    unittest.main()
