random_char_string = "auiuaysidfaiusdyfasiufo"
# 1. Create a unique character list from the above string

unique_char_list = []

for char in random_char_string:
    if char not in unique_char_list:
        unique_char_list+=[char]
print (unique_char_list)

# 2. get the count of each character in the above string

char_count_dict = {}
for unique_char in unique_char_list:
    count = 0
    for char in random_char_string:
        if unique_char == char:
            count +=1
    char_count_dict[unique_char] = count

print (char_count_dict)

# 3. Increase the variable value with only odd numbers till 100

number = 3
result = 0
while (result < 100):
    if (number % 2 != 0):
        print (result)
        result += number
        
    number+=1 
    
    