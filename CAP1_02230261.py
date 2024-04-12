################################
# Name: Cheten Dorji 
# Department: B.E Mechanical Engineering
# Student ID Number: 02230261
################################
# REFERENCES
# https://www.w3schools.com/python/python_dictionaries.asp#:~:text=Dictionaries%20are%20used%20to%20store,and%20earlier%2C%20dictionaries%20are%20unordered.
# http://link.to.an.article/video.com
################################
# SOLUTION
# Solution Score:50055
# Put your number here : 1
################################
def read_input():
    return open("input_1_cap1.txt", "r")# it reads the input file 

def calculate_scores(s):
    
    A = 1#Rock
    B = 2#Paper
    C = 3#Sissor
    X = 0#Lose = 0
    Y = 3#Draw = 3
    Z = 6#Win = 6
    lose1 = C + X   #Adding the score
    lose2 = A + X
    lose3 = B + X
    draw1 = A + Y
    draw2 = B + Y
    draw3 = C + Y
    win1 = B + Z
    win2 = C + Z 
    win3 = A + Z

    #Created a new dict
    score_dict = {
        "A X":lose1,
        "B X":lose2,
        "C X":lose3, 
        "A Y":draw1, 
        "B Y":draw2, 
        "C Y":draw3, 
        "A Z":win1, 
        "B Z":win2, 
        "C Z":win3 
        
    } 
    total_score = 0
    for result in s:
        score = result.strip()#reads the input file line by line 
        score_from_dict = score_dict.get(score, None)#It will add  the score and if not found it will print None 
        if score_from_dict is not None:
            total_score += score_from_dict
        else:
            print(None)
        
    print(f" The total score is {total_score}")

calculate_scores(read_input())