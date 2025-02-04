#!/bin/sh
#author: sanju
#Purpose:Learning basic command 
#Usage:./uppercase.sh

echo "Enter the string"
read string

uppercase=$(echo $string | tr 'a-z' 'A-Z')

echo "Uppercase: $uppercase"