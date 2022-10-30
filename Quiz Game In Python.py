print("Welcome To The Science Quiz Created By Vaibhav")

user_name = input("Enter Your Name : ")
yes_no = input("Do you want to play: ")
if yes_no != "Yes":
    print("Type Yes To Play Or Go Away")
    quit()

if yes_no == "Yes":
    print("Okay,", user_name, "Lets Play")
print("What does DNA stand for?")
answer = input("Your Answer : ")
if answer == "Deoxyribonucleic acid":
    print("Correct!! :)")
else:
    print("Sorry , But You are not able to answer this simple question :(")
print("Who Albert Einstein called the father of modern science?")
answer = input("Your Answer : ")
if answer == "Galileo Galilei":
    print("Correct!! :)")
else:
    print("Sorry , But You are not able to answer this simple question :(")

print("Which subatomic particle is positively charged?")
answer = input("Your Answer : ")
if answer == "Proton":
    print("Correct!! :)")
elif answer == "proton":
    print("Correct!! :)")
else:
    print("Sorry , But You are not able to answer this simple question :(")
print("Which subatomic particle is negatively charged?")
answer = input("Your Answer : ")
if answer == "Electron":
    print("Correct!! :)")
elif answer == "electron":
    print("Correct!! :)")
else:
    print("Sorry , But You are not able to answer this simple question :(")
print("Who discovered the Theory Of Relativity?")
answer = input("Your Answer : ")
if answer == "Albert Einstein":
    print("Correct!! :)")
elif answer == "albert einstein":
    print("Correct , But it's a proper noun")
elif answer == "einstein":
    print("Write full name !")
elif answer == 'albert':
    print("Write Full Name!")
else:
    print("Sorry , But You are not able to answer this simple question :(")

print("Congrats You Have Completed All The 5 Questions , ")
