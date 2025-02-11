# try:
#     print(str(10 + 10))
# except TypeError:
#     print("Exception occured")
# except ValueError:
#     print("Value Error")
# except ZeroDivisionError:
#     print("Zero Division Error")

import os

def create_file(directory, filename, content):
    # Check if the directory exists, if not create it
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")
    
    # Create the file with the specified content
    with open(os.path.join(directory, filename), 'w') as file:
        file.write(content)
    print(f"File '{filename}' created with your content.")