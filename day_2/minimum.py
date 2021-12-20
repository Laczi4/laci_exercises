numbers = [12, 87, 41, 32, 27, 4, 99, 91]

# Write a program that prints to the console the smallest number of the numbers array
# You should get 4

i = 0
smallest = numbers[0]

while i < len(numbers):
    if smallest > numbers[i]:
        smallest = numbers[i]
    i += 1

print('A legkisebb elem a', smallest)