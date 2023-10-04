random_string = input("Enter a random string: ")

print(random_string)

char_count = {}

for char in random_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)