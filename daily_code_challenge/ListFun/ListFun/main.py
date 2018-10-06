def create_num_list():
    return None

def find_sum(num_list):
    result = 0

    for val in num_list:
        result += val

    return result

def sort_asc(num_list):
    return None

def find_largest(num_list):
    result = num_list[0]

    for val in num_list:
        result = val if val > result else result

    return result
