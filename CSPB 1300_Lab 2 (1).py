
day = input("What day of the week is it?") #first we need input from the user to use to generate a response

days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] #we need a list of answers that the program can iterate through

#the conditional statements below allow the program to find the response that matches with the user's input
if day == "Friday":
    print("It's finally Friday!") #if the user entered "Friday", the computer will print out "It's finally Friday!"
elif day == "Saturday":
    print("It's the weekend!") #if the user entered "Saturday", the computer will print out "It's the weekend!"
elif day == "Monday":
    print("The week is just getting started...") #if the user entered "Monday", the computer will print out "The week is just getting started..."
else:
    print("It's not Friday yet. You have to wait...") #if the user entered "Sunday", "Tuesday", "Wednesday", or "Thursday", the computer will print out "It's not Friday yet. You have to wait..."