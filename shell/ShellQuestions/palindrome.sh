#!/bin/sh
#author: sanju
#Purpose:Learning basic command 
#Usage:./palindrome.sh

# echo "Enter the string"
# read string

# if [ "$(echo $string | rev)" = "$string" ]; then
#     echo "Palindrome"
# else
#     echo "Not Palindrome"
# fi

echo "Enter the string:"
read string

length=${#string}
is_palindrome="true"

for (( i=0; i<length/2; i++ )); do
    if [ "${string:i:1}" != "${string:length-i-1:1}" ]; then
        is_palindrome="false"
        break
    fi
done

if [ "$is_palindrome" = "true" ]; then
    echo "Palindrome"
else
    echo "Not Palindrome"
fi