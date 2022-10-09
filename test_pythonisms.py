from pythonisms import Sentences, MySentenceIterator


def test_exists():
    assert Sentences


def test_sentence_reads_correctly():
    phrase = "The quick brown fox."
    actual = Sentences.sentence(phrase)
    expected = "T" \
               "h" \
               "e" \
               " " \
               "q" \
               "u" \
               "i" \
               "c" \
               "k" \
               " " \
               "b" \
               "r" \
               "o" \
               "w" \
               "n" \
               " " \
               "f" \
               "o" \
               "x" \
               "."
    assert actual == expected


def test_iterator_sentence():
    phrase = "The quick brown fox."
    object_passed_in = MySentenceIterator(phrase)
    new_str = ""
    for char in range(len(phrase)):
        new_str += (next(object_passed_in))
    actual = new_str
    expected = phrase
    assert actual == expected
