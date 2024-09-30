#!/usr/bin/env bash

#defining variables
name="rony"

#printign variable
echo "hello ${name}"

#printing pass arguments
#echo "this is my number ${1}"

#if conditionant
file=$1
if [[ -f $file ]]; then
	echo "$file exist"
else
	echo "$file doesn't exist"
fi

#for conditionant
for i in {1..10}
do
	echo "index: ${i}"
done

#operators
num1=5
num2=6
sum=$((num1 + num2))
echo "the sum result is: ${sum}"

#reading input
echo "Enter name: "
read variable
echo "Hello, ${variable}"


