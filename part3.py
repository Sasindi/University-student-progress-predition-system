
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: ………18097584……………..…         
  
# Date:  ……………2020/12/11………..…





# Part 3

# A program that allow a staff member to predict progression outcomes for multiple students.

# Function to get credits for pass
def pass_marks():
    credits_for_pass=""
    pass_credits=0
    marks=0
    while True:
        # Check the input value is a integer or not
        while True:
            credits_for_pass= input("\nEnter your total PASS credits\t: ")
            try:
                marks=int(credits_for_pass)
                break
            except:
                print("Integer required")
                continue
        # Check that the user input integer is greater than or equal to 0 and less than or equal to 120
        if((marks<=120 and marks>=0)):
            #Check the integer value is divisible by 20 or not
            if(marks % 20 == 0):
                pass_credits=marks
                break
            else:
                print("Invalid input")
                continue
        else:
            print("out of range")
            continue
    return pass_credits 

# Function to get credits for defer
def defer_marks():
    credits_for_defer=""
    defer_credits=0
    marks=0
    while True:
        # Check the input value is a integer or not
        while True:
            credits_for_defer= input("Enter your total DEFER credits\t: ")
            try:
                marks=int(credits_for_defer)
                break
            except:
                print("Integer required")
                print("\n")
                continue
        # Check that the user input integer is greater than or equal to 0 and less than or equal to 120
        if((marks<=120 and marks>=0)):
            #Check the integer value is divisible by 20 or not
            if(marks % 20 == 0):
                defer_credits=marks
                break
            else:
                print("Invalid input")
                print("\n")
                continue
        else:
            print("out of range")
            print("\n")
            continue
    return defer_credits

# Function to get credits for fail 
def fail_marks():
    credits_for_fail=""
    fail_credits=0
    marks=0
    while True:
        # Check the input value is a integer or not
        while True:
            credits_for_fail= input("Enter your total FAIL credits\t: ")
            try:
                marks=int(credits_for_fail)
                break
            except:
                print("Integer required")
                print("\n")
                continue
        # Check that the user input integer is greater than or equal to 0 and less than or equal to 120
        if((marks<=120 and marks>=0)):
            #Check the integer value is divisible by 20 or not
            if(marks % 20 == 0):
                fail_credits=marks
                break
            else:
                print("Invalid input")
                print("\n")
                continue
        else:
            print("out of range")
            print("\n")
            continue
    return fail_credits

# Function to find the final output
def final_output(pass_m,defer_m,fail_m):
    output=""
    # check the total credits of defer and fail is equal to 0
    if(defer_m + fail_m==0): 
        output="Progress"

    # check the total credits of defer and fail is equal to 20
    elif(defer_m+ fail_m ==20):
        output="Progress(module trailer)"
        
    # check the total credits of defer and fail is equal to 40,60,80,100 or 120
    elif((defer_m + fail_m ==40) or (defer_m + fail_m ==60) or (defer_m + fail_m ==80) or (defer_m + fail_m ==100) or (defer_m + fail_m ==120)):

        # check the total credits of fail is equal to 80,100 or 120
        if((fail_m==80) or (fail_m==100) or (fail_m==120)): # check the total credits of fail is equal to '80' OR '100' OR '120'
            output="Excluded" 
        else:
            output="Do not progress – module retriever"
    return output


# main programe

decision = 'y'
progress=0
trailer=0
excluded=0
retriever=0
total_progression=0


print("Staff Version with Histogram ")

#Call the pass_marks(),defer_marks(),fail_marks()functions and assining the return value to a variable
while True:
    if(decision=='y'):
        pass_m=pass_marks()
        defer_m=defer_marks()
        fail_m=fail_marks()

        # Find the total credits of pass,defer and fail
        total=pass_m+defer_m+fail_m

        # Check the total is equal to 120 and when it is not equal, ask user to re-enter credits
        while True:
            if(total!=120):
                print("Total Incorect")
                print("\n")
                pass_m=pass_marks()
                defer_m=defer_marks()
                fail_m=fail_marks()
                total=pass_m+defer_m+fail_m
            else:
                # Call the final_output(pass_m,defer_m,fail_m) function and print the progression outcome
                progression=final_output(pass_m,defer_m,fail_m)
                print(progression)
                if(progression=="Progress"):
                    progress=progress+1
                elif(progression=="Progress(module trailer)"):
                    trailer=trailer+1
                elif(progression=="Excluded"):
                    excluded=excluded+1
                elif(progression=="Do not progress – module retriever"):
                    retriever=retriever+1
                break
                
                    
                

        decision=''
        print("\nWould you like to enter another set of data?")
        decision=str(input("Enter 'y' for yes or 'q' to quit and view results\t: "))

    else:
        total_progression=progress+trailer+excluded+retriever
        print("\n----------------------------------------------------------------------------------------------")
        print("\nHorizontal Histogram")
        print("\nProgress ",progress,"        :    ",end="")
        for i in range(progress):
            print("*",end="")
            
        print("\nTrailer ",trailer,"         :    ",end="")
        for i in range(trailer):
            print("*",end="")

        print("\nRetriever  ",retriever,"     :    ",end="")
        for i in range(retriever):
            print("*",end="")

        print("\nExcluded ",excluded,"       :    ",end="")
        for i in range(excluded):
            print("*",end="")

        print("\n")
        print("\n",total_progression,"  outcomes in total.")
        print("\n----------------------------------------------------------------------------------------------")
        break


