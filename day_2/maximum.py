numbers = [12, 87, 41, 32, 27, 4, 99, 91]

# Write a program that prints to the console the greatest number of the numbers array
# You should get 99

i = 0
greatest = numbers[0]

while i < len(numbers):
    if greatest < numbers[i]:
        greatest = numbers[i]
    i += 1

print('A legnagyobb elem a', greatest)
