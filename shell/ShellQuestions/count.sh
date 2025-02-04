#!/bin/sh
#author: sanju
#Purpose:Learning basic command 
#Usage:./count.sh

echo "Enter the string"
read -r string

count=$( wc -w <<< $string )
echo "$count"