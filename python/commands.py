s='Hello how are u doing sanjid akram' 
x=s.index("a")
#print(x)
s2="hellooo"
print(s2.isalnum())
s3="12232323"
print(s3.isalnum())

s4="u00b2"
# print(s4.isdecimal())
# print(s4.isdigit())
# print(s4.isnumeric())

# s5="10\u00bd"
# print(s5.isdecimal())
# print(s5.isdigit())
print(s4.isidentifier())
s5="hi all"
a=["hi","how","are","youa"]
print(s5.islower())
s6=(" ".join(a))
print(s6.strip("ha"))
print(s6.split(", "))
print(s6.title())
print(s6.swapcase())
print(s6.startswith("hi"))