""" List Methods """
example_list = ["Python", "is", "very", "easy", "to", "learn"]
example_list_2 = ["But", "you", "have", "to", "practice", "every", "day"]

print (example_list)
print (example_list[0])
print (example_list[1])


print (example_list[0:3])
print (example_list[0:3:2])

print (example_list + example_list_2)

print (example_list * 3)

print (len(example_list))

print (example_list.index("very"))
print (example_list.count("very"))

example_list.append("and")
print (example_list)

example_list.insert(3,"super")
print (example_list)

example_list.remove("super")
print (example_list)

example_list.pop()
print (example_list)

example_list.pop(3)
print (example_list)

example_list.reverse()
print (example_list)

example_list.sort()
print (example_list)

example_list.sort(reverse=True)
print (example_list)

example_list.clear()
print (example_list)

example_list = ["Python", "is", "very", "easy", "to", "learn"]
example_list_2 = ["But", "you", "have", "to", "practice", "every", "day"]

example_list.extend(example_list_2)
print (example_list)

example_list_3 = example_list.copy()
print (example_list_3)

example_list_3.clear()
print (example_list_3)

example_list_3 = example_list
print (example_list_3)

example_list_3.clear()
print (example_list_3)

a = [1,2,3]

a + [4]
[1,2,3,4]

