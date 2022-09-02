#Lesson: Create a game in which you take prompt the user questions and
#adnd if given the right answer, return a CORRECT 

# Start the game
print("Welcome to my computer quiz!")

# Prompt the user to play the game
playing = input("Do you want to play? ")

# Check if the user typed yes, if not end program
if playing != "yes":
     quit()

# Respond to question
print("Okay let's play : )")


# Start asking questions
answer = input("How many parts are there to a computer? ")
if answer == "5":
    print("You got it correct!")
else: 
    print("You are incorrect, try again") 

answer = input("Enter the basic parts of a computer, seperated by space ")
print("\n")
answerList = answer.split()
if answerList.__contains__(["CPU", "RAM", "GPU", "storage", "motherboard"]):
    print(answerList)


answer = input("What does CPU stand for? ")
if answer == "Central Processing Unit":
    print("You got it correct!")
else: 
    print("You are incorrect, try again") 

answer = input("What does the Motherboard do? ")
#"Integrates all the physical components to communicate and operate together
if answer.__contains__("Integrates all physical components to communicate and operate together"):
    print("You got it correct!")
else: 
    print("You are incorrect, try again") 

answer = input("What does the CPU do? ")
#"All data is processed. The instructions given to a computer is processed in the CPU. 
# The basic controlling, logical, arithmetic operations are executed in the CPU
if answer.__contains__("Brain of the computer"):
    print("You got it correct!")
else: 
    print("You are incorrect, try again") 

answer = input("What does the GPU do? ")
#Used to enhance the performance of the CPU. Boosts the CPU performance by providing a parallel processing facility.
#Offloads some time consuming parts of program codes to improver performance of CPU.

if answer.__contains__("Offloads time consuming parts of program. Produces high quality visuals"):
    print("You got it correct!")
else: 
    print("You are incorrect, try again") 

answer = input("What does the RAM do? ")
#RAM stands for Random Access Memory.
#It refers to the main memory of a computer
#Stores the application programs, operating system, data being used
#Shorter time to read data from ram than write data inti 
#CPU can access data stored in RAM quickly
#RAM holds less data

if answer.__contains__("the main memory of a computer"):
    print("You got it correct!")
else: 
    print("You are incorrect, try again") 


answer = input("What does the storage do? ")
#Solid State Storage and Hard Disk Drive are the key storage components
#HDD stores data permanently
#Even if you turn off the computer, the data will be saved
#Important data, software programs, operating systems are stored on the hard disk drive
#HDD are secondary storage devices.

if answer.__contains__("2 types: Hard disk and solid state"):
    print("You got it correct!")
else: 
    print("You are incorrect, try again") 

answer = input("What is a computer? ")
#A device that stores, retrieves, and manipulates data
#It can perform arithmetic operations or logical functions based
#on the instructions and input data provided by users

if answer.__contains__("a device that stores, retrieves, and manipulates data"):
    print("You got it correct!")
else: 
    print("You are incorrect, try again") 
