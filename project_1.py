# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
#background_image = pygame.image.load("/Users/boburjonkobilov/Desktop/background.jpg")
## initialize game engine
#pygame.init()
#
#window_width=400
#window_height=400
#
#animation_increment=10
#clock_tick_rate=20
#
## Open a window
#size = (window_width, window_height)
#screen = pygame.display.set_mode(size)
#
## Set title to the window
#pygame.display.set_caption("Hello World")
#
#dead=False
#
#clock = pygame.time.Clock()
#background_image = pygame.image.load("/Users/boburjonkobilov/Desktop/images_1.jpg").convert()
#
#while(dead==False):
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            dead = True
#
#    screen.blit(background_image, [0, 0])
#
#    pygame.display.flip()
#    clock.tick(clock_tick_rate)
import getpass

physics_score=0
english_score=0
math_score=0

name_password={'Bob':2323
        }
class Subject(object):
    
    def user_info(self,name,password):
    
        self.name=name
        self.password=password
        
    def user_info_check(self,user_name,user_password):
        
        for name, password in name_password.items():
            if user_name==name and user_password==password:
               print("Login and Password verified")
               print("Welcome %s" %(name))
               break
            else:
               print("Wrong Login ID or Password")
               break
   
        
    
    
    def app_rules(self):
        print("-"*30)
        print("Weclome to the Brain Sharping Game")
        print("There are 3 areas to test your knowledge and get scores to pass next level")
        print("-"*30)
        print("1.Physics")
        print("2. English")
        print("3. Maths") 
        print("-"*30) 
       
    def subject_choice(self):
         choice=int(input("> "))
         
         if choice==1:
             self.physics()
             
         elif choice==2:
              self.English()
         
         elif choice==3:
             self.maths()
         else:
              print("Invalid input") 
            
    def physics(self):
        print("-"*30)
        print("Welcome to physics board and let's start the game")
        print("-"*30)
        self.physics_level_1()
        if physics_score>=30:
          self.physics_level_2() 
     
    def physics_level_1(self):
        print("-"*30)
        print("Welcome to level 1")
        print("-"*30)
        print("Game instructions are the following:")
        print("I will show a formula picture and you will try to find the meaning of the formula")
        print("-"*30)
        print("Question1: F=M*A is")
        print("1.Force")
        print("2.Length")
        print("3.Sun and earth distance formula")
        print("-"*30)
        physics_question_1=int(input("> "))
        if physics_question_1==1:
           print("RIGHT")
           global physics_score
           physics_score+=10
        else:
            print("Wrong!")
    #        global score
            physics_score-=10  
            
             
    def physics_level_2(self):
        print("-"*30)
        print("Welcome to level 2")
        print("-"*30)
        print("What is Newton's second law ")
        print("1. Inertia")
        print("2. Force")
        print("3. Movement")
        print("-"*30)
        physics_level_2_1=int(input("> "))
        if physics_level_2_1==1:
            print("-"*30)
            print("RIGHT")
            print("-"*30) 
            global physics_score
            physics_score+=10
        else:
              print("-"*30)
              print("WRONG")
              print("-"*30) 
              physics_score-=10


    
    def English(self):
        print("-"*30)
        print("Welcome to English board and let's start the questions")
        print("-"*30)
        self.english_level_1()
        if english_score>=30:
           self.english_level_2()
        
    def maths(self):
        print("-"*30)
        print("Welcome to Mathematics board and let's start the questions")
        print("-"*30)
        print("2+5= ")
        print("1. 9")
        print("2. 6")
        print("3. 7")
        maths_question_1=int(input("> "))
        if maths_question_1==3:
           print("-"*30) 
           print("RIGHT")
           print("-"*30) 
           global math_score
           math_score+=10
        else:
             print("-"*30)
             print("WRONG")
             print("-"*30)
    #         global score
             math_score-=10
             
    def english_level_1(self):
        print("-"*30)
        print("Welcome to Level 1")
        print("-"*30)
        print("I ... lived in Seoul for four years")
        print("1.has")
        print("2.have")
        print("3.was")
        print("-"*30)
        english_question_1=int(input("> "))
        if english_question_1==2:
           print("-"*30)  
           print("RIGHT")
           print("-"*30) 
           global english_score
           english_score+=10
        else:
            print("-"*30) 
            print("Wrong")
            print("-"*30) 
    #        global score
            english_score-=10
            
            
    def english_level_2(self):
        print("-"*30)
        print("Welcome to Level 2")
        print("-"*30)
        print("Bob went to ... hospital to see his ill dad ")
        print("1. a")
        print("2. some")
        print("3. the")
        print("-"*30) 
        english_question_2_1=int(input("> "))
        if english_question_2_1==3:
            print("-"*30) 
            print("RIGHT")
            print("-"*30) 
            global english_score
            english_score+=10
        else:
            print("-"*30) 
            print("WRONG")
            english_score-=10
    
    def math_level_2(self):
        print("-"*30) 
        print("Welcome to level 2")
        print("(2*4)/10= ")
        print("1. 0.8")
        print("2. 5.5")
        print("1.8")
        print("-"*30) 
        math_question_2_1=int(input("> "))
        if math_question_2_1==1:
            print("-"*30)  
            print("RIGHT")
            print("-"*30)  
            global math_score
            math_score+=10
        else:
             print("-"*30) 
             print("WRONG")
             print("-"*30) 
             math_score-=10 

    def score_showing(self):
      print("-"*30)
      print("Physics score: ",physics_score)
      print("English score: ",english_score)
      print("Maths score: ",math_score)
      print("-"*30) 
     
    def next_action(self):
        while True:
            print("To quit the game, press 'q' or 'Q' To continue press any keyboard>  ")
            print("-"*30)
            print("Feeling bored?? Do you want some jokes ?. If so, press 'J' or 'j")
            print("-"*30)
            print("If you have any questions, please press 'A' and leave your question there")
            
            print("-"*30)
            next_move=input("> ")
            if next_move=='q' or next_move=='Q':
                  print("Thank you for using our app")
                  print("See you soon again!")
                  break
            elif next_move=='A' or next_move=='a':
                  filename='questions.txt'
                  question=input("Leave it here please> ")
                  txt=open(filename,"a+")##based on the name of the file, we open file
                  txt.write(question)
                  txt.close()
                  print("Thank you again")
                  break
            elif next_move=='J' or next_move=='j':
                print("I ate a clock yesterday, it was very time consuming.")
                break
            
             
              
user=Subject()
user_name=input("Enter your login ID> ")
#print("Enter your password> ")
#user_password=int(input("Enter your password "))
user_password=int(getpass.getpass("Enter your password> "))                    #warning: getpass function doesnt fully work in spyder console but it works in terminal well
user.app_rules()
user.user_info_check(user_name,user_password)              
user.subject_choice()
user.score_showing()
user.next_action()
          
          
               
