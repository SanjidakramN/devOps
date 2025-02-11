

#!/bin/bash


# check if number is fibonacci or not

  


echo "Enter a number:"
read n
a=0
b=1
for (( i=0; i<n; i++ ))
do
    fib=$((a+b))
    a=$b
    b=$fib
done
if [ $fib -eq $n ]
then
    echo "$n is a fibonacci number"
else
    echo "$n is not a fibonacci number"
fi



 