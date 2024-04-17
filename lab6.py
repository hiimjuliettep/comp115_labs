#Juliette Purkiss!!

#Exercise 1

def reverse_str(s):
    new_str = []
    for x in range(len(s)-1, -1, -1):
        new_str.append(s[x])
    return(new_str)

my_string = "I hope this works"
print(reverse_str(my_string))

#Exercise 2

def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    lower_s = s.lower()
    count = 0
    for char in lower_s:
        if char in vowels:
            count += 1
            continue
    return count

assert count_vowels("Apple") == 2

#Exercise 3

def remove_dupes(s):
    lower_s = s.lower()
    new_str = []
    for char in lower_s:
        if char not in new_str:
            new_str.append(char)
    return ''.join(new_str)

assert remove_dupes('apple') == 'aple'

#Exercise 4

def find_index(s, t):
    for i in range(len(s)):
        if s[i] == t:
            return i
    return -1

assert find_index("Abd", "b") == 1

#Exercise 5

def project_completion_day(day, days_to_fin):
    weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    weekday_index = weekdays.index(day)
    completion_index = (weekday_index + days_to_fin) % 7
    return weekdays[completion_index]

print(project_completion_day('Monday', 4))

assert project_completion_day('Monday', 4) == 'Friday'
assert project_completion_day('Monday', 7) == 'Monday'