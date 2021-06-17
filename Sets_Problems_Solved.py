## SETS SOLUTIONS:

# Define sets.
regular_brownie_set = {"salt","flour","egg","chocolate chips","cinamon","caramel"}
caramel_brownie_set = {"salt","flour","egg","caramel","nuts"}

# Your code to perfrom the intersction here:
common_items = regular_brownie_set & caramel_brownie_set 

# Remove caramel from regualr brownies here:
if "caramel" in regular_brownie_set:
    regular_brownie_set.remove("caramel")

# Try adding duplicate caramel to caramel brownies here:
caramel_brownie_set.add("caramel")

# Print final sets.

print("Ingredints for both brownie mixes:",common_items)
# Expected output (Oder does not matter): 
# Ingredints for both brownie mixes: {'caramel', 'salt', 'egg', 'flour'}
# Notice caramel is in this list, this is because it's merged before you remove it 
# (That's how you notice.)

print("Final regular brownies:",regular_brownie_set)
# Expected output (Oder does not matter):  
# Final regular brownies: {'salt', 'egg', 'chocolate chips', 'flour', 'cinamon'}  

print("Final caramel brownies:",caramel_brownie_set)
# Expected output (Oder does not matter):  
# Final caramel brownies: {'caramel', 'salt', 'egg', 'nuts', 'flour'}