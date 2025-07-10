#!/bin/bash

number_cnt=$1
sum=0

for i in $(seq 0 "${number_cnt}");
do
	sum=$((sum + i))
done

echo "The sum from 0 to ${number_cnt} is ${sum}" 

