from turtle import Screen,Turtle
class Ractangle():
    def __init__(self):
        self.x = 0
        self.y = 0
    def area(self):
        tot_area = self.x * self.y
        return tot_area
    def scop(self):
        tot_scop = self.x*2 + self.y*2
        return tot_scop
    def inp(self):
        self.x = int(input("please enter with: "))
        self.y = int(input("please enter height: "))
    def out(self):
        print(self.x)
        print(self.y)
        print(self.scop())
        print(self.area())
        for i in range(0, self.y):
            print(self.x*"*")
r1 = Ractangle()
r1.inp()
r1.out()
# print(r1.out())
#r1 = Ractangle(width=5,height=10)
#print(r1)
'''
#name = "abcdefg"
#print(name[-1::-2][2:])
print("pi is {0:.2}".format(22 / 7))
print("pi is {0:12f}".format(22 / 7))
print("pi is {0:12.50}".format(22 / 7))
print("pi is {0:52.50f}".format(22 / 7))
print("pi is {0:62.50f}".format(22 / 7))
print("pi is {0:<72.50f}".format(22 / 7))

#res = ["rge",5,6.35,1]
#res.sort()
#print(res)
d = {1: ['a', 'b', 'c', 'd'], 2: 'rara'}
print(d.items())
print(d)


'''
# def f(x,y):        x,y פרמטרים
#     x = x            x השמאלי הינו משתנה של הימני
#     y = y
#
# f(10,20)         10,20 הם ארגומנטים
# def x(z)
#     ...
#
# x(list)         list הינו ארגומנט של המתודה  איקס
