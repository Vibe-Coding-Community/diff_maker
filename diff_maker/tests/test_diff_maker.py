import unittest

from diff_maker import diff_maker


class DiffMakerTests(unittest.TestCase):
    def check(self, original: str, edited: str, expected: str):
        self.assertEqual(diff_maker(original, edited), expected)

    def test_insert_comma(self):
        self.check("думают что", "думают, что", "думают<ins>,</ins> что")

    def test_replace_char(self):
        self.check("зойти", "зайти", "<rep>зайти</rep>")

    def test_whole_phrase_replace(self):
        self.check("забудут вообще", "вообще забудут", "<rep>вообще забудут</rep>")

    def test_delete_space(self):
        self.check("телефон и даже", "телефон, и даже", "телефон<ins>,</ins> и даже")

    def test_long_text(self):
        self.check(
            "Чтобы подключить онлайн банкинг нужно зойти на сайтик",
            "Чтобы подключить онлайн-банкинг, нужно зайти на сайт",
            "Чтобы подключить <rep>онлайн-банкинг</rep><ins>,</ins> нужно <rep>зайти</rep> на <rep>сайт</rep>"
        )

    def test_missed_dot(self):
        self.check(
            "3-х рабочих дней Убедись",
            "3-х рабочих дней. Убедись",
            "3-х рабочих дней<ins>.</ins> Убедись"
        )

    def test_missed_space_after_dot(self):
        self.check(
            "3-х рабочих дней.Убедись", 
            "3-х рабочих дней. Убедись",
            "3-х рабочих дней.<ins> </ins>Убедись"
        )

    def test_replace_and_insert(self):
        self.check(
            "или просто возьмет.", 
            "или просто возьмешь сам.", 
            "или просто <rep>возьмешь сам</rep>."
        )

    def test_insert_in_middle(self):
        self.check(
            "вид карты дебетовая", 
            "вид карты - дебетовая", 
            "вид карты <ins>- </ins>дебетовая"
        )

    


if __name__ == "__main__":
    unittest.main()
