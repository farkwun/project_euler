#!/bin/bash
display_usage() {
    echo -e "\nUsage: $0 [new_directory_name] \n"
}
# if less than two arguments supplied, display usage
if [  $# -eq 0 ]
then
    display_usage
    exit 1
fi

mkdir $1
cp code.py $1/.
