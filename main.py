# Code to Check the Birthday Paradox
import random


# Declare an empty list
l = []

sample = int(input("Enter the Number of persons: "))

# Run a for loop for the number of samples
for i in range(sample):
    # Keep adding the random integer value representing the day of the year from 1 to 365
    l.append(random.randint(1, 365))
# Sort the list in ascending order
l.sort()
# Print the sorted list
print(l)

# Declare variables
i = 0
flag = 0
count = 0

# Now code to check if there is a repetition in the given sample list
while i < len(l) - 1:
    if l[i] == l[i + 1]:
        print("There is a Repetition of Birthday in the Sample :", l[i], l[i + 1])
        flag = 1
        # Keep the count of matches
        count = count + 1
        pass
    i = i + 1
# print the count of matches
if count != 0:
    print(count, "Persons Birthday matches in the Sample")
# When no repetition is present in the sample
if flag == 0:
    print("There is No Repetition of Birthday in the Sample")
