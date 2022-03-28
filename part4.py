# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: ………18097584……………..…         
  
# Date:  ……………2020/12/11………..…




# A program to predict progression outcomes for multiple students.

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
final_list=[]
progress_list=[]
trailer_list=[]
retriever_list=[]
excluded_list=[]
progress_len=0
trailer_len=0
retriever_len=0
excluded_len=0




print("\n\tStaff Version with Histogram ")

#Call the pass_marks(),defer_marks(),fail_marks()functions and assign the return value to a variable
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
                if(progression=="Progress"):
                    progress=progress+1
                elif(progression=="Progress(module trailer)"):
                    trailer=trailer+1
                elif(progression=="Excluded"):
                    excluded=excluded+1
                elif(progression=="Do not progress – module retriever"):
                    retriever=retriever+1
                break
                
                    
                
        # asking user to repeat the programe
        decision=''
        print("\nWould you like to enter another set of data?")
        decision=str(input("Enter 'y' for yes or 'q' to quit and view results\t: "))

    else:
        # Exit from reapeting the programe and display the Horizontal Histogram
        
        total_progression=progress+trailer+excluded+retriever # Count the total outcome
        print("\n----------------------------------------------------------------------------------------------")
        print("\n\tHorizontal Histogram")

        # Stars append to the lists
        print("\nProgress ",progress,"        :    ",end="")
        progress_list.append("Progress ")
        for i in range(progress):
            print("*",end="")
            progress_list.append("    *")

            
        print("\nTrailer ",trailer,"         :    ",end="")
        trailer_list.append("Trailer ")
        for i in range(trailer):
            print("*",end="")
            trailer_list.append("    *")


        print("\nRetriever  ",retriever,"     :    ",end="")
        retriever_list.append("Retriever ")
        for i in range(retriever):
            print("*",end="")
            retriever_list.append("    *")


        print("\nExcluded ",excluded,"       :    ",end="")
        excluded_list.append("Excluded ")
        for i in range(excluded):
            print("*",end="")
            excluded_list.append("    *")

        
        print("\n")
        print("\n",total_progression,"  outcomes in total.") # Print the total outcome
        print("\n----------------------------------------------------------------------------------------------")

        # Display the Vertial Histograme
        print("\n\tVertial Histograme")

        # Get th length of each list of stars appended
        progress_len=len(progress_list)
        trailer_len=len(trailer_list)
        retriever_len=len(retriever_list)
        excluded_len=len(excluded_list)

        # Get the maximum length among previous 
        max_len=max(progress_len,trailer_len,retriever_len,excluded_len)

        # Compare all the lengths with tha maximum length and append a space to the list untill equal to the maximum length
        if(max_len>progress_len):
            for i in range(progress_len,max_len):
                progress_list.append(' ')

        if(max_len>trailer_len):
            for i in range(trailer_len,max_len):
                trailer_list.append(' ')
      
        if(max_len>retriever_len):
            for i in range(retriever_len,max_len):
                retriever_list.append(' ')

        if(max_len>excluded_len):
            for i in range(excluded_len,max_len):
                excluded_list.append(' ')


        # Append all the lists with stars and spaces to the final list 
        final_list.append(progress_list)    
        final_list.append(trailer_list)
        final_list.append(retriever_list)
        final_list.append(excluded_list)

        
        for x in range(max_len): # Get the elements from the list
            for n in range(len(final_list)): # Get the list from the list
                print(final_list[n][x],end="\t")
            print("\t")
            print()


        
        break
