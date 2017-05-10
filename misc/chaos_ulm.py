# File: tdemo_chaos.py
# Author: Gregor Lingl
# Date: 2009-06-24
# 2015-10-12 M.Ulm - refactor to improve my understanding

# A demonstration of chaos

from turtle import *

MaxXToPlot = 80
MinYToShow = -0.1
MaxYToShow = 1.1
MinXToShow = -1
seedForChaosFunction = 0.35  # Original value 0.35

def f(x):
    return 3.9*x*(1-x)

def g(x):
    return 3.9*(x-x**2)

def h(x):
    return 3.9*x-3.9*x*x

def jumpto(x, y):
    penup(); goto(x,y)

def line(x1, y1, x2, y2):
    jumpto(x1, y1)
    pendown()
    goto(x2, y2)

def plotCoordinateSystem():
    line(MinXToShow, 0, MaxXToPlot+1, 0)
    line(0, MinYToShow, 0, MaxYToShow)

def plotChaosFunction(chaos_function, start, color):
    pencolor(color)
    y = start
    jumpto(0, y)
    pendown()
    dot(5)
    for i in range(MaxXToPlot):
        y=chaos_function(y)
        goto(i+1,y)
        dot(5)

def showWorldStartingFrom(x) : 
     setworldcoordinates(x,MinYToShow, MaxXToPlot+1,MaxYToShow)

def initChaosPlot() :
    reset()
    showWorldStartingFrom(MinXToShow)
    speed(0)
    hideturtle()
    plotCoordinateSystem()

def zoomWorldToStartFrom(startingX) :
    zoomStepsPerEachX = 2 # Orgingal value: 2
    for s in range(startingX * zoomStepsPerEachX) : 
        showWorldStartingFrom(s / zoomStepsPerEachX)       

def main():
    initChaosPlot()
    plotChaosFunction(f, seedForChaosFunction, "blue")
    plotChaosFunction(g, seedForChaosFunction, "green")
    plotChaosFunction(h, seedForChaosFunction, "red")
    zoomWorldToStartFrom(60)  # Original value: 50
    return "Done!"

if __name__ == "__main__":
    main()
    mainloop()

