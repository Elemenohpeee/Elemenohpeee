# The following formula is used to calculate the amount of demolition (m112) used to cut a tree
# lowing formula is used for an external charge of TNT to cut a tree and remove it from a forest

# TNT = Diameter(squared) * 250. Round the answer up to the nearest whole number, then multiply by the amount of trees.

# Import the math module
import math

# First determine how many trees you will be cutting
trees = eval(input('How many trees will you be cutting?: \n'))

# Next we need to gather the circumference of the largest tree
c = eval(input('What is the circumference of the largest tree in inches?: \n'))

# Next you have to figure out the diameter
d = int(c / math.pi)

# The following formula will give you the amount pounds of TNT rounded up to the next greatest pound.
p = ((math.ceil(d ** 2 / 250)) * trees)
tnt = (p / trees)

print('you will need', p,'lbs of TNT for', trees,'trees.')
print("Distribute",tnt,'lbs to each tree.')




