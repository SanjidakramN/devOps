#!/bin/sh
#author: sanju
#Purpose:Learning function with parameter
#Usage:./basiclearnig.sh

echo "Current time"
current_hour=$(date +"%H")

if [ "$current_hour" -lt 12 ]; then
    echo "Good morning"
elif [ "$current_hour" -lt 16 ]; then
    echo "Good afternoon"
elif [ "$current_hour" -lt 20 ]; then
    echo "Good evening"
else
    echo "Good night"
fi