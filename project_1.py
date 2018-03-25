score=0
def start():
    print("Welcome to Genious Puzzle Game")
    print("Choose the area you want")
    print("1.Physics")
    print("2.English")
    print("3.Mathematics")
    sub_choice()

def sub_choice():
    next=int(input("> "))
    if next==1:
       physics()
    elif next==2:
         English()
    elif next==3:
         maths()
    else:
         print("Invalid input")
def physics():
    print("Welcome to physics board and let's start the game")
    print("Game instructions are the following:I will show a formula picture and you will try to find the meaning of the formula")
    print("F=M*A is")
    print("1.Force")
    print("2.Length")
    print("3.Sun and earth distance formula")
    physics_question_1=int(input("> "))
    if physics_question_1==1:
       print("RIGHT")
       global score
       score+=10
    else:
        print("Wrong!")
#        global score
        score-=10

def English():
    print("Welcome to English board and let's start the questions")
    print("I ... lived in Seoul for four years")
    print("1.has")
    print("2.have")
    print("3.was")
    english_question_1=int(input("> "))
    if english_question_1==1:
       print("RIGHT")
       global score
       score+=10
    else:
        print("Wrong")
#        global score
        score-=10
def maths():
    print("Welcome to Mathematics board and let's start the questions")
    print("2+5= ")
    print("1. 9")
    print("2. 6")
    print("3. 7")
    maths_question_1=int(input("> "))
    if maths_question_1==3:
       print("RIGHT")
       global score
       score+=10
    else:
         print("WRONG")
#         global score
         score-=10

start()

