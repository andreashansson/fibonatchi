import unittest
import fibonatchi
import json
import os

class TestFibonatchi(unittest.TestCase):
    def setUp(self):
        data = ["5", "10"]
        with open("skipped_test.json", "w") as json_file:
            json.dump(data, json_file)

    def tearDown(self):
        os.remove("skipped_test.json")

    def test_create_fibonatchi_values(self):
        res = fibonatchi.create_fibonatchi_values("14")
        self.assertEqual(
            res,
            {
                "10": "55",
                "11": "89",
                "12": "144",
                "13": "233",
                "14": "377",
                "1": "0",
                "2": "1",
                "3": "2",
                "4": "3",
                "5": "5",
                "6": "8",
                "7": "13",
                "8": "21",
                "9": "34",
            }
        )

    def test_create_fibonatchi_values_with_one_value(self):
        res = fibonatchi.create_fibonatchi_values("1")
        self.assertEqual(
            res,
            {"1": "0"}
        )

    def test_create_fibonatchi_values_with_two_values(self):
        res = fibonatchi.create_fibonatchi_values("2")
        self.assertEqual(
            res,
            {"1": "0", "2": "1"}
        )

    def test_get_fib_val_by_fib_pos_not_skipped(self):
        fb = fibonatchi.Fibonatchi("skipped_test.json")
        res = fb.get_fib_val_by_fib_pos("11")
        self.assertEqual(res, {"11": "89"})

    def test_get_fib_val_by_fib_pos_is_skipped(self):
        fb = fibonatchi.Fibonatchi("skipped_test.json")
        res = fb.get_fib_val_by_fib_pos("10")
        self.assertEqual(res, {"10": "skipped"})

    def test_get_fib_vals_up_to_fib_pos_with_skipped(self):
        fb = fibonatchi.Fibonatchi("skipped_test.json")
        res = fb.get_fib_vals_up_to_fib_pos("14")
        self.assertEqual(
            res,
            {
                '1': '0',
                '2': '1',
                '3': '2',
                '4': '3',
                '6': '8',
                '7': '13',
                '8': '21',
                '9': '34',
                '11': '89',
                '12': '144',
                '13': '233',
                '14': '377'
            }
        )
