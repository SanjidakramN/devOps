#!/bin/sh
#author: sanju
#Purpose:Learning function with parameter
#Usage: ./functionwithparameter.sh

function sum {
    local total=$(( $1 + $2 ))
    echo "$total"
 }
result=$(sum 5 8)
echo "the result is $result"



