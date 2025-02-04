#!/bin/bash
#author: sanju
#Purpose:Learning for loop 
#Usage: ./for.sh

fruits=("apple" "banana" "cherry" "mango")
for fruit in "${fruits[@]}"; do
	echo "I liked to eat $fruit"
done

fruits=("apple" "banana" "cherry" "mango")
for i in  "${!fruits[@]}"; do
	echo "fruit ate @$i is ${fruits[${i}]}"
done


for i in  "${!fruits[@]}"; do
if [ `expr ${i} % 2` == 0 ]; then
	echo "i like fruits ${fruits[${i}]}"
else 
        echo "i does not like fruits ${fruits[${i}]}"
fi
done