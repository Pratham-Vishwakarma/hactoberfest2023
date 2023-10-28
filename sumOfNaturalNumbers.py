num=int(input("Enter A Natural Number:")) #To take user input for natural number.

sum=0 #Intialization of counter.

if (num < 0):

    print("** Error!!! Check Your Input.**") #If input isn't a natural number, this statement will be print. 

else:

    for i in range(1,num,-1):

        sum=sum+num #Process of the counter.

    print("The sum of first", num ,"natural numbers is: ",sum) #To print the final statement.
