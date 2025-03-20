import turtle

draw = turtle.Turtle()

draw.speed(1000)
draw.penup()
draw.goto(-200,100)
draw.pendown()
draw.pensize(5)
draw.shapesize(0.1)
draw.fd(300)
draw.penup()
draw.right(90)
draw.fd(100)
draw.right(90)
draw.pendown()
draw.fd(300)
draw.bk(100)
draw.right(90)
draw.fd(200)
draw.bk(300)
draw.penup()
draw.right(90)
draw.fd(100)
draw.left(90)
draw.pendown()
draw.fd(300)

win = 0
game = 1
turn = 1

def circle():
    draw.pd()
    draw.setheading(0)
    draw.circle(30)
    draw.pu()

def cross():
    draw.penup()
    draw.setheading(90)
    draw.right(45)
    draw.fd(25.5)
    draw.pendown()
    draw.fd(90)
    draw.penup()
    draw.fd(25.5)
    draw.pendown()
    draw.right(135)
    draw.pu()
    draw.fd(100)
    draw.pd()
    draw.right(135)
    draw.penup()
    draw.fd(25.5)
    draw.pendown()
    draw.fd(90)
    draw.penup()
    draw.fd(25.5)
    draw.penup()



field1 = 0
field2 = 1
field3 = 9
field4 = 3
field5 = 4
field6 = 5
field7 = 6
field8 = 7
field9 = 8

print("input works by entering the number 1 - 9 beginning from the top left")

while game == 1:
    if field1 == field2 == field3:
        if field1 == 2:
            print("player X won!")
        elif field1 == -2:
            print("player O won!")
        else:
            print("something went wrong")
    elif field1 == field5 == field9:
        if field1 == 2:
            print("player X won!")
        elif field1 == -2:
            print("player O won!")
        else:
            print("something went wrong")
    elif field1 == field4 == field7:
        if field1 == 2:
            print("player X won!")
        elif field1 == -2:
            print("player O won!")
        else:
            print("something went wrong")
    elif field2 == field5 == field8:
        if field2 == 2:
            print("player X won!")
        elif field2 == -2:
            print("player O won!")
        else:
            print("something went wrong")
    elif field4 == field5 == field6:
        if field4 == 2:
            print("player X won!")
        elif field4 == -2:
            print("player O won!")
        else:
            print("something went wrong")
    elif field7 == field5 == field3:
        if field7 == 2:
            print("player X won!")
        elif field7 == -2:
            print("player O won!")
        else:
            print("something went wrong")
    elif field7 == field8 == field9:
        if field7 == 2:
            print("player X won!")
        elif field7 == -2:
            print("player O won!")
        else:
            print("something went wrong")
    elif field3 == field6 == field9:
        if field3 == 2:
            print("player X won!")
        elif field3 == -2:
            print("player O won!")
        else:
            print("something went wrong")

    elif (field1 + field2 + field3 + field4 + field5 + field6 + field7 + field8 + field9) == 2:
        print("its a tie!!!!")
    elif turn == 1:
        move1 = input("Player X, enter where you want to go: ")
        if move1 == "1":
            if field1 == 0:
                draw.penup()
                draw.goto(-200,100)
                cross()
                turn += 1
                field1 += 2

            else:
                print("this field is already full")

        elif move1 == "2":
            if field2 == 1:
                draw.penup()
                draw.goto(-100,100)
                cross()
                turn += 1
                field2 += 1
            
            else: print("This field is already full")

        elif move1 == "3":
            if field3 == 9:
                draw.penup()
                draw.goto(0,100)
                cross()
                turn += 1
                field3 -= 7

            else:
                print("This field is already full")

        elif move1 == "4":
            if field4 == 3:
                draw.penup()
                draw.goto(-200,0)
                cross()
                turn += 1
                field4 -= 1

            else:
                print("this field is already full")

        elif move1 == "5":
            if field5 == 4:
                draw.penup()
                draw.goto(-100,0)
                cross()
                turn += 1
                field5 -= 2

            else:
                print("this field is already full")

        elif move1 == "6":
            if field6 == 5:
                draw.penup()
                draw.goto(0,0)
                cross()
                turn += 1
                field6 -= 3

            else:
                print("this field is already full")

        elif move1 == "7":
            if field7 == 6:
                draw.penup()
                draw.goto(-200,-100)
                cross()
                turn += 1
                field7 -= 4

            else:
                print("this field is already full")

        elif move1 == "8":
            if field8 == 7:
                draw.penup()
                draw.goto(-100,-100)
                cross()
                turn += 1
                field8 -= 5

            else:
                print("this field is already full")

        elif move1 == "9":
            if field9 == 8:
                draw.penup()
                draw.goto(0,-100)
                cross()
                turn += 1
                field9 -= 6

            else:
                print("this field is already full")

        else:
            print("Not a valid input")

    elif turn == 2:
        move2 = input("Player O, enter where you want to go: ")
        if move2 == "1":
            if field1 == 0:
                draw.goto(-150,120)
                circle()
                turn -= 1
                field1 -= 2

            else:
                print("this field is already full")

        elif move2 == "2":
            if field2 == 1:
                draw.goto(-50,120)
                circle()
                turn -= 1
                field2 -= 3
            
            else: print("This field is already full")

        elif move2 == "3":
            if field3 == 9:
                draw.goto(50,120)
                circle()
                turn -= 1
                field3 -= 11

            else:
                print("This field is already full")

        elif move2 == "4":
            if field4 == 3:
                draw.goto(-150,20)
                circle()
                turn -= 1
                field4 -= 5

            else:
                print("This field is already full")
                
        elif move2 == "5":
            if field5 == 4:
                draw.goto(-50,20)
                circle()
                turn -= 1
                field5 -= 6

            else:
                print("This field is already full")

        elif move2 == "6":
            if field6 == 5:
                draw.goto(50,20)
                circle()
                turn -= 1
                field6 -= 7

            else:
                print("This field is already full")

        elif move2 == "7":
            if field7 == 6:
                draw.goto(-150,-80)
                circle()
                turn -= 1
                field7 -= 8

            else:
                print("This field is already full")

        elif move2 == "8":
            if field8 == 7:
                draw.goto(-50,-80)
                circle()
                turn -= 1
                field8 -= 9

            else:
                print("This field is already full")

        elif move2 == "9":
            if field9 == 8:
                draw.goto(50,-120)
                circle()
                turn -= 1
                field9 -= 10

            else:
                print("This field is already full")

        else:
            print("invalid input")

    elif turn == 0:
        break

    else:
        print("something went wrong")

turtle.pu()
turtle.circle(999999999999)