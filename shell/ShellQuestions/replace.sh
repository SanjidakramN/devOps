#!/bin/sh
#author: sanju
#Purpose:Learning basic command 
#Usage:./replace.sh

echo "Enter the file name"
read "myfile"
echo "Enter the word to be replaced"
read "old"
echo "Enter the new word"
read "new"

sed -i "s/$old/$new/g" $myfile
