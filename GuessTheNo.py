#No. guessing game
#random module
import random

a = random.randint(1,100)

warm = abs(a+10) #abs() function to find the positive difference between two numbers

cold = abs(a-10)

print(warm)
print(a)
print(cold)

step = []

   
     


while True:
        guesss = int(input("ENTER YOUR GUESS NO. !!!\n\n\n"))
        step.append(guesss)
        if guesss > 100 or guesss < 1:
            print("\n***Out Of Bounds :-(***")
            continue
        else: 
            if (warm > guesss) and (guesss > a):
                print('\n***WARMING YOU ARE NEAR!!!+***')
                continue
            elif (cold < guesss) and (guesss < a):
                print('\n***COLD YOU ARE NEAR!!!!-***')
                continue
            elif guesss == a:
                print("\n***WIN***\n")
                b = str(len(step))
                print("\nyou take "+b + " steps!!!! TO complete Challenge..!" )
                break
            elif cold > guesss > 1:
                print("\n***FAR AWAY...cold-***")
                continue
            elif warm < guesss < 101:
                print("\n***FAR AWAY...WARM+***")
                continue
            
  