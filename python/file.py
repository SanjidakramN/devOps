# s1="devops"
# s2="batch"
# s3="3"
# s=s1+" "+s2+" "+s3
# print(s)
# print(len(s))
# print(s.upper().find("B"))
# print(s.split()[0])
# print(s.index(s[-1]))
# print(s.split()[1])
# print(s.index("b"))



# from collections import Counter

# List of strings
# list = ["sanju", "sanu", "linu", "anu"]

# # Join all strings in the list to form a single string
# all_chars = ''.join(list)

# # Use Counter to count the frequency of each character
# char_count = Counter(all_chars)

# # Find the most common character
# most_common_char = char_count.most_common(1)[0]

# print(f"The most common character is '{most_common_char[0]}' with {most_common_char[1]} occurrences.")
# print(list[1:3])


# weak_days=("monday","tuesday","wednesday","thursday","friday")
# holidays=tuple(["saturday","sunday"])
# print(holidays)
# print(weak_days + holidays)

# print(weak_days[0:2])

# print(list(weak_days))

set1= set()
for i in range(1,8):
    set1.add(i)

for i in range(1,8):
    print(set1)
    set1.pop(i)

print(len(set1))