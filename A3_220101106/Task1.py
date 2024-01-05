# Function to generate all permutations of length n
def generate_permutations(n):
    if n == 0:
        return [[]]  # If n is 0, return a list with an empty list inside.
    permutations = []  # List to store permutations.
    # Start with a stack containing the initial state.
    stack = [(list(range(1, n + 1)), [])]

    while stack:
        remaining, current = stack.pop()  # Pop the top state from the stack.
        if not remaining:  # If no elements are remaining to be added, a permutation is complete.
            permutations.append(current)
        for i, element in enumerate(remaining):
            # Remove the element from the remaining list.
            new_remaining = remaining[:i] + remaining[i + 1:]
            # Add the element to the current permutation.
            new_current = current + [element]
            # Push the new state onto the stack.
            stack.append((new_remaining, new_current))

    return permutations

# Function to check valid permutations


def check_permutations(perm_list):
    valid_permutations = []
    for perm in perm_list:
        temporary = []  # Stack to keep track of elements to be compared.
        # List to represent the elements in their original order.
        current = list(range(1, len(perm) + 1))
        k = 0
        for i in range(len(perm)):
            # Add the current element to the stack.
            temporary.append(current[i])
            # Check if the top element in the stack matches the current element.
            while temporary and temporary[-1] == perm[k]:
                # If they match, remove the element from the stack.
                temporary.pop()
                k += 1  # Move to the next element in the permutation.
        if not temporary:  # If the stack is empty, the permutation is valid.
            valid_permutations.append(perm)

    return valid_permutations


input_str = input(
    "Enter the permutation as a comma-separated list (e.g., '1,2,3,4'): ").strip()

if not input_str:
    print("Please provide a valid input.")
else:
    elements = input_str.split(',')
    try:
        # Convert input to a list of integers
        permutation_list = list(map(int, elements))
    except ValueError:
        print("Invalid input format. Please enter comma-separated integers.")
    else:
        n = len(permutation_list)

        if len(set(permutation_list)) != n:
            print("Error: Repeated elements are not allowed.")
        elif n > 5:
            print("Warning: This code was designed for small values of n (<= 5). It may work for larger inputs, but it could be slower and may not be optimal.")
        else:
            permutations = generate_permutations(n)
            valid_permutations = check_permutations(permutations)

            print("Number of valid permutations:", len(valid_permutations))
            for perm in valid_permutations:
                print(perm)
