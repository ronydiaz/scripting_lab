#!/bin/bash

# Define source and destination directories
SOURCE_DIR="~/Documents/repositories/myrepos"
BACKUP_DIR="~/Documents"
DATE=$(date +%F)
BACKUP_FILE="$BACKUP_DIR/backup-$DATE.tar.gz"

# Create a backup
tar -czf "$BACKUP_FILE" -C "$SOURCE_DIR" .

echo "Backup created at $BACKUP_FILE"


