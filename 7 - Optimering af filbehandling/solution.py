def count_lines(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            count += 1
    return count

filename = "text.txt"
print(count_lines(filename))