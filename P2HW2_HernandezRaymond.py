# Create a list
# Add #'s to the list
# Determine the lowest
# Remove lowest
# Determine the length of the list
# Get the average of the sum and total amount of grades
# Sort out results in a chart

num_list = []
num = float(input("Enter score #1: "))
num_list.append(num)
num = float(input("Enter score #2: "))
num_list.append(num)
num = float(input("Enter score #3: "))
num_list.append(num)
num = float(input("Enter score #4: "))
num_list.append(num)
num = float(input("Enter score #5: "))
num_list.append(num)
num = float(input("Enter score #6: "))
num_list.append(num)
num = float(input("Enter score #7: "))
num_list.append(num)


lowest = min(num_list)
num_list.remove(lowest)
total = sum(num_list)
length = len(num_list)
average = total/length

print('------------Results------------')
print('Lowest Score :', lowest)
print('Modified List :', num_list)
print('Scores Average :', average)
print('-------------------------------')
