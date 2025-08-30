str = "MyFirstPythonString"

print(str[::-1])

hour = 3
minute = "19"
ary = "current time is %d : %s" % (hour, minute)

print(ary)

ary2 = "{new} skill {name} ".format(name="lovewinsall",new ="OMG")

print(ary2)

ary3 = [1,4,3,2,5,77,45,2,3]
ary3.sort()
ary3.reverse()
ary3.append(100)
ary3.insert(0,1000)
print(ary3)