
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: ………18097584……………..…         
  
# Date:  ……………2020/12/11………..…




# Part 1

# A program that allow students to predict their progression outcome at the end of each academic year.

# Create variables

pass_credits=0
defer_credits=0
fail_credits=0

# Ask user to enter credits for pass,defer and fail
pass_credits = int(input("Please enter your credits at Pass\t: ")) 
defer_credits = int(input("Please enter your credits at Defer\t: ")) 
fail_credits = int(input("Please enter your credits at Fail\t: ")) 


# Check whether all the credits less than or equal to 120 and greater than or equal to 0
if((pass_credits<=120 and pass_credits>=0) and (defer_credits<=120 and defer_credits>=0) and (fail_credits<=120 and fail_credits>=0)):

    # Check whether all the credits are devisible by 20 and total of all credits are equal to 120
    if((pass_credits % 20 == 0) and (defer_credits % 20 == 0) and (fail_credits % 20 == 0) and (pass_credits + defer_credits + fail_credits == 120)):

        # check the total credits of defer and fail is equal to 0
        if(defer_credits + fail_credits ==0): 
            print("Progress")

        # check the total credits of defer and fail is equal to 20
        elif(defer_credits + fail_credits ==20):
            print("Progress(module trailer)")
        
        # check the total credits of defer and fail is equal to 40,60,80,100 or 120   
        elif((defer_credits + fail_credits ==40) or (defer_credits + fail_credits ==60) or (defer_credits + fail_credits ==80) or (defer_credits + fail_credits ==100) or (defer_credits + fail_credits ==120)):

            # check the total credits of fail is equal to 80,100 or 120
            if((fail_credits==80) or (fail_credits==100) or (fail_credits==120)): # check the total credits of fail is equal to '80' OR '100' OR '120'
                print("Excluded") 
            else:
                print("Do not progress – module retriever")
