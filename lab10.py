#LAB 10
#Question 1

def practice_if(score, average):
    if score < average:
        print("Do better next time!")
    else:
        if score >= 90:
            print("Woot woot!")
        elif score > 80:
            print("Great job!")
        else:
            print("Nicely done!")


##print(practice_if(80,80))

#Because the score is equal to the average, none of the elif parts 
#parts of the function apply, the score needs to be over 80 
#to return 'great job!

#Question 2

def practice_for_if(nums, target):
    list = []
    for num in nums:
        if num > target:
            list.append(num)
    return list


#this function will check the 
#numbers we enter and check them against the target value
#so if we entered ([5,5,2,9], 3) the function would return 
#(5,5,9) because those values are greater than the "target" variable


##print(practice_for_if([5, 5, 2, 9], 3))

#Question 3:

def practice_function(nums):
    even_list = []
    for num in nums:
        if num % 2 == 0:
            even_list.append(num)

#This function checks if entered numbers are even or odd
#by dividing by two and checking if there is any remainder 
#if the number%2 is equal to 0, it is even
# if you entered "(5, 5, 2, 9, 6)" into it this function would return
#Nothing in its current state as there is no return prompt

#print(2%2)
#practice_function(5, 5, 2, 9, 6)
#print(even_list(practice_function([5, 5, 2, 9, 6])))

##Question 4,5,6

def practice_for_index_1(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


def practice_for_index_2(nums, target):
    index = -1
    for i in range(len(nums)):
        if nums[i] == target:
            index = i
            break
    return index


def practice_for_index_3(nums, target):
    index = -1
    for i in range(len(nums)):
        if nums[i] == target:
            index = i
    return index

##Q4 

#print(practice_for_index_1([5, 5, 2, 9, 9, 6],9))
#when we run this we get a return value of 3 because 
#the computer stops checking after finding the first 
#appropriate index value, so it does not check the second '9'


###Q5

#practice_for_index_1 & practice_for_index_2
#are functionally the same, they differentiate in how they update 
#the index value. 

##Q6

#practice_for_index_2 & practice_for_index_3
#these functions differ as practice_for_index_3 does not have 
#a break in the 'for' loop, so it checks every index value even if 
#the conditions of the if statement are already satisfied 

###Q7
#this function input will return every number that is NOT
#the target (2) and also returns the string 'none' at the end 
#because the continue function reiterates the for loop one last time 
#even though there is no value to put through

##Q8
#We get the value '6' as the function is essentially 
#a more involved integer division, we could change the number
#we are dividing by by altering the 4th line of the function

#Q9
def exist_in_both(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    shared_index = 0
    for letter in str1:
       if letter in str2:
        shared_index += 1 
        continue 
    return shared_index

#print(exist_in_both('lap', 'help'))
#print(exist_in_both('computer', 'mute'))

##Q10

def good_neighbours(word):
    pair_index = 0
    for i in range(len(word)-1):
        if word[i] == word[i + 1]:
            pair_index += 1 
    return pair_index 

#print(good_neighbours('happiness'))
#print(good_neighbours('arrrrhhh'))

#Q11 

#def more_than_2(words):
    repeat_word_dict = {}
    for word in set(words):
        if words.count(word) > 1:
            repeat_word_dict[word] = word.count(word)
            continue
    return repeat_word_dict

def more_than_2(word_list):
    new_words = {}
    repeat_words = set()
    for word in word_list:
        if word in new_words:
            repeat_words.add(word)
        else:
            new_words[word] = True
    return repeat_words


fruits = ['apple', 'banana', 'apple', 'apple', 'pear', 'orange', 'pear', 'banana']
colours = ['red', 'green', 'blue', 'green', 'yellow', 'red']

        
print(more_than_2(fruits))
print(more_than_2(colours))

