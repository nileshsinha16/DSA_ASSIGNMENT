#Q1. Write a code to reverse a string.

ab=("hello nilesh", "dip","sinha")
list(reversed(ab))


#Q2. Write a code to count the number of vowels in a string.

b="hello python"
len (b)


#Q3. Write a code to check if a given string is a palindrome or not

str="madam"
str1= reversed(str)

if list(str)== list(str1):
  print('it is palandroma')
else:
  print('it is not palandroma')


#Q4. Write a code to check if two given strings are anagrams of each other.

s= 'race'
s1= 'care'
sorted_s= sorted(s)
sorted_s1=sorted(s1)
if sorted_s==sorted_s1:
  print(f"{s} and {s1}  both are anagram ")
else:
  print(f"{s} and {s1}  both are not anagram ")


#Q5. Write a code to find all occurrences of a given substring within another string

def print_indices(s, sub):
    pos = s.find(sub)

    if pos == -1:
        print("NONE")

    while pos != -1:
        print(pos, end=" ")
        pos = s.find(sub, pos + 1)

if __name__ == "__main__":
    str1 = "GeeksforGeeks"
    str2 = "Geeks"
    print_indices(str1, str2)


#Q6. Write a code to perform basic string compression using the counts of repeated characters

def solve(s):
   res = ""
   cnt = 1
   for i in range(1, len(s)):
      if s[i - 1] == s[i]:
         cnt += 1
      else:
         res = res + s[i - 1]
         if cnt > 1:
            res += str(cnt)
         cnt = 1
   res = res + s[-1]
   if cnt > 1:
      res += str(cnt)
   return res

s = "abbbaaaaaaccdaaab"
print(solve(s))


#Q7. Write a code to determine if a string has all unique characters.

st = "abcvjkrld"
a=""
for i in st:
    if i not in a:
        a+=i
if(a==st):
    print(True)
else:
    print(False)


#Q8. Write a code to convert a given string to uppercase or lowercase.

text= "i am Nilesh Sinha"
##upper
print (text.upper())
##lower
print (text.lower())


#Q9. Write a code to count the number of words in a string.

count_word = len(" i am electrical engineering student of BP PODDAR ".split())
print("Count of word in the given sentance is ", count_word)


#Q10. Write a code to concatenate two strings without using the + operator.

word1= "Hello"
word2= " I am a student"
sen= "".join([word1,word2])
print(sen


#Q11. Write a code to remove all occurrences of a specific element from a list.

test_list = [1, 3, 4, 6, 5, 1]
ele=1
x=[j for i,j in enumerate(test_list) if j!=ele]
print(x)


#Q12. Implement a code to find the second largest number in a given list of integers

# List of numbers
list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]

# Removing duplicates from the list
list2 = list(set(list1))

# Sorting the  list
list2.sort()

# Printing the second last element
print("Second largest element is:", list2[-2])


#Q13. Create a code to count the occurrences of each element in a list and return a dictionary with elements as keys and their counts as values

def CountFrequency(my_list):

    # Creating an empty dictionary
    count = {}
    for i in [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]:
        count[i] = count.get(i, 0) + 1
    return count


# Driver function
if __name__ == "__main__":
    my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
    print(CountFrequency(my_list))


#Q14. Write a code to reverse a list in-place without using any built-in reverse functions

las= [1,2,3,4,5,6,7,8]
print(las[::-1])


#Q15. Implement a code to find and remove duplicates from a list while preserving the original order of elements

test_list1 = [1, 5, 3, 6, 3, 5, 8, 8, 6, 1]
print ("The original list is : "
        + str(test_list1))

# using set() to remove duplicated from list
test_list1 = list(set(test_list1))

# printing list after removal
# distorted ordering
print ("The list after removing duplicates : "
        + str(test_list1))


#Q16. Create a code to check if a given list is sorted (either in ascending or descending order) or not.

test_list2 = [1, 4, 5, 8, 10]

# printing original list
print ("Original list : " + str(test_list2))

# using sorted() to
# check sorted list
flag = 0
if(test_list2 == sorted(test_list2)):
    flag = 1

# printing result
if (flag) :
    print ("Yes, List is sorted.")
else :
    print ("No, List is not sorted.")


#Q17. Write a code to merge two sorted lists into a single sorted list

test_list3 = [1, 5, 6, 9, 11]
test_list4 = [3, 4, 7, 8, 10]

# printing original lists
print ("The original list 1 is : " + str(test_list3))
print ("The original list 2 is : " + str(test_list4))

# using sorted()
# to combine two sorted lists
res = sorted(test_list3 + test_list4)

# printing result
print ("The combined sorted list is : " + str(res))



#Q18. Implement a code to find the intersection of two given lists.

def intersection(lst3, lst4):
    lst5 = [value for value in lst3 if value in lst4]
    return lst5

# Driver Code
lst3 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst4 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(lst3, lst4))


#Q19. Create a code to find the union of two lists without duplicates.

def Union(lst6, lst7):
    final_list = lst6 + lst7
    return final_list

# Driver Code
lst6 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst7 = [2, 48, 15, 12, 26, 32, 47, 54]
print(Union(lst6, lst7))

#Q20. Write a code to shuffle a given list randomly without using any built-in shuffle functions.

import random
test_list6 = [1, 4, 5, 6, 3]

