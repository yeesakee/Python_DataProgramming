import re


# Name: Yeesa Kee
# Section: AE
# This program creates a Document class. Users are able to pass in a file name
# and get the term frequency (number of occurences of a term in the
# file / the number of words in the file) of a word from a given file and get
# a list of all the unique words (no repeats) in the given file.


class Document:
    """
    Creates a Document object that takes a file.
    Users can get the term frequency (number of occurences of the term in the
    file / the number of words in the file) of a given term from the given
    file.
    Users can get a list of all the unique words (no repeats) in the
    given file.

    All words processed will be case insensitive and ignore punctuation.
    """

    def __init__(self, file_name):
        """
        Initializes a Document object.
        Takes a file name to be processed.
        """
        # stores a tuple with the first index containing a dictionary with
        # words as keys and the number of times it appears as the value. The
        # second index stores the total number of words in the given file.
        tup = self._store(file_name)
        self._dic = tup[0]
        self._total_words = tup[1]

    def _store(self, file_name):
        """
        Returns a tuple with the first index containing a dictionary with
        words in the file as keys and the number of times the word appears
        in the given file as values, and the second index containing the
        total number of words in the given file.

        All words processed will be case insensitive and ignore punctuation.
        """
        dic = dict()
        count = 0
        with open(file_name) as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                line_list = line.split()
                count += len(line_list)
                for word in line_list:
                    # remove all punctuation and convert to lowercase
                    word = re.sub(r'\W+', '', word).lower()
                    # if word is a key in dic
                    if word in dic:
                        dic[word] += 1
                    else:
                        dic[word] = 1
        return dic, count

    def term_frequency(self, word):
        """
        Returns the term frequency (number of occurences of the term in the
        file / the number of words in the file) of a word from a given file.
        Returns 0 if the word does not appear in the given file.
        """
        if word in self._dic:
            return self._dic[word] / self._total_words
        return 0

    def get_words(self):
        """
        Returns a list of all the unique words (no repeats) in the given file.
        """
        word_list = list()
        for key in self._dic.keys():
            word_list.append(key)
        return word_list
