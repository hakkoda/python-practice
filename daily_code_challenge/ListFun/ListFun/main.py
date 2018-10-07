def create_num_list():
    return None

def find_sum(num_list):
    result = 0

    for val in num_list:
        result += val

    return result

def copy_list(num_list):
    result = []

    for x in num_list:
        result.append(x)

    return result

def sort_asc(num_list):
    result = copy_list(num_list)

    for target_index in range(0, len(result)):
        target = result[target_index]
        for result_index in range(target_index, len(result)):
            if result[result_index] > target:
                temp = result[result_index]
                result[result_index] = target
                result[target_index] = temp
                target = temp

    return result

def find_largest(num_list):
    result = num_list[0]

    for val in num_list:
        result = val if val > result else result

    return result
