#opdrachten week 1
#1.2.1
def lijn():
    print("-" * 40)
line()
#1.2.2
def line():
    print("-" * 40)

def sides():
    txt = "|" + (" " * 38) + "|"
    print(txt)

line()
sides()
sides()
sides()
line()
#1.2.3
def sides():
    txt = "|" + (" " * 38) + "|"
    print(txt)
#1.2.4
line()
sides()
sides()
sides()
line()
#1.2.5
def box():
    line = "-" * 40
    sides =  "|" + " " * 38 + "|"
    print(line)
    print(sides)
    print(sides)
    print(sides)
    print(line)

box()
#1.2.6

#1.2.7

#1.2.8
"ja"
#1.2.9

#1.2.10

#1.2.11
#niggaballs
def line(lengte):
    print("-" * lengte)

line(15)
line(30)
#1.2.12
def line(lengte):
    print("-" * lengte)

def sides(width):
    text = "|" + (" " * width) + "|"
    print(text)

#line(15)
#line(30)
sides(15)
sides(30)
#1.2.13
"""
2:ja
0:ja
-2:ja
Hallo: error
"""
#1.2.14
for i in range(2):
    print(i)
    print("Hallo")
#1.2.15
def box(breedte, lengte):
    line = "-" * breedte
    sides =  "|" + " " * (breedte - 2) + "|"
    print(line)
    for i in range(lengte - 2):
        print(sides)
    print(line)
    
box(10,6)
#1.2.16

#1.2.17

#1.2.18
"""

"""
#1.2.19
def right_justify(s):
    print(" " * 70 + s)
    len(s)

right_justify('monty')
#1.2.20
def box(s2):
    w = int(len(s2))
    print('length of line is:', len(s2))
    out = "+--" + '-'* w + "--+"
    middle = '|  ' +  s2 + '  |' 
    print(out)
    print(middle)
    print(out)

box('Hallo Python')
#1.2.21

#1.2.22
graankorrels = 1
totaal = 0
for veld in range(1, 65):
    print('veld', veld, ':', graankorrels)
    totaal = totaal + graankorrels
    graankorrels = graankorrels * 2
print('totaal :', totaal)
