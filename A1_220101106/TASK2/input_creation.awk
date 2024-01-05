# This AWK script prints pairs of time values and then exits.

# Print pairs of time values in the specified format.
BEGIN {
    print "034023\t052030"  # Start Time: 03:40:23, End Time: 05:20:30
    print "051811\t061150"  # Start Time: 05:18:11, End Time: 06:11:50
    print "061711\t091050"  # Start Time: 06:17:11, End Time: 09:10:50
    print "071811\t111150"  # Start Time: 07:18:11, End Time: 11:11:50
    print "031811\t151150"  # Start Time: 03:18:11, End Time: 15:11:50
    print "091811\t123412"  # Start Time: 09:18:11, End Time: 12:34:12
    print "060021\t180042"  # Start Time: 06:00:21, End Time: 18:00:42
    print "123500\t142832"  # Start Time: 12:35:00, End Time: 14:28:32
    exit  # Exit the script after printing
}
