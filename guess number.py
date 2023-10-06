import random
import sys, subprocess

def human(x):
    rand=random.randint(1,x)
    n=0
    while n!=rand:
        
        n=int(input("enter guessed number: "))
        if n>rand:
            print(f"    {n} is too high")
        elif n<rand:
            print(f"    {n} is too low")
    print(f"you guessed the number.....! \n \
    the number is {n}")

    m=input("play again(Y) or end game(N): ").upper()
    if m=='Y':
        subprocess.run('clear', shell=True)
        human(100)
    elif m=='N':
        pass

def computer(x):
    c=0
    a=1
    rand=random.randint(a,x)
    n=""
    while n!="C":
        subprocess.run('clear', shell=True)
        print(f"Is it {rand}")
        n=input("if number is too low give (L) or the number is too high (H) or If the number correct (C): ").upper()
        if n=="L":
            a=rand+1
            rand=random.randint(a,x)
            
        elif n=="H":
            x=rand-1
            rand=random.randint(a,x)
            
        elif n=="C":
            print("computer won.......!")
        c+=1
    if c<3:
        print(f"the number is {rand}") 
    m=input("play again(Y) or end game(N): ").upper()
    if m=='Y':
        computer(100)
    elif m=='N':
        pass
    
def mode(n):
    if n=="H":
        human(100)
    elif n=="C":
        computer(100)
        
print("welcome to the guessing game")        
n=input("enter (H) for human or (C) for computer: ").upper()
mode(n)

    

    
