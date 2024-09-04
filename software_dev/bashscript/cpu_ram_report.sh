#!/bin/bash

#Get CPU usage
cpu_usage=$(top -bn1 | grep "CPU(s)")

#Check information
echo "CPU usage: ${cpu_usage}"
