#Unique element function
def unique_element(list):
    result=[]
    for item in list:
        if item not in result:
            result.append(item)
            return result
print(unique_element([1,4,3,7,8,4,5,6,7,4,3,2,8]))


# List Rotation
def rotate_list(lst, k):
    k = k % len(lst)  
    return lst[-k:] + lst[:-k]

print(rotate_list([1, 2, 3, 4, 5], 2)) 



# Find Longest Word
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word("Python is an amazing programming language"))  



# Sum of Digits
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

print(sum_of_digits(12345))  



# character freq counter
def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print(char_frequency("hello"))



