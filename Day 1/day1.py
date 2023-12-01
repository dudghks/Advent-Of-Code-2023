# Part one
import re

with open('input.txt') as file:
    text = file.readlines()

sum = 0
for line in text:
    numbers = []
    for char in line:
        if char.isnumeric():
            numbers.append(char)
    sum += int(numbers[0] + numbers[-1])

print(sum)

# Part two
with open('input.txt') as file:
    text = file.readlines()

regex = '(?=(one|two|three|four|five|six|seven|eight|nine|zero|\d))'
word_to_number = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5',
                  'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}

sum = 0
for line in text:
    numbers = [word_to_number[x] if len(x) > 1 else x for x in re.findall(regex, line)]
    print('=========')
    print(line)
    print(re.findall(regex, line))
    print(numbers)
    print(numbers[0] + numbers[-1])
    sum += int(numbers[0] + numbers[-1])

print(sum)