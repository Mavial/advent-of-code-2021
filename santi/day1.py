import requests
import os

# Import file and data
cookies = {"session": os.getenv('SESSION')}
input = [ int(num) for num in requests.get( "https://adventofcode.com/2021/day/1/input", cookies=cookies ).text.split("\n")[:-1] ]

"""PART 1"""
# Solution
print(len([meas for index, meas in enumerate(input) if meas > input[index-1]]))

# Alternative solution (Benny)
solution = 0
for index in range(1, len(input)):
    if input[index-1] < input[index]:
        solution += 1
print(solution)


"""PART 2"""
# Solution
print(len([sum(input[index:index+3]) for index, _ in enumerate(input[:-2]) if sum(input[index:index+3]) < sum(input[index+1:index+4])]))

# Alternative solution (Benny)
solution = 0
for index in range(len(input)-2):
    if sum(input[index:index+3]) < sum(input[index+1:index+4]):
        solution += 1
print(solution)