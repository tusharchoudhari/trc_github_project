import math
x,y=0,0

while True:
    step=input("Type step UP/DOWN/RIGHT/LEFT #no_of_steps:")
    if(step==""):
        break
    else :
        step=step.split(" ")
        if(step[0]=="UP") :
            y=y+int(step[1])
        elif (step[0] == "DOWN") :
            y = y - int(step[1])
        elif (step[0] == "RIGHT"):
            x = x + int(step[1])
        elif (step[0] == "LEFT"):
            x = x - int(step[1])
        else :
            print("Invalid direction to move")
            print("Please provide in below format:")
            print("UP 5\nDOWN 3\nLEFT 3\nRIGHT 2")
            continue
distance=math.sqrt(x**2+y**2)
print("The distance current position after sequence of movements:", distance)