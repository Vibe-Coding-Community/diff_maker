import unittest

from diff_maker import diff_maker


class DiffMakerTests(unittest.TestCase):
    def check(self, original: str, edited: str, expected: str):
        self.assertEqual(diff_maker(original, edited), expected)

    def test_insert_comma(self):
        self.check("думают что", "думают, что", "думают<ins>,</ins> что")

    def test_replace_char(self):
        self.check("зойти", "зайти", "<rep>зойти</rep>")

    def test_whole_phrase_replace(self):
        self.check("вообще забудут", "забудут вообще", "<rep>вообще забудут</rep>")

    def test_delete_space(self):
        self.check("телефон, и даже", "телефон и даже", "телефон<del>,</del> и даже")


if __name__ == "__main__":
    unittest.main()
