TASK1
File: search.sh

1. Place the Script in the Same Folder:
First, make sure the search.sh file is in the same folder as the text file you want to search. You can use the provided file.txt file for testing.

2. Make the Script Executable:
In your command line, navigate to the folder where the script is located.
Run the following command to give the script permission to execute:

$ chmod +x search.sh

3. Perform a Search:
Now, you can search for specific words or phrases in your text file. Use the following command format:

$ ./search.sh <string_to_find> <file_name>
Replace <string_to_find> with the word or phrase you want to search for, and <file_name> with the name of the text file you want to search in.

For Example:
If you want to search for the word "hello" in the sample.txt file, you can run the following command:

$ ./search.sh hello file.txt

What the Script Does:
This script helps you find specific words or phrases in a text file. It will tell you which lines in the file contain the word or phrase you're looking for and display them along with their line numbers.

Important Notes:
Make sure to place the script in the same folder as your text file.
Use the chmod +x command to make the script executable.
You can search for any word or phrase in the text file by replacing <string_to_find> and <file_name> with your desired values.
The script is simple and works well for small to medium-sized text files.
If you have a different text file to search, replace sample.txt with the name of your file in the command.
Have fun searching for text in your files!


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


TASK2

Bash Script for Sending Messages to Logged-In Users

Usage:
Assuming the script is saved in a file named "message.sh," run the following command to send a message to all logged-in users:

./message.sh <file_name>
It requires one argument, which is the name of a file containing the message you want to send.

If you do not provide exactly one argument or if the provided file is not readable, the script will display an error message.

Argument Check:
The script first checks if exactly one argument (the message file) is provided.
If not, it shows a usage message and exits.

Message File:
The specified message file is stored in a variable called testtext.txt.

File Readability Check:
The script checks if the argument (message file) is readable.
If not, it displays an error message and exits.

User List:
It retrieves a list of currently logged-in users using the who command.
It extracts and stores their usernames in a temporary file called tmp_users.txt.

Message Reading:
The message to be sent is read from the message file and stored in a variable called message.

Sending Messages:
The script iterates through the list of logged-in users.
For each user, it checks if the user is the same as the one executing the script (the current user).
If the user is not the current user, it sends the message to that user using the write command.
If the user is the current user, it displays the message on the terminal.

Clean-Up:
After sending the message to all users, the temporary file tmp_users.txt is cleaned up and deleted.

Example:
To send a message to all logged-in users with the content of a file named "my_message.txt," you can run:

./message.sh my_message.txt

Important Notes:
Make sure the script is in the same directory as the message file.
Use the chmod +x command to make the script executable if needed.
The script is designed for sending messages to users on a Linux system who are currently logged in.
After sending the message, the script cleans up the temporary user list file.






