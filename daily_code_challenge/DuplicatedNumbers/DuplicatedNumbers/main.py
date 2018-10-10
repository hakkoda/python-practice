class DuplicatedNumbers(object):
    def __init__(self):
        pass

    def has_dups(self, num_list):
        sorted_list = self.sort_list(num_list)
        for x_index in range(0, len(sorted_list)-1):
            if sorted_list[x_index] == sorted_list[x_index+1]:
                return True
        return False

    def sort_list(self, num_list):
        result = num_list

        for x_index in range(0, len(result)):
            x = result[x_index]
            for y_index in range(x_index, len(result)):
                y = result[y_index]
                if y < x:
                    result[y_index] = x
                    result[x_index] = y
                    x = y

        return result
