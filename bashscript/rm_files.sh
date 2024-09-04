#!/bin/bash

for file in *;
do
	if [[ -f "$file" ]] then
	
		if [[ "$file" == *.txt ]]; then
			rm $file
		fi
	fi

done
