#!/bin/bash


# Set the threshold for disk usage (in percentage)
THRESHOLD=90

# Check disk usage
df -h | grep -vE '^Filesystem' | awk '{print $5 " " $6}' | while read USAGE MOUNTPOINT; do
    # Remove % sign
    USAGE=${USAGE%\%}

    if [ "$USAGE" -gt "$THRESHOLD" ]; then
        echo "Warning: Disk usage on $MOUNTPOINT is above ${THRESHOLD}%!"
    fi
done

