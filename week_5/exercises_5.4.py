# exercise 1
def count_letters(text):
    letter_counts = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter not in letter_counts:
                letter_counts[letter] = 1
            else:
                letter_counts[letter] += 1
    return letter_counts


def print_letter_counts(letter_counts):
    for letter in sorted(letter_counts):
        print(letter, letter_counts[letter])


input_text = "ThiS is String with Upper and lower case Letters"
print_letter_counts(count_letters(input_text))

# exercise 2
def add_fruit(inventory, fruit, quantity=0):
    if fruit not in inventory:
        inventory[fruit] = quantity
    else:
        inventory[fruit] += quantity

new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
print(new_inventory)
add_fruit(new_inventory, "strawberries", 25)
print(new_inventory)

import urllib.request

# retrieve the book
url = "http://www.gutenberg.org/files/11/11-0.txt"
file_name = "alice.txt"
urllib.request.urlretrieve(url, file_name)

# read the book
with open(file_name) as alice_book:
    alice_text = alice_book.read()

# process the book
words = alice_text.lower().split()
word_count = {}
for word in words:
    # Getting this right is actually pretty hard
    # (scroll throught the list of words and mess around with it to get a feel for how hard)
    # Is a - part of the word, or is it punctuation?
    # should the mark be removed or should the word be split on this sign?
    word = word.strip("!\"#$%&'()*+,./:;<=>?@[\]^_`{|}~!”")   # we need to keep "-" so string.punctution doesn't work
    if len(word) > 0 and word[0].isalpha():
        word_count[word] = word_count.get(word, 0) + 1