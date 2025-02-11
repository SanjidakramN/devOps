import re # import regular expression module

string = "Good morning all, the class is good , food is good"
match = re.search("good", string,re.I) # match the string with the pattern
print(match)
"""if match:
    print("Matching",match.group(0))"""
# match1 = re.findall("(?i)Morning", string) # find all the matching string with the pattern
# print(match1)

# match2 = re.findall("good", string, re.I)
# print(match2) # match the string with the pattern

# match3 = re.search("good.morning" , string, re.I | re.DOTALL)

# myspan  = match3.span()
# print(myspan) # get the span of the matching string

# l = []
# for i in re.finditer(re.escape("good"), string, re.I):
#     l.append(i.span())
#     print(i) # get the span of the matching string

# print(l)

match4 = re.sub("(?i)good", "bad", string) # replace the matching string with the new string
print(match4) # replace the matching string with the new string
print(string) # print the original string

sring1 =  ''''hi
hello
how are you'''
match5 = re.split("\n", sring1) # split the string with the new line
print(match5) # split the string with the new line

pattern = r'[a].*'
match6 = re.findall(pattern, string)
print(match6)

pattern1 = r'[a].*[f]' # non greedy
match7 = re.findall(pattern1, string)
print(match7)

 # non greedy

 