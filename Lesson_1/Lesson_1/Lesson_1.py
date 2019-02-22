# The fake AI conversation.
# Recives input from user regarding their emotional state.
my_message = input("Hello World, how are you? ")
print("Wow! " + my_message + ". That is great to hear!")
# gets the users age.
my_number = input("How old are you? ")
print("OMGee! " + my_number + "! You're older than dirt!")
# converts users sting input into integer
num = int(my_number)
# calculates age in seconds
seconds_old = num * 12 * 365 * 24 * 60 * 60
# converts sting back to integer
sec_old = str(seconds_old)
print("Your " + sec_old + " seconds old! That's a big number!")
# Calculates circumference back to begining of life and then back to where they are now as a circle
# and converts it back to a string
pie = 2 * 3.14 * seconds_old
pie_now = str(pie)
# Tells how long till alternet reality
print(
    "Based on this information, it will take you " + pie_now + " seconds to get back to where you are now except in a different reality!")
# Finds out what OS user is using
my_platform = input("What platform do you run? ")
print("I agree " + my_platform + " is the best ever!")
# Finds out what type of PC user has
my_computer = input("What brand of PC do you have? ")
print(my_computer + " ooo ... you should send that back to the manufacture.")
