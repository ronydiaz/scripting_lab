#!/bin/bash

number_files=$1

for i in $(seq "$number_files");
do
	echo "Printing file $i"
done
