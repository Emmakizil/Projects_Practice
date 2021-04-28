'''build a program that will take the weight of a package and 
determine the cheapest way to ship that package using Sal’s Shippers.
more details -> codecademy/workflow projects
'''
weight = 1.5
# Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

# Premium Shipping - Flat charge
cost_premium = 125.00

# Drone Shipping
if weight <= 2:
  cost_premium = weight * 4.50
elif weight <= 6:
  cost_premium = weight * 9.00
elif weight <= 10:
  cost_premium = weight * 12.00
else:
  cost_premium = weight * 14.25