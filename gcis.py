def rectangle_will_fit(x,y,length,height):
    if x+length<=400 and y+height <=400:
        return 1
    else:
        return 2
def main():
    xcor=int(input("enter a x cordinate: "))
    ycor=int(input("enter y cordinates: "))
    length=int(input("enter length: "))
    height=int(input("enter height"))
    print(rectangle_will_fit(xcor,ycor,length , height))
    if __name__=="main_":
        main()
        
import turtle
t=turtle
t.speed(10)
def draw_shape(shape,color_code,x,y,length,height=0):
    if shape=="r":
        if x+length <+400 and y+height <= 400:
            t.up()
            t.goto(x,y)
            t.fillcolor(color_code)
            t.begin_fill()
            t.down()
            for i in range(1,3):
                t.fd(length)
                t.lt(90)
                t.fd(height)
                t.lt(90)
            t.end_fill
            t.up()
            t.goto(0,400)
            return color_code
        else:
           return 0
    elif shape=="c":
        if height <=400:
            t.up()
            t.goto(x,y)
            t.lt(180)
            t.fillcolor(color_code)
            t.begin_fill()
            t.fd(height)
            t.down()
            t.circle(height)
            t.end_fill()
            t.up()
            t.goto(0,400)
            t.lt(90)
        else:
            return 0
    elif shape =="t":
        t.up()
        t.fillcolor(color_code)
        t.goto(x,y)
        t.begin_fill()
        t.down()
        if height <=400:
            i=0
            while i<3:
                t.fd(height)
                t.lt(120)
                i=i+1
        else:
            return 0 
        t.end_fill()
        t.penup()
        t.goto(150,60)
        t.pendown()
        t.fillcolor("green")
        t.begin_fill()
        for i in range(4):
            t.fd(100)
            t.lt(90)
        t.end_fill()

draw_shape("r","red",100,150,300,150)
draw_shape("c","yellow",-5,0,300,80)
draw_shape("t","blue",-100,300,300,100)

rectangle_will_fit()
main()
draw_shape()

