# import os
# print("Current Directory:", os.getcwd())
# f = None
# try:
#     f = open("test.txt","w")
#     f.write("Hello World")
#     f.close()
#     f = open("test.txt", "r")
#     print(f.read())
#     print(type(f.readlines()))
# except:
#     print("An error occurred")
# finally:
#     if f is not None:
#         f.close()
# 
import os

print("Current Directory:", os.getcwd())
f = None
try:
    f = open("test.txt", "w")
    f.write("Hello World")
    f.close()
    f = open("test.txt", "r")
    print(f.read())
    f.seek(0)  # Move the cursor back to the beginning of the file
    print(type(f.readlines()))
except Exception as e:
    print("An error occurred:", e)
finally:
    if f is not None:
        f.close()
    if os.path.exists("test.txt"):
        os.remove("test.txt")
        print("File 'test.txt' removed.") 


os.remove("C:\Users\Administrator\Myust\hello.txt")
print("File 'test.txt' removed.")