print("The original list is : " + str(test_list6))

# using random.sample()to shuffle a list
res = random.sample(test_list6, len(test_list6))

print("The shuffled list is : " + str(res))

#Q21. Write a code that takes two tuples as input and returns a new tuple containing elements that are common to both input tuples

test_tuple1 = (4, 5)
test_tuple2 = (7, 8)

# printing original tuples
print("The original tuple 1 : " + str(test_tuple1))
print("The original tuple 2 : " + str(test_tuple2))

# All pair combinations of 2 tuples
# Using list comprehension
res =  [(a, b) for a in test_tuple1 for b in test_tuple2]
res = res +  [(a, b) for a in test_tuple2 for b in test_tuple1]

# printing result
print("The filtered tuple : " + str(res))


#Q22. Create a code that prompts the user to enter two sets of integers separated by commas. Then, print the intersection of these two sets

s1 = {1, 2, 3}
s2 = {2, 3, 5}
print(s1.intersection(s2))


#Q23. Write a code to concatenate two tuples. The function should take two tuples as input and return a new tuple containing elements from both input tuples

test_tup1 = (1, 3, 5)
test_tup2 = (4, 6)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Ways to concatenate tuples
# using + operator
res1 = test_tup1 + test_tup2

# printing result
print("The tuple after concatenation is : " + str(res1))

#Q26. Write a code that prompts the user to input two sets of characters. Then, print the union of these two sets.

A1 = {'ab', 'ba', 'cd', 'dz'}
B1 = {'cd', 'ab', 'dd', 'za'}

print("Union of A1 and B1:", A1.union(B1))


#Q27. Develop a code that takes a tuple of integers as input. The function should return the maximum and minimum values from the tuple using tuple unpacking.

test_list8 = [(2, 3), (4, 7), (8, 11), (3, 6)]

# create a list of all values in the tuples
values = [val for tup in test_list8 for val in tup]

# sort the list of values
sorted_values = sorted(values)

# find the min and max values
min_val = sorted_values[0]
max_val = sorted_values[-1]

# printing result
print("The minimum value is: ", min_val)
print("The maximum value is: ", max_val)

#Q28. Create a code that defines two sets of integers. Then, print the union, intersection, and difference of these Two sets.

A1 = {'ab', 'ba', 'cd', 'dz'}
B1 = {'cd', 'ab', 'dd', 'za'}

## UNION OF TWO
print("Union of A1 and B1:", A1.union(B1))

## INTERSECTION OF TWO
print("A1 intersection B1 : ",
      A1.intersection(B1))

## DIFFERANCE OF TWO
print("Differance of A1 and B1:", A1.difference(B1))


#Q29. Write a code that takes a tuple and an element as input. The function should return the count of occurrences of the given element in the tuple&

tuple5=(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
x1=list(filter(lambda i: (i==10),tuple5))
x2=list(filter(lambda i: (i==8),tuple5))

print("the element 10 occurs",len(x1),"times")
print("the element 8 occurs",len(x2),"times")


#Q30. Develop a code that prompts the user to input two sets of strings. Then, print the symmetric difference of these two sets.
set_A = {"ram", "rahim", "ajay", "rishav", "aakash"}
set_B = {"aakash", "ajay", "shyam", "ram", "ravi"}
print("Symmetric Difference TWO String is:",(set_A ^ set_B))


#Q31. Write a code that takes a list of words as input and returns a dictionary where the keys are unique words and the values are the frequencies of those words in the input list

def CountFrequency(my_list):

    # Creating an empty dictionary
    count = {}
    for i in [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]:
        count[i] = count.get(i, 0) + 1
    return count


# Driver function
if __name__ == "__main__":
    my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
    print(CountFrequency(my_list))


#Q32. Write a code that takes two dictionaries as input and merges them into a single dictionary. If there are common keys, the values should be added together

from collections import Counter

# initializing two dictionaries
dict1 = {'a': 12, 'for': 25, 'c': 9}
dict2 = {'Geeks': 100, 'geek': 200, 'for': 300}


# adding the values with common key

Cdict = Counter(dict1) + Counter(dict2)
print(Cdict)


#Q33. Write a code to access a value in a nested dictionary. The function should take the dictionary and a list of keys as input, and return the corresponding value. If any of the keys do not exist in the dictionary, the function should return None

test_dict = {'Gfg' : {'is' : 'best'}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using nested get()
# Safe access nested dictionary key
res5 = test_dict.get('Gfg', {}).get('is')

# printing result
print("The nested safely accessed value is :  " +str (res5))


#Q34. Write a code that takes a dictionary as input and returns a sorted version of it based on the values. You an choose whether to sort in ascending or descending order

from collections import OrderedDict
d = { '123': { 'key1': 3, 'key2': 11, 'key3': 3 },
      '124': { 'key1': 6, 'key2': 56, 'key3': 6 },
      '125': { 'key1': 7, 'key2': 44, 'key3': 9 },
    }
d_ascending = OrderedDict(sorted(d.items(), key=lambda kv: kv[1]['key3']))
d_descending = OrderedDict(sorted(d.items(),
                                  key=lambda kv: kv[1]['key3'], reverse=True))
print("ASCENDING IS :",d_ascending)
print("DESCENDING IS :",d_descending)
