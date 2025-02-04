#!/bin/sh
#author: sanju
#Purpose:Learning basic command 
#Usage:./regularexpression.sh

numString="ABCDabcd"
if [[ $numString =~ ^1 ]]; then
    echo "$numString starts with 1"    
fi

if [[ $numString =~ ^[A-Za-z]+$ ]]; then
    echo "$numString starts with a and b present in the string"    
fi