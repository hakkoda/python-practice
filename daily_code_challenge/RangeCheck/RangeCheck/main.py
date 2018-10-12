class RangeCheck(object):
    def __init__(self):
        pass

    def run(self, first, last, num_list):
        result = None

        result = first
        for index in range(first, last):
            if num_list[index] < num_list[result]:
                result = index

        return result;

    def sort_asc(self, num_list):
        result = num_list

        list_len = len(result)
        for x_index in range(0, list_len):
            smallest_index = self.run(x_index, list_len, result)
            smallest = result[smallest_index]
            result[smallest_index] = result[x_index]
            result[x_index] = smallest

        return result
