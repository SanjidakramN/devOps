#!/bin/sh
#author: sanju
#Purpose:Learning function with parameter
#Usage:./touch.sh

while getopts :a:b: flag;do
    case $flag in
        a) ab=$OPTARG;;
        b) bc=$OPTARG;;
        ?) echo "invalid option"
        esac
done
    echo "first value $ab, second value $bc"