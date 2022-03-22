# get the average for your grades
def main():
    # variables

    grades = 0
    total = 0
    grade_list = []
    
    num = int(input("How many scores do you want to enter? "))

    for i in range(0, num):
        grade = int(input("Enter score #" + str(i + 1)+ ": "))
        while grade < 0 or grade > 100:
            print("INVALID Score entered!!!!!")
            print("Score must be between 1 and 100")
            grade = int(input("Enter a grade #" + str(i + 1)+ ": "))
        grade_list.append(grade)
    lowest = min(grade_list)
    print(grade_list)
    grade_list.remove(lowest)
    average = sum(grade_list)/num
    print(average)

    if average >89:
        grade = "A"
    elif average >79:
        grade = "B"
    elif average >69:
        grade = "C"
    elif average >59:
        grade = "D"
    else:
        grade = "F"

print('----------Results----------')
print('Lowest Score :', lowest)
print('Modified List :', grade_list)
print('Scores Average:', total)
print('Grade :', grade)
        
main()
