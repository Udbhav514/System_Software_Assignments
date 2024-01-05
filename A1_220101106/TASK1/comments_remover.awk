# This is an AWK script to remove comments from C/C++ code.
# It helps simplify code files by eliminating both block and line comments.

# Initialize a variable to keep track of whether we're inside a block comment.
BEGIN {
    within_blockComment = 0  # Start with no block comments found
}

# Loop through each line of the input.
{
    # Check if we are currently inside a block comment. If so, look for the end (*/).                                                                                                                                                                                                                                              
    if (within_blockComment) {
        if (sub("\\*/", "")) {
            within_blockComment = 0
        } else {
            next   # Skip this line if still in a block comment
        }
    }

    # Remove block comments (/* ... */) and line comments (// ...) from the line.
    gsub("/\\*.*\\*/", "")
    gsub("//.*", "")

    # Check if the line contains the start of a block comment (/*).
    if (sub("/\\*", "")) {
        within_blockComment = 1   # Start being in a block comment
    }
}

# Loop through each line again to print the lines that are not entirely comments.
{
    # Check if the line has any non-space content (fields) after removing comments.
    if (NF > 0) {
        print  # Print the line that has actual content
    }
}
