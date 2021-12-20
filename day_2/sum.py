numbers = [12, 87, 41, 32, 27, 4, 99, 91]

# Write a program that prints to the console the sum of the numbers array
# You should get 393

i = 0
sum = 0
while i < len(numbers):
    sum = sum + numbers[i]
    i += 1

print('A számok összege a', sum)