#!/bin/sh
#author: sanju
#Purpose:Learning basic command 
#Usage:./autopopulate.sh

echo "all argumemts compaigned together $*"
echo "number of arguments $#"
echo "first $1"
echo "expact all the command on separate words $@"
echo "process id of current process $$"

 sleep 400 &
 echo "process id of recently background process $!"
 echo "filename of the current program $0"
