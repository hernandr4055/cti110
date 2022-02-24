# This code will caclulate the total and subtotal of a list of prices
# 2/24/2022
# CTI-110 P2HW1 - Total Purchases
# Raymond Hernandez
#

# Create a list
# Add 5 total inputs of the list
# Determine the subtotal of all items bought
# Determine the sales tax based off subtotal
# Determine the total price with but subtotal and tax
# Sort out results in a chart

num_list = []
num = float(input("Enter the price of item #1: "))
num_list.append(num)
num = float(input("Enter the price of item #2: "))
num_list.append(num)
num = float(input("Enter the price of item #3: "))
num_list.append(num)
num = float(input("Enter the price of item #4: "))
num_list.append(num)
num = float(input("Enter the price of item #5: "))
num_list.append(num)

subtotal = sum(num_list)
tax = subtotal * 0.07
total = subtotal + tax

print('------------Results------------')
print('Subtotal :', subtotal)
print('Sales Tax :', tax)
print('Total :', (total)
print('-------------------------------')
