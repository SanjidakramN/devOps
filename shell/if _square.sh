#!/bin/bash
#author: sanju
#Purpose: Creating variable
#Usage: ./input_variable.sh

file=$1
if [ -f "$file" ]; then
       echo "file access $file"
else
      	echo "file doesnot exist"
fi


file=$1
if [[ -f "$file" ]]; then
       echo "file access $file"
else
      	echo "file doesnot exist"
fi


