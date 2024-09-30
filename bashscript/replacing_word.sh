#!/bin/bash

word_input=$1
word_output=$2
file_name=$3

if [[ -w "$file_name" ]] then
	echo "Replacing ${word_input} in ${file_name} file"
	sed -i "s/${word_input}/${word_output}/g" $file_name
else
	echo "This ${file_name} is not writable"
fi





