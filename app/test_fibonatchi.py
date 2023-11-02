import unittest
import fibonatchi


class TestFibonatchi(unittest.TestCase):
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
