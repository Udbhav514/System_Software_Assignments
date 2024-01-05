# This AWK script calculates the time difference between two time values
# and presents the results in a tab-separated format.

# Set the output field separator to a tab for organized formatting.
BEGIN {
    OFS = "\t"
    
    # Print header for the output table.
    print "Time1", "", "Time2", "", "Difference"
}

# Process each input line starting from the second line (NR > 0).
NR > 0 {
    # Extract hours, minutes, and seconds for the Time1 time.
    Time1_hour = substr($1, 1, 2)
    Time1_minute = substr($1, 3, 2)
    Time1_second = substr($1, 5, 2)
    
    # Extract hours, minutes, and seconds for the Time2 time.
    Time2_hour = substr($2, 1, 2)
    Time2_minute = substr($2, 3, 2)
    Time2_second = substr($2, 5, 2)
    
    # Convert Time1 and Time2 times to total seconds.
    Time1_total_seconds = Time1_hour * 3600 + Time1_minute * 60 + Time1_second
    Time2_total_seconds = Time2_hour * 3600 + Time2_minute * 60 + Time2_second
    
    # Calculate the time difference in seconds.
    time_difference_seconds = Time2_total_seconds - Time1_total_seconds
    
    # Calculate hours, minutes, and seconds from the time difference.
    time_difference_hours = int(time_difference_seconds / 3600)
    remaining_seconds = int(time_difference_seconds % 60)
    remaining_minutes = int((time_difference_seconds % 3600) / 60)
    
    # Format hours, minutes, and seconds as two digits with leading zeros.
    formatted_hours = sprintf("%02d", time_difference_hours)
    formatted_minutes = sprintf("%02d", remaining_minutes)
    formatted_seconds = sprintf("%02d", remaining_seconds)
    
    # Print the formatted output line.
    print Time1_hour ":" Time1_minute ":" Time1_second,
          Time2_hour ":" Time2_minute ":" Time2_second,
          formatted_hours ":" formatted_minutes ":" formatted_seconds
}
