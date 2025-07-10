#!/bin/bash

uname -a > local_machine_resources.txt

cat /etc/os-release >> local_machine_resources.txt

free >> local_machine_resources.txt

df -h >> local_machine_resources.txt

lscpu >> local_machine_resources.txt
