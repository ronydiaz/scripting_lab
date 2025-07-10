#!/bin/bash

# Set the threshold for disk usage (in percentage)
THRESHOLD=90

# Check disk usage
for PART in $(df -h | grep -vE '^Filesystem' | awk '{print $5 " " $6}')
do
    USAGE=$(echo $PART | awk '{print $1}' | sed 's/%//')
    MOUNTPOINT=$(echo $PART | awk '{print $2}')
    
    if [ "$USAGE" -gt "$THRESHOLD" ]; then
        echo "Warning: Disk usage on $MOUNTPOINT is above ${THRESHOLD}%!"
    fi
done

