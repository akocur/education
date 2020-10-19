import unittest
import regex as r


class TestRegex(unittest.TestCase):
    def test_is_equal(self):
        def check_true(regex, words):
            for word in words:
                self.assertTrue(r.is_matched(regex, word), f'{regex} == {word}')

        check_true('colou?r', ('color', 'colour', 'colorr', 'colourr', 'colour red'))
        check_true('colou?ur', ('colour', 'colouur', 'colourr', 'colouurr', 'colouur red'))

        not_equal_words = ('colouur', 'olor', 'olour', 'colouurr', 'olorr', 'olourr',)
        for word in not_equal_words:
            for i, ch in enumerate(word):
                self.assertFalse(r.is_matched('colou?r', word[i:]), f'colou?r != {word[i:]}')


if __name__ == '__main__':
    unittest.main()