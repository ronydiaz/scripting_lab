#!/bin/bash

echo "This script must receive arguments from command line and print all of them and the total"

if [[ "$#" -eq 0 ]]; then
	echo "There were received ${#} arguments"

else
	echo "There were received ${#} arguments: "
	
	for i
	do
		echo -n "${i} "
	done
	echo ""
fi

