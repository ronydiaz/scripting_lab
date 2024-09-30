#!/bin/bash

if [[ $# -ne 2 ]]; then
    echo "Usage: $0 username password"
    exit 1
fi

USERNAME=$1
PASSWORD=$2

# Add the user
useradd -m "$USERNAME"

# Set the password for the user
echo "$USERNAME:$PASSWORD" | chpasswd

# Print success message
echo "User $USERNAME created and password set."

