import unittest
from search_by_words import search_by_words 

class TestSearchWords(unittest.TestCase):
    def setUp(self):
        self.text = """
    In an alternate universe, movie buffs have Citizen Kane on vinyl. In that alternate universe, unlike in our own, Capacitance Electronic Discs (CEDs) survived instead of being consigned to the same media-format graveyard as Betamax and HD DVD.
    Few people even remember that such a medium as vinyl movies existed, but for a brief, doomed period in the early 1980s, home video was available on CEDs. While CED players were not released to consumers until 1981, the development of the system dates back to the 1960s. The idea was that they could encode sound and video information to a vinyl disc if they could only get the grooves small enough.
        """

    def test_should_return_a_empty_list_when_it_does_not_find_words(self):
        result = search_by_words('It is a text', 'ball')
        self.assertEqual(result, [])

    def test_should_return_the_sentence_where_it_contains_the_word(self):
        result = search_by_words(self.text, 'HD')
        expected = ['In that alternate universe, unlike in our own, Capacitance Electronic Discs (CEDs) survived instead of being consigned to the same media-format graveyard as Betamax and HD DVD']

        self.assertEqual(len(result), 1)
        self.assertEqual(result, expected)

    def test_should_return_the_sentences_with_word_in_plural(self):
        result = search_by_words(self.text, 'CED')
        expected = ['In that alternate universe, unlike in our own, Capacitance Electronic Discs (CEDs) survived instead of being consigned to the same media-format graveyard as Betamax and HD DVD', 'Few people even remember that such a medium as vinyl movies existed, but for a brief, doomed period in the early 1980s, home video was available on CEDs', 'While CED players were not released to consumers until 1981, the development of the system dates back to the 1960s']

        self.assertEqual(len(result), 3)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
