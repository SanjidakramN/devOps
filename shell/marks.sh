#!/bin/sh
#author: sanju
#Purpose:Learning basic command 
#Usage:./marks.sh

echo "Enter marks for Maths:"
read maths
echo "Enter marks for Chemistry:"
read chemistry
echo "Enter marks for Biology:"
read biology

if [ "$maths" -lt 35 ] || [ "$chemistry" -lt 35 ] || [ "$biology" -lt 35 ]; then
    echo "Result: Failed"
else
    total=$(($maths + $chemistry + $biology))
    average=$(($total / 3))

    if [ "$average" -gt 80 ]; then
        echo "Result: Distinction"
    elif [ "$average" -gt 60 ]; then
        echo "Result: First Class"
    elif [ "$average" -gt 50 ]; then
        echo "Result: Second Class"
    elif [ "$average" -gt 40 ]; then
        echo "Result: Pass"
    else
        echo "Result: Failed"
    fi
fi