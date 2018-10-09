class Anagram(object):
    def __init__(self):
        pass

    def sort_word(self, word):
        result = self.str_to_list(word)

        for x_index in range(0, len(result)):
            x = result[x_index]
            for y_index in range(x_index, len(result)):
                if result[y_index] < result[x_index]:
                    y = result[y_index]
                    result[y_index] = x
                    result[x_index] = y
                    x = y

        return result;

    def str_to_list(self, word):
        result = []
        
        for letter in word:
            result.append(letter)

        return result

    def is_anagram(self, word_1, word_2):
        if len(word_1) != len(word_2):
            return False

        word_1_sorted = self.sort_word(word_1)
        word_2_sorted = self.sort_word(word_2)

        return word_1_sorted == word_2_sorted

