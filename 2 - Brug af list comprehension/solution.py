input_list = [1, -2, 3, -4, 5, -6]

def positive_numbers(input_list):
    return [x for x in input_list if x > 0]

print(positive_numbers(input_list))