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
