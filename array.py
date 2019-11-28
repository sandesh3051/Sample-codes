#In this program, we are reversing the array
#--------------------------------------------
#we are asking input from the user for the array
arr = input("please input the array of numbers:- ")
 #in range len(arr)-1 is start index and -1 is end index and -1 is the step count
 #this way it decreases by -1 and returns the array in reverse way
for i in range (len(arr)-1,-1,-1):
    print(arr[i])