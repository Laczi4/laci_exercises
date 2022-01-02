numbers_one = [1, 8, 3, 7, 6]
numbers_two = [9, 7, 55, 7, 5]

def greatest_element(array):
    i = 0
    greatest = array[0]
    while i < len(array):
        if array[i] > greatest:
            greatest = array[i]
        i += 1
    return greatest


print(greatest_element(numbers_one))
print(greatest_element(numbers_two))

amount = greatest_element(numbers_two) + 87

print(amount)