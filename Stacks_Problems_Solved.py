## STACKS SOLUTIONS: 


# Problem soved ususing 12th Chair:

# Define our variables.
num_chairs_to_stack = 25
broken_chair_num = 12
stacked_chairs_stack = []
# Loop through each value and add it to our stack one by one.
for number in range(1, num_chairs_to_stack + 1):
    stacked_chairs_stack.append(number)

# Pop off each value only until the number we need.
# This time we will override each pop value until we hit the last one. 
while len(stacked_chairs_stack) >= broken_chair_num:
    value = stacked_chairs_stack.pop()
# Print it :)     
print ('The broken chair we removed from the stack is:', value )

# Expected output: 
# "The broken chair we removed from the stack is: 12"


# BONUS PROBLEM SOLUTION:

# Define our variables.
num_chairs_to_stack = int(input("How many Chairs do we need to stack today: "))
broken_chair_num = int(input("Oh no! A broaken chair! Which chair is broken: "))
stacked_chairs_stack = []
# Loop through each value and add it to our stack one by one.
for number in range(1, num_chairs_to_stack + 1):
    stacked_chairs_stack.append(number)

# Pop off each value only until the number we need.
# This time we will override each pop value until we hit the last one. 
while len(stacked_chairs_stack) >= broken_chair_num:
    value = stacked_chairs_stack.pop()
# Print it :)     
print ('The broken chair we removed from the stack is:', value )

# Expected (Example) output: 
# "How many Chairs do we need to stack today: 25" 
# "Oh no! A broaken chair! Which chair is broken: 18"
# "The broken chair we removed from the stack is: 18"