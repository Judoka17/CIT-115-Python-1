while True:
 #grade anylizer
    (input('Name of person that we are calculating the grades for: '))
    print('--------------------------------------------')

    test1 = int(input('What is your first test score: '))
    test2 = int(input('What is your second test score: '))
    test3 = int(input('What is your third test score: '))
    test4 = int(input('What is your fourth test score: '))

# user input on whether to drop the lowest grade
    USERINPUT = input("Would you like to drop the lowest test score? Y/N  ")

#making sure that no grade is in the negative
    if test1 < 0 or test2 < 0 or test3 < 0 or test4 < 0:
        print('All numbers must be above 0')
        exit()

    #imputs if the user decides to drop the lowest grade *this came from Russul he was a big help
    if USERINPUT == "y" or USERINPUT == "Y":
        if test1 < test2 and test1 < test3 and test1 <test4:
            AVERAGE = (test2 + test3 + test4)/3
        elif test2 < test1 and test2 < test3 and test2 < test4:
            AVERAGE = (test1 +  test3 + test4)/3
        elif test3 < test1 and test3 < test2 and test3 <test4:
            AVERAGE = (test1 + test2 + test4)/3
        else:
            AVERAGE = (test1 + test2 + test3)/3
        
        #user input if they choose to not drop the lowest grade
    if USERINPUT =="N" or USERINPUT == "n":
        AVERAGE = (test1 + test2 + test3 + test4)/4
    #test score clalculations
    
    #display
    print(f'The average of the your test scores is {AVERAGE:,.2f}')

    #Grade letter things
    if AVERAGE >= 97.0:
        print('A+')
    elif AVERAGE >= 94.0:
        print('A')
    elif AVERAGE >= 90.0:
        print('A-')
    elif AVERAGE >= 87.0:
        print('B+')
    elif AVERAGE >= 84.0:
        print('B')
    elif AVERAGE >= 80.0:
        print('B-')
    elif AVERAGE >= 77.0:
        print('C+')
    elif AVERAGE >= 74.0:
        print('C')
    elif AVERAGE >= 70.0:
        print('C-')
    elif AVERAGE >= 67.0:
        print('D+')
    elif AVERAGE >= 64.0:   
        print('D')
    elif AVERAGE >= 60.0:
        print("D-")
    else:
        print('F')
    #code stop of continue
    STOP_CODE = input('Would you like to continue Yes/No ')
    if STOP_CODE != "YES" and STOP_CODE != "yes":
        break

