# exercise 1

"Python"[1]
"Strings are sequences of characters."[5]
len("wonderfull")
"Mystery"[:4]
"p" in "Pineapple"
"apple" in "Pineapple"
"pear" not in "Pineapple"
"apple" > "Pineapple"
"pineapple" > "Peach"

# exercise 2 - first my try and then his answer

prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if prefixes[5]:
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)

# If you (like me) wondered what on earth this was in reference to: https://youtu.be/LBNjJmR5Yzw?t=249
# It is a children's tale about a family of ducks and these are the names of the ducklings.
prefixes = list("JKLMN")
prefixes.extend(["Ou", "P", "Qu"])

suffix = "ack"

for letter in prefixes:
    print(letter + suffix)

# exercise 3
def count_letters(word, letter):
    count = 0
    for word_letter in word:
        if word_letter == letter:
            count += 1
    return count

print(count_letters("banana", "a"))

# exercise 4
def count_letters(word, letter):
    count = 0
    prev = word.find(letter)  # find the first occurrence
    while prev >= 0:  # if a new occurrence was found look at the remaining part of the string
        prev = word.find(letter, prev + 1)
        count += 1
    return count

print(count_letters("banana", "a"))

# exercise 7
def reverse(text):
    txet = ""
    for i in range(len(text) - 1, 1, -1):
        txet += text[i]
    return txet


def mirror(text):
    return text + reverse(text)


def remove_letter(letter, text):
    stripped = ""
    for letter_in_text in text:
        if letter_in_text != letter:
            stripped += letter_in_text
    return stripped


def is_palindrome(text):
    return text == reverse(text)


def remove(substring, text):
    return text.replace(substring, "", 1)


def remove_all(substring, text):
    return text.replace(substring, "")


print(reverse("happy"))
print(reverse("Python"))
print(reverse(""))
print(reverse("a"))
print()

print(mirror("good"))
print(mirror("Python"))
print(mirror(""))
print(mirror("a"))
print()

print(remove_letter("a", "apple"))
print(remove_letter("a", "banana"))
print(remove_letter("z", "banana"))
print(remove_letter("i", "Mississippi"))
print(remove_letter("b", ""))
print(remove_letter("b", "c"))
print()

print(is_palindrome("abba"))
print(not is_palindrome("abab"))
print(is_palindrome("tenet"))
print(not is_palindrome("banana"))
print(is_palindrome("straw warts"))
print(is_palindrome("a"))
print(is_palindrome(""))  # yes it is
print()

print(remove("an", "banana"))
print(remove("cyc", "bicycle"))
print(remove("iss", "Mississippi"))
print(remove("eggs", "bicycle"))
print()

print(remove_all("an", "banana"))
print(remove_all("cyc", "bicycle"))
print(remove_all("iss", "Mississippi"))
print(remove_all("eggs", "bicycle"))