#!/bin/sh
#author: sanju
#Purpose:Learning while loop 
#Usage: ./for.sh



for i in  1 2 3 4 5
do 
	echo "$i"
done

for i in {1..5};
do
	echo "$i"
done

for (( i =1; i<=10; i++ ));
do
	echo "$i"
done