# Example 1: Calculating a rectangle's perimeter

def rectangle_perimeter(length, width):
    perimeter = (length + width) * 2
    return round(perimeter, 2)

assert rectangle_perimeter(5, 6) == 22
assert rectangle_perimeter(1.25, 2.43) == 7.36
assert rectangle_perimeter(1.001, 2.005) == 6.01

#returns assertionerror if untrue

#Exercise 1

def convert_american_dollars(american_dollars):
    can_dollar = (american_dollars * 1.34)
    return round(can_dollar, 2)

assert (convert_american_dollars(1) == 1.34)
assert (convert_american_dollars(100) == 134)
assert (convert_american_dollars(100.05) == 134.07)

#Exercise 2

current_time_string = input("What is the current time (in hours)? ")
waiting_time_string  = input("How many hours do you have to wait? ")

current_time_int = int(current_time_string)
waiting_time_int = int(waiting_time_string)

hours = current_time_int + waiting_time_int

timeofday = hours % 24

print(timeofday)

def alarm_time(current_time_string, waiting_time_string):
    current_time_int = int(current_time_string)
    waiting_time_int = int(waiting_time_string)

    hours = current_time_int + waiting_time_int
    timeofday = hours % 24

    return timeofday

assert alarm_time('13', '1') == 14
assert alarm_time('12', '24') == 12
assert alarm_time('13', '11') == 0
assert alarm_time('15', '10') == 1

#Exercise 3

def average(nums):
    num_total = 0
    for num in nums:
        num_total += num
    return(num_total / len(nums))


assert average([1, 1, 1, 5]) == 2.0


#Exercise 4

def find_max(nums):
    current_max = 0
    for num in nums:
        if num > current_max:
            current_max = num
        else:
            continue
    return(current_max)

assert find_max([1, 1, 1, 5]) == 5

#Exercise 5

def evens(nums):
    even_num_list = []
    for num in nums:
        if num % 2 == 0:
            even_num_list.append(num)
        else:
            continue
    return(even_num_list)

assert evens([1, 2, 3, 4]) == [2, 4]

#Exercise 6

def sum_of_sqrs(nums):
    squares_list = []
    for num in nums:
        squares_list.append(num ** 2)
        continue
    return(sum(squares_list))

assert sum_of_sqrs([2, 3, 4]) == 29

#Exercise 7

def squares(nums):
    sqr_list = []
    for num in nums:
        sqr_list.append(num ** 2)
        continue
    return (sqr_list)

assert squares([2, 4, 6, 7, 8]) == [4, 16, 36, 49, 64]