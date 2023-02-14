from cse163_utils import assert_equals

from document import Document
from search_engine import SearchEngine

# Name: Yeesa Kee
# Section: AE
# This program simulates tests to check that the methods in document.py
# and search_engine.py returns the correct/expected values


def main():
    doc_empty = Document('/home/empty_test.txt')
    test_empty(doc_empty)

    doc_test_1 = Document('/home/docu_test_1.txt')
    test_doc_1(doc_test_1)

    doc_test_2 = Document('/home/docu_test_2.txt')
    test_doc_2(doc_test_2)

    search_0 = SearchEngine('/home/SearchEngine_test_file')
    test_search_empty(search_0)
    test_search_0(search_0)

    search_1 = SearchEngine('/home/SearchEngine_test_file_1')
    test_search_empty(search_1)
    test_search_1(search_1)


def test_empty(doc):
    """
    Runs test_empty

    Tests the emtpy case of functions term_frequency and get_words in
    document.py
    """
    assert_equals(0, doc.term_frequency('dog'))
    assert_equals([], doc.get_words())

    print("Testing test_empty complete")


def test_doc_1(doc):
    """
    Runs test_doc_1

    Tests the functions term_frequency and get_words in document.py
    """
    assert_equals(0.25, doc.term_frequency('dog'))
    assert_equals(0.5, doc.term_frequency('cutest'))
    assert_equals(['the', 'cutest', 'dog'], doc.get_words())

    print("Testing test_docu_1 complete")


def test_doc_2(doc):
    """
    Runs test_doc_2

    Tests the functions term_frequency and get_words in document.py
    """
    assert_equals(0.1, doc.term_frequency('this'))
    assert_equals(0.2, doc.term_frequency('is'))
    assert_equals(0.3, doc.term_frequency('test'))
    assert_equals(['this', 'document', 'is', 'testing', 'the', 'test'],
                  doc.get_words())

    print("Testing test_docu_2 complete")


def test_search_empty(engine):
    """
    Runs test_search_empty

    Tests the empty case of function search in search_engine.py
    """
    assert_equals(None, engine.search('super duper'))
    print("Testing test_search_empty complete")


def test_search_0(engine):
    """
    Runs test_search_0

    Tests the function search in search_engine.py
    """
    assert_equals(['/home/SearchEngine_test_file/doc3.txt',
                  '/home/SearchEngine_test_file/doc1.txt'],
                  engine.search('dogs'))

    print("Testing test_search_0 complete")


def test_search_1(engine):
    """
    Runs test_search_1

    Tests the function search in search_engine.py
    """
    assert_equals(['/home/SearchEngine_test_file_1/doc2.txt',
                  '/home/SearchEngine_test_file_1/doc1.txt'],
                  engine.search('high school'))

    print("Testing test_search_1 complete")


if __name__ == '__main__':
    main()
