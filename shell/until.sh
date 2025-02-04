#!/bin/sh
#author: sanju
#Purpose:Learning until 
#Usage: ./until.sh

echo -e "please enter the ip adress to ping/c"
read -r ip
until ping $ip
do 
	echo "host in $ip is down" 
	sleep 1
done
echo "host in $ip"