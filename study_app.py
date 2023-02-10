import csv
import random
import os

# Check if the file exists, if not, it creates one
if not os.path.exists("questions.csv"):
    
    fieldnames = ["Question", "Responses", "Answer", "Topics"]

    with open ("questions.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        writer.writeheader()

    
# Access the questions.csv file and prompt the user for input to create a new question
# Use a loop to ensure valid input
def add_question():
    
    flag = True
    
    while flag:
        try:
            
            question = input("What is the question?")

            if len(question) < 10:

                raise ValueError("Questions must be at least 10 characters long")
                
            flag = False 
            
        except ValueError as err:
                print(err)
            
    flag = True
    
    while flag:
        
        try:
        
            responses = input("Please enter 4 possible responses seperated by commas")

            if responses.count(",") != 3:

                raise ValueError("Responses must be seperated by commas")
            
            flag = False
            
        except ValueError as err:
                print(err)
                
    flag = True
    
    while flag:
        possible_answers = ["a", "b", "c", "d"]
        
        try:
            
            answer = input("Which one is the correct answer?")

            if answer not in possible_answers:
                raise ValueError("Please only enter a, b, c or d")
                
            flag = False
        
        except ValueError as err:
            print(err)
            
    flag = True
    
    while flag:
        try:
            topics = input("What are the topics covering this question? If there are more than one, seperate them by commas")
            if len(topics) == 0:
                raise ValueError("Please enter topics seperated by commas")
                
            flag = False
                
        except ValueError as err:
            print(err)
        
    
    data = {"Question" : question, "Responses" : responses, "Answer" : answer, "Topics" : topics}
    
    fieldnames = ["Question", "Responses", "Answer", "Topics"]
    
    with open ("questions.csv", "a") as csv_file:
        
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        
        writer.writerow(data)
        

# Access the questions.csv file to load all questions into the list 
# Choose a random question to display to the user
# Use the input function while displaying answer options
def initiate_study_session():
    review_session = []
    
    with open ("questions.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        
        for line in reader:
            review_session.append(line)
            
        
    continue_session = True
    while continue_session == True:
        
        question = random.choice(review_session)
        print(question["Question"])
        
        responses = question["Responses"].split(",")
        
        answer = input(f"What is your answer? a.{responses[0]}, b.{responses[1]}, c.{responses[2]}, d.{responses[3]}\n")
        if answer == question["Answer"]:
            print("Correct!")
        else:
            print(f"The correct answer is {question['Answer']}")
            
        user_answer = ""
        while user_answer != "c" and user_answer != "q":
            user_answer = input("Press [c] to continue the session or [q] to quit")
        
        if user_answer == "q":
            continue_session = False
            
        
# Use a conditional to respond to what the user has chosen by executing one of the functions defined above
current_task = ""
while current_task != "q":
    print("Press [a] to add a new question, [s] to start a new study session, or [q] to quit.")
    current_task = input("What would you like to do?")
    if current_task == "a":
        add_question()
    elif current_task == "s":
        initiate_study_session()