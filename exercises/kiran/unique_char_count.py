
#random_string = "hkalshdfjdskfjhdkjhdcvjnmcvxvnxvquwryqeuwyqiuweynerfpoipotitpezmxnbvmxcv"

random_string = input("Enter a random string: ")

unique_characters = ""

for char in random_string:
    if char not in unique_characters:
        unique_characters += char
print("Here are the unique characters in the string: ", unique_characters)

for uniqchar in unique_characters:
    #char_count=random_string.count(uniqchar)
    char_count=0
    for char in random_string:
        if char == uniqchar:
            char_count+=1
    print(uniqchar, "occurred", char_count, "times")

