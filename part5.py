# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: ………18097584……………..…         
  
# Date:  ……………2020/12/11………..…



# Function to Display "progress" and count the number of progress in final outcome
def progress(mark_list):
    i=0
    progress_count=0
    while(i<=len(mark_list)-1):
        # Check the values and if they are equal to 120,0,0 respectively print "progress"
        if(mark_list[i]==120):
            if((mark_list[i+1]==0)and (mark_list[i+2]==0)):
                print("Progress")
                progress_count += 1
        i=i+3 # Add 3 to 'i' to get the next pass value
    return progress_count


# Function to Display "Progress (module trailer)" and count the number of trailers in final outcome
def trailer(mark_list):
    i=0
    trailer_count=0
    while(i<=len(mark_list)-1):
        # Check the values and if they are equal to 100,20,0 or 100,0,20 respectively print "progress (module trailer)"
        if(mark_list[i]==100):
            if(((mark_list[i+1]==20)and (mark_list[i+2]==0))or ((mark_list[i+1]==0) and (mark_list[i+2]==20))):
                print("Progress (module trailer)")
                trailer_count += 1
        i=i+3 # Add 3 to 'i' to get the next pass value
    return trailer_count



# Function to Display "Do not Progress - module retriever" and count the number of retrievers in final outcome
def retriver(mark_list):
    i=0
    retriver_count=0
    while(i<=len(mark_list)-1):
        # Check the values that are equal to 80,20,20 or 60,40,20 or 40,40,40 or 20,40,60 respectively.
        if(mark_list[i]==80):
            if((mark_list[i+1]==20)and (mark_list[i+2]==20)):
                print("Do not Progress - module retriever")
                retriver_count += 1
        elif(mark_list[i]==60):
            if((mark_list[i+1]==40)and (mark_list[i+2]==20)):
                print("Do not Progress - module retriever")
                retriver_count += 1
        elif(mark_list[i]==40):
            if((mark_list[i+1]==40)and (mark_list[i+2]==40)):
                print("Do not Progress - module retriever")
                retriver_count += 1
        elif(mark_list[i]==20):
            if((mark_list[i+1]==40)and (mark_list[i+2]==60)):
                print("Do not Progress - module retriever")
                retriver_count += 1
        i=i+3 # Add 3 to 'i' to get the next pass value
    return retriver_count



# Function to Display "Exclude" and count the number of excluded in final outcome
def excluded(mark_list):
    i=0
    exclude_count=0
    while(i<=len(mark_list)-1):
        # Check the values that are equal to 20,20,80 or 20,0,100 or 0,0,120 respectively.
        if(mark_list[i]==20):
            if(((mark_list[i+1]==20)and (mark_list[i+2]==80))or ((mark_list[i+1]==0) and (mark_list[i+2]==100))):
                print("Exclude")
                exclude_count += 1
        elif(mark_list[i]==0):
            if((mark_list[i+1]==0)and (mark_list[i+2]==120)):
                print("Exclude")
                exclude_count +=1
        i=i+3 # Add 3 to 'i' to get the next pass value
    return exclude_count


# Main program

print("\n\tAlternative Staff Version")
print("\n")

#create variables in main program
p_count=0
t_count=0
r_count=0
e_count=0

# Take all the values into a one list respectively
mark_list=[120,0,0,100,20,0,100,0,20,80,20,20,60,40,20,40,40,40,20,40,60,20,20,80,20,0,100,0,0,120]

# Call all the functions and assign the return value to a variable
p_count=progress(mark_list)
t_count=trailer(mark_list)
r_count=retriver(mark_list)
e_count=excluded(mark_list)

print("\n")
total = p_count+ t_count + r_count + e_count # Find the nuber of total outputs

#Print a Horizontal Histogram with stars
print("Progress\t",p_count,":\t",end="")
for p in range(p_count):
    print("*",end="")

print("\nTrailing\t",t_count,":\t",end="")
for t in range(t_count):
    print("*",end="")

print("\nRetriever\t",r_count,":\t",end="")
for r in range(r_count):
    print("*",end="")

print("\nExcluded\t",e_count,":\t",end="")
for e in range(e_count):
    print("*",end="")

print("\n")
print("\n",total,"outcomes in total.")

    
    
