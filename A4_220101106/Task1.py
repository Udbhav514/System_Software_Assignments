from itertools import permutations

# Input the number of numbers to be added
t = int(input("Enter the number of numbers to be added: "))
print("Enter the numbers one by one")

# Initialize a list to store the numbers and get user input for each number
l = []
for i in range(t):
    l.append(input())

# Get user input for the final sum
print("Enter the final sum")
sum1 = input()
l.append(sum1)

# Flag to check if the input contains only capital English letters
flag = 0

# Validate that each character in the input is a capital English letter
for x in l:
    for y in x:
        if y not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                     'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            print("Input must contain only Capital Letters")
            exit()
            flag = 1

# If the input is valid, proceed with solving the equation
if flag == 0:
    # Extract distinct letters from the input
    distinct_letters = set()
    for x in l:
        for y in x:
            distinct_letters.add(y)
    distinct_letters = list(distinct_letters)

    # List to store valid solutions
    solution = []

    # Iterate through all permutations of digits for distinct letters
    for perm in permutations("0123456789", len(distinct_letters)):
        assignment_dict = dict(zip(distinct_letters, perm))

        l2 = []
        # Convert the original numbers to their assigned values
        for y in l:
            s = ''.join(assignment_dict[z] for z in y)
            l2.append(s)

        s = 0
        # Calculate the sum of the converted numbers
        for c in l2:
            s += int(c)

        s -= int(l2[-1])

        # Check if the sum matches the final sum
        if s == int(l2[-1]):
            solution.append(assignment_dict)

    nums = []

    # Convert the numbers in each solution to their assigned values
    for assignment_dict in solution:
        pp = []
        for x in l:
            s = ''.join(assignment_dict[y] for y in x)
            pp.append(s)

        nums.append(pp)

    # Print the solutions or indicate if there is no solution
    if len(nums) == 0:
        print("Following are the possible solutions - ")
        print("No Solution")
    else:
        wow = 0
        print("Following are the possible solutions - ")
        for x in nums:
            f = 0
            for y in range(len(x)):
                if x[y][0] == "0":
                    f = 1
                    break
            if f == 1:
                continue
            wow = 1
            for y in range(len(x) - 1):
                print(x[y])
            print('+')
            print("----------")
            print(x[-1])

            print("")
            print("")
        if wow == 0:
            print("No Solution")

# Explanation: This code uses a brute force approach to solve an addition puzzle where letters represent digits.
# It validates user input to ensure it contains only capital English letters. Then, it generates and checks all
# possible digit assignments for the letters to match the given sum. The output includes the valid solutions
# avoiding solutions where the leftmost digit of any number is zero. This exhaustive search might take 10-20 seconds
# to print all the possible solutions.
