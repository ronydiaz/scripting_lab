#!/bin/bash

#!/bin/bash

read -p "Introduce a filename: " file_name
read -p "Introduce how many files do you want to create: " how_many

# Check for empty filename
if [ -z "$file_name" ]; then
    echo "Introduce a valid name"
    exit 1
fi

# Check if how_many is a number and not empty
if ! [[ "$how_many" =~ ^[0-9]+$ ]]; then
    echo "Introduce a valid number"
    exit 1
fi

echo "Creating $how_many files called $file_name..."

for i in $(seq 1 "$how_many"); do
    touch "${file_name}_${i}.txt"
done

