#!/bin/bash

file_name="$1"
how_mani="$2"

echo "Printing $how_mani files called $file_name"

for i in $(seq 1 "$how_mani");
do
	touch ${file_name}_${i}.txt
done

