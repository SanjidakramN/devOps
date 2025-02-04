#!/bin/sh
#author: sanju
#Purpose:Learning basic command 
#Usage:./extractfile.sh

echo "Enter the file name"
read "myfile"

emails=$(grep -oE '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}' "$myfile")
echo "Email: $emails"
