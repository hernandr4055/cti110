# CTI-110
# P3HW2 - Pizza Order
# Raymond Hernandez
# 3-22-2022
#

def main():

    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50
    
    score = int(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    elif score >= B_score:
        print('Your grade is: B')
    elif score >= C_score:
        print('Your grade is: C')
    elif score >= D_score:
        print('Your grade is: D')
    else:
        print('Your grade is: F') # TO DO: finish this

main()
