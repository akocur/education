# Make sure your output matches the assignment *exactly*
spend_hours = int(input())
if spend_hours < 2:
    print("That seems reasonable")
elif spend_hours < 4:
    print("Do you have time for anything else?")
else:
    print("You need to get outside more!")
