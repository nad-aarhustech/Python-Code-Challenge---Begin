def count_elements(input_list):
    count_dict = {}
    for num in input_list:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict
