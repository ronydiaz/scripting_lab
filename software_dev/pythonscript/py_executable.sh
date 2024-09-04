#!/bin/bash

for file in *;
do
	if [[ -f $file ]] then
		
		if [[ $file == *.py ]] then
			echo "Making python file executable... \n"
			chmod +x $file
		fi
	fi
		
done
