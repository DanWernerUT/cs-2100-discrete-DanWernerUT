# Implement the Permutation Generator algorithm as discussed in class and found in section 6.6 of the book.
# Note that the algorithm in the book uses 1-based arrays, whereas Python uses 0-based, so you will need to put some thought into it.
# Do not use Python's built in generators, or any other code that is not yours.

# Wrap the code in a main function so that your program prompts the user for any integer N between 1 and 9, and prints ALL permutations in lexicographic order for that N.
# If they enter 2, you'd compute and print:
# 01 10
# If they enter 3, you'd compute and print:
# 012 021 102 120 201 210
import math

def next_permutation(arr):
    # checks if on last perm
    i = len(arr) - 2
    while (i >= 0) and (arr[i] >= arr[i + 1]): #check if arr[current] < arr[left neighbor], if false proceed to next check
        i -= 1 
    if i < 0: return False #if true, the final perm has been calculated, exits loop
    
    # calculates permutations
    j = len(arr) - 1
    while (arr[i] >= arr[j]): 
        j -= 1

    arr[i], arr[j] = arr[j], arr[i] #swaps element locations
    
    # puts tail end of the perm after the last element, and shifts everthing over to fill the void
    start = i + 1
    end = len(arr) - 1
    while end > start:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return True

def generate_permutations(n):
    arr = [str(i) for i in range(n)] #create list w/ items from 0 to n-1
    results = ["".join(arr)]         # start w/ first perm
    while next_permutation(arr):     # generate while true, essentially until all perms have been generated
        results.append("".join(arr)) # add most recent perm to results 
    print(" ".join(results))         # Print all permutations on one line, separated by spaces.
    
def count_permutations(n):
    n = math.factorial(n)
    print("Permutations:", n)

n = 0
while(n > 9 or n <= 0):
    n = int(input("Enter an integer between 1 and 9: "))
generate_permutations(n)
count_permutations(n)
