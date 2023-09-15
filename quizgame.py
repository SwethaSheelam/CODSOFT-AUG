print("Wellcome to quiz game !!")
print('NOTE: if your spelling is incorrect then it is considered as wrong answer')
score = 0
question_no = 0
playing = input('Are you ready to play ? ').lower()
if playing == 'yes':
    question_no += 1
    ques = input(f'\n{question_no}. What is the extension of python files ').lower()
    if ques == '.py':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> .py ')

# ------1
    question_no += 1
    ques = input(f'\n{question_no}. Is string immutable in python ').lower()
    
    if ques == 'true':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> true')

# -----2
    question_no += 1
    ques = input(f'\n{question_no}. Which operator is used to multiply numbers? ').lower()
    
    if ques == '*':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> * ')

# -----3
    question_no += 1
    ques = input(f'\n{question_no}. Which collection does not allow duplicate members?').lower()
    
    if ques == 'set':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> set')


# -----4
    question_no += 1
    ques = input(f'\n{question_no}. Which statement is used to stop a loop? ').lower()
    
    if ques == 'break':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> break')


# ------5 

else:
    print('thankyou you are out of a game.')
    quit()

print(f'\nnumber of question is {question_no}')
print(f'your score is {score}')
try:
    percentage = (score *100)/question_no
except ZeroDivisionError:
    print('0% quetions are correct')

print(f'{percentage}% questions are correct.')