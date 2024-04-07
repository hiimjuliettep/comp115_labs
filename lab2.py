#Juliette Purkiss
#Exercise 1

num = 5
new_num = num * 10 - 15
print(f"this exercise's number is now: {new_num}")

#Exercise 2

dividend = 13
divisor = 4

decimal_quotient = dividend / divisor
quotient = dividend // divisor
remainder = dividend % divisor

print(f"Exercise 2's quotient is {quotient}, remainder is: {remainder}.")

#Exercise 3

rectangle_w = 5
rectangle_l = 3

perimeter = (rectangle_w + rectangle_l) * 2
area = rectangle_l * rectangle_w
print(f"Exercise 3's rectanguler perimeter is: {perimeter}, with an area of: {area}.")

#Exercise 4

marks = [80.5, 86.5]
mark_mid = marks[0]
mark_final = marks[1]
mark_avergae = (mark_mid + mark_final) / len(marks)
print(f"Exercise 4's average mark is {mark_avergae}")

#Exercise 5

words = ["apple", "pear"]
if len(words[0]) > len(words[1]):
    longer_word = words[0]
else:
    longer_word = words[1]

print(f"Exercise 5's longer word is: {longer_word}")

#Exercise 6

increase = 0.2
increase_percentage = increase * 100
print(f"Exercise 6's increase percentage is: {increase_percentage}%")

#Exercise 7

x = 2 
count = 0
while count < 14:
    print(x)
    x = x + 2
    count = count + 2

print(x)

