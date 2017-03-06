from cube import Cube
from algorithm import Algorithm
import colorama

colorama.init()

c = Cube()

files = ["firstcross", "firstface", "middle", "lastcross", "lastface", "resolve"]
for s in files:
	a = Algorithm()
	a.loadFromFile(s + ".algo")
	c.addAlgo(s, a)

print("Welcome to Rubick's Cube player ! :)");
print("Type 'help' to get a list of usable command");
c.printCube();

inStr = ""
while inStr != "exit":
	s = c.eval(inStr)
	inStr = input(">> ")
	