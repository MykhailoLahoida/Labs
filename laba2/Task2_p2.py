"""
Create a class that performs statistical processing of a text file - counting characters, words, sentences, etc.
Determine the required attributes-data and attributes-methods in class for working with the text file.
"""
class Counter:
    def __init__(self, filename):
        self.__file = open(filename)
        self.__data = self.__file.read()

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, str):
            raise TypeError("Data is string")
        self.__data = data

    @property
    def count_chars(self):
        return len(self.data)

    @property
    def count_words(self):
        word = self.data.split()
        return len(word)

    @property
    def count_sentences(self):
        point = self.data.split('.')
        exclamation_mark = self.data.split('!')
        question_mark = self.data.split('?')
        mega_mark = self.data.split('?!')
        return len(point) - 1 + len(exclamation_mark) - 1 + len(question_mark) - 1 + len(mega_mark) - 1

if __name__ == "__main__":
    William = Counter('text.txt')
    print('Number of characters in text file :', William.count_chars)
    print('Number of words in text file :', William.count_words)
    print('Number of sentences in text file :', William.count_sentences)