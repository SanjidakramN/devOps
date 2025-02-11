#.!/bin/bash
#zip a folder

echo "Enter the folder name:"
read folder
tar czf folder.tar $folder
echo "Folder zipped successfully"


