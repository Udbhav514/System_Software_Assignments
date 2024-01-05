#!/bin/bash

# Check if exactly one argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <message_file>"
    exit 1
fi

# Store the provided message file in a variable
message_file="$1"

# Check if the argument is a readable file
if [ ! -r "$message_file" ]; then
    echo "Error: The argument '$message_file' is not a readable file."
    exit 1
fi

# Get a list of currently logged-in users and store their usernames in a temporary file
who | awk '{print $1}' | sort -u > tmp_users.txt

# Read the message from the message file
message=$(<"$message_file")

# Loop through the list of logged-in users and send the message to each user
while IFS= read -r user; do
    # Skip the current user (the one executing the script)
    if [ "$user" != "$USER" ]; then
        echo "Sending message to user: $user"
        
        # Use the 'write' command to send the message to the user
        write "$user" <<<"$message"
    else
        # Display the message to the current user
        echo "You (current user): $message"
    fi
done < tmp_users.txt

# Clean up the temporary file
rm tmp_users.txt
