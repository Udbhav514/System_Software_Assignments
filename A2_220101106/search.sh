#!/bin/bash

# Function to print usage information
usage() {
    # Display a message explaining how to use the script
    echo "Usage: $0 <string_to_find> <file_name>"
    exit 1
}

# Check for the correct number of arguments
if [ "$#" -ne 2 ]; then
    # Check if the number of arguments is not exactly 2
    echo "Error: Exactly 2 arguments are required."
    usage
fi

# Store the command line arguments in variables
string_to_find="$1"    # The string we want to find
file_name="$2"         # The name of the file to search in

# Check if the file exists and is not empty
if [ ! -f "$file_name" ]; then
    # Check if the file does not exist
    echo "Error: File '$file_name' does not exist."
    usage
fi

if [ ! -s "$file_name" ]; then
    # Check if the file is empty
    echo "Error: File '$file_name' is empty."
    usage
fi

# Initialize a variable to keep track of whether the string was found
found=false

# Initialize a variable to keep track of the line number
line_number=1

# Loop through each line in the file and search for the string
while read -r line; do
    # Check if the line contains the string_to_find
    if grep -qF "$string_to_find" <<< "$line"; then
        # If found, print the line number and the line itself
        echo "Match found on Line $line_number: $line"
        # Set the 'found' variable to true
        found=true
    fi
    # Increment the line number for the next iteration
    ((line_number++))
done < "$file_name"

# Check if the string was not found
if [ "$found" = false ]; then
    echo "No such string '$string_to_find' present in the file."
fi

