import math
import os
import re
from document import Document

# Name: Yeesa Kee
# Section: AE
# This program is a SearchEngine class. Users are able to create a SeachEngine
# object that takes a directory.
# Users are able to get a list of file names in descending order of TF-IDF.


class SearchEngine:
    """
    Creates a SearchEngine object that takes a directory.
    Users can get a list of document names sorted in descending order of
    TF-IDF.
    """
    def __init__(self, directory):
        """
        Initializes a SearchEngine object.
        Takes a directory of the all the files that will be processed.
        """
        # stores Documents as keys and directories as values
        self._directory_dict = dict()
        for file_name in os.listdir(directory):
            direc_name = f'{directory}/{file_name}'
            doc = Document(direc_name)
            self._directory_dict[doc] = direc_name
        # stores words as keys and which documents the words show up as values
        self._dic_index = self._inverse_index(self._directory_dict)

    def _inverse_index(self, direc_list):
        """
        Returns an inverse index (a dictionary with unique words found in the
        given files as keys and the Documents the words are seen in as values)
        """
        index = dict()
        for docu in direc_list.keys():
            # stores the list of all the unique words in docu
            word_list = docu.get_words()
            for word in word_list:
                # if word is a key in index
                if word in index:
                    index[word].append(docu)
                else:
                    index[word] = [docu]
        return index

    def _calculate_idf(self, word):
        """
        Returns the calculated IDF score of the given word
        Returns 0 if word does not appear in any of the given files.
        """
        if word not in self._dic_index:
            return 0
        # stores the number of files that word appears in
        t_docu_num = len(self._dic_index[word])
        # stores the total number of files given
        total_docu = len(self._directory_dict)
        return math.log(total_docu / t_docu_num)

    def search(self, my_search):
        """
        Returns a list of file names in descending order of TF-IDF.
        Returns None if my_search does not appear in any given files.
        """
        my_search = my_search.strip()
        list_search = my_search.split()
        do_not_contain = True
        for word in list_search:
            word = re.sub(r'\W+', '', word).lower()
            if word in self._dic_index:
                do_not_contain = False
        if do_not_contain:
            return None
        # stores the TF-IDF score of my_search
        TFIDF = 0
        # stores tuples with the first index storing the file name
        # and the second index storing the TF-IDF score
        list_TFIDF = list()
        # stores the list of file names in descending order of TF-IDF
        result = list()
        for doc in self._directory_dict:
            file_name = self._directory_dict[doc]
            for word in list_search:
                word = re.sub(r'\W+', '', word).lower()
                TFIDF += self._calculate_idf(word) *\
                    doc.term_frequency(word)
            if TFIDF > 0:
                list_TFIDF.append((file_name, TFIDF))
                TFIDF = 0
        # sort the list in descending order of TF-IDF
        list_TFIDF = sorted(list_TFIDF, key=lambda doc: doc[1], reverse=True)
        for tup in list_TFIDF:
            result.append(tup[0])
        return result
