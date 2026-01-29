print("Welcome to my game!")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's play :)")
score = 0


answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")



answer = input("Which is the smallest prime number? ")
if answer.lower() == "2":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")



answer = input("Whihc ocean is the largest? ")
if answer.lower() == "pacific":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")    



answer = input("whihc language has the most native speaker in the world? ")
if answer.lower() == "chinese":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")



answer = input("Which country is known as the land of the Rising Sun? ")
if answer.lower() == "japan":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")    


    
answer = input("What is the hardest natural substance on Earth? ")
if answer.lower() == "diamond":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")    




answer = input("What is the capiatl of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("You got", score, "out of 7 questions")
print("You got " + str((score/7)*100) + "%")
