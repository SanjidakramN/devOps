#!/bin/sh
#author: sanju
#Purpose:Learning function with parameter
#Usage:./backup.sh

function backup {
    echo "Enter the filename"
     read -r myfile
    # if [ -f $myfile ]; then
    #     echo "file exists"
    #     cp $myfile /tmp/backup.sh
    # else
        echo "file does not exist"
    #fi
    cp $myfile /tmp/backup.sh
       #echo $?
    if [ $? -ne 0 ]; then
        echo "backup failed $?"
    fi        
}

backup