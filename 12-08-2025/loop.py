#Numbers Divisible by 3 or 5
def divisible_by_3_or_5_not_both(start, end):
    for num in range(start, end + 1):
        if (num % 3 == 0 or num % 5 == 0) and not (num % 3 == 0 and num % 5 == 0):
            print(num, end=" ")

divisible_by_3_or_5_not_both(1, 15)


#Reverse Words in a Sentence
def reverse_words(sentence):
    words = []
    word = ""

    # Extract words manually
    for char in sentence:
        if char == " ":
            words.append(word)
            word = ""
        else:
            word += char
    words.append(word)  

    # Reverse the list manually
    reversed_sentence = ""
    for i in range(len(words)-1, -1, -1):
        reversed_sentence += words[i]
        if i != 0:
            reversed_sentence += " "

    return reversed_sentence

print(reverse_words("hello i am here"))

#Star Diamond Pattern
def diamond_pattern(n):
    # Upper part
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    # Lower part
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

diamond_pattern(5)


#Count Consonants in a String
def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

print(count_consonants("hello world"))  # Output: 7


#Number Guessing Game
def number_guessing_game(secret_number):
    while True:
        guess = int(input("Guess the number: "))
        if guess == secret_number:
            print("Correct! You guessed it.")
            break
        else:
            print("Wrong, try again.")

number_guessing_game(8)  

