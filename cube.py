import colorama
from algorithm import Algorithm

colorama.init()

class Cube:
	def __init__(self):
		self.reset()
		self.algo = {}
		self.options = {}
		self.options["verbose"] = 2
		self.options["interactive"] = True
		self.options["rotateMode"] = True
		self.options["coloredOutput"] = True
		
	def reset(self):
		self.faces = [[i for j in range(9)] for i in range(6)]
		
	def pause(self):
		if self.options["interactive"]:
			input('')
			
	def pr(self, str):
		if self.options["verbose"]:
			print(str)
	
	# Primary moves
	
	def rotateLeft(self, n=1):
		for i in range(n):
			self.faces[0], self.faces[1], self.faces[2], self.faces[3] = self.faces[3], self.faces[0], self.faces[1], self.faces[2]
			f = self.faces[4]; f[0], f[1], f[2], f[3], f[5], f[6], f[7], f[8] = f[2], f[5], f[8], f[1], f[7], f[0], f[3], f[6]
			f = self.faces[5]; f[0], f[1], f[2], f[3], f[5], f[6], f[7], f[8] = f[6], f[3], f[0], f[7], f[1], f[8], f[5], f[2]		
	def rotateDown(self, n=1):
		for i in range(n):
			f1, f2 = self.faces[5][::], self.faces[3][::]
			self.faces[1], self.faces[5] = self.faces[4][::], self.faces[1][::]
			f = self.faces[3]; f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8] = f1[8], f1[7], f1[6], f1[5], f1[4], f1[3], f1[2], f1[1], f1[0]
			f = self.faces[4]; f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8] = f2[8], f2[7], f2[6], f2[5], f2[4], f2[3], f2[2], f2[1], f2[0]
			f = self.faces[2]; f[0], f[1], f[2], f[3], f[5], f[6], f[7], f[8] = f[2], f[5], f[8], f[1], f[7], f[0], f[3], f[6]
			f = self.faces[0]; f[0], f[1], f[2], f[3], f[5], f[6], f[7], f[8] = f[6], f[3], f[0], f[7], f[1], f[8], f[5], f[2]		
	def turnFace(self, n=1):
		for i in range(n):
			f = self.faces[1]; f[0], f[1], f[2], f[3], f[5], f[6], f[7], f[8] = f[6], f[3], f[0], f[7], f[1], f[8], f[5], f[2]
			f1, f2, f3, f4 = self.faces[0], self.faces[4], self.faces[2], self.faces[5]
			f1[8], f1[5], f1[2], f2[6], f2[7], f2[8], f3[0], f3[3], f3[6], f4[2], f4[1], f4[0] = f4[2], f4[1], f4[0], f1[8], f1[5], f1[2], f2[6], f2[7], f2[8], f3[0], f3[3], f3[6]
		
		
	# Simple moves
		
	def F(self, n=1):
		self.turnFace(n)
		return self
	def F2(self):
		self.turnFace(2)
		return self
	def F_(self):
		self.turnFace(3)
		return self
		
	def B(self, n=1):
		self.rotateLeft(2)
		self.turnFace(n)
		self.rotateLeft(2)
		return self
	def B2(self):
		return self.B(2)
	def B_(self):
		return self.B(3)
		
	def U(self, n=1):
		self.rotateDown()
		self.turnFace(n)
		self.rotateDown(3)
		return self
	def U2(self):
		self.U(2)
		return self
	def U_(self):
		self.U(3)
		return self
		
	def D(self, n=1):
		self.rotateDown(3)
		self.turnFace(n)
		self.rotateDown()
		return self
	def D2(self):
		self.D(2)
		return self
	def D_(self):
		self.D(3)
		return self
		
	def R(self, n=1):
		self.rotateLeft(3)
		self.turnFace(n)
		self.rotateLeft()
		return self
	def R2(self):
		self.R(2)
		return self
	def R_(self):
		self.R(3)
		return self
		
	def L(self, n=1):
		self.rotateLeft()
		self.turnFace(n)
		self.rotateLeft(3)
		return self
	def L2(self):
		self.L(2)
		return self
	def L_(self):
		self.L(3)
		return self
		
	## Double moves
		
	def f(self, n=1):
		self.B(n)
		self.z(n)
		return self
	def f2(self):
		return self.f(2)
	def f_(self):
		return self.f(3)
	
	def b(self, n=1):
		self.F(n)
		self.z(3*n)
		return self
	def b2(self):
		return this.b(2)
	def b_(self):
		return this.b(3)
	
	def u(self, n=1):
		self.D(n)
		self.y(n)
		return self
	def u2(self):
		return self.u(2)
	def u_(self):
		return self.u(3)
		
	def d(self, n=1):
		self.U(n)
		self.y(3*n)
		return self
	def d2(self):
		return self.d(2)
	def d_(self):
		return self.d(3)
	
	def r(self, n=1):
		self.L(n)
		self.x(n)
		return self
	def r2(self):
		return self.r(2)
	def r_(self):
		return self.r(3)
		
	def l(self, n=1):
		self.R(n)
		self.x(3*n)
		return self
	def l2(self):
		return self.l(2)
	def l_(self):
		return self.l(3)
	
	## Middle moves
	
	def M(self, n=1):
		self.R(n)
		self.L(3*n)
		self.x(3*n)
	def m(self, n=1):
		self.L(n)
		self.R(3*n)
		
	def E(self, n=1):
		self.U(n)
		self.D(3*n)
		self.y(3*n)
	def e(self, n=1):
		self.U(3*n)
		self.D(n)
	
	def S(self, n=1):
		self.F(3*n)
		self.B(n)
		self.z(n)
	def s(self, n=1):
		self.F(n)
		self.B(3*n)
	
	## Cube rotations
	
	def x(self, n=1):
		self.rotateDown(3*n)
		return self
	def x2(self):
		return self.x(2)
	def x_(self):
		return self.x(3)

	def y(self, n=1):
		self.rotateLeft(3*n)
		return self
	def y2(self):
		return self.y(2)
	def y_(self):
		return self.y(3)
		
	def z(self, n=1):
		self.rotateLeft(3)
		self.rotateDown(n)
		self.rotateLeft()
		return self
	def z2(self):
		return self.z(2)
	def z_(self):
		return self.z(3)
		
	
	## Eval and algorithms
		
	def eval(self, str):
		algo = Algorithm()
		changer = algo.parseLine(str)
		algo.do(self)
		if changer: self.printCube()
			
	def do(self, str, m=0, silent=False):
		self.z(m)
		i = 0
		s = ""
		suffix = ['', "2", "'"]
		while i < len(str):
			n, c = 1, str[i]
			if i+1 < len(str) and str[i+1] == "'":
				n = 3
				i += 2
			elif i+1 < len(str) and str[i+1] == '2':
				n = 2
				i += 2
			elif i+1 < len(str) and c == '2':
				n = 2
				c = str[i+1]
				i += 2
			else:
				i += 1
			
			if(c == 'F'): self.F(n)
			elif(c == 'B'): self.B(n)
			elif(c == 'U'): self.U(n)
			elif(c == 'D'): self.D(n)
			elif(c == 'R'): self.R(n)
			elif(c == 'L'): self.L(n)
			
			elif(c == 'f'): self.f(n)
			elif(c == 'b'): self.b(n)
			elif(c == 'u'): self.u(n)
			elif(c == 'd'): self.d(n)
			elif(c == 'r'): self.r(n)
			elif(c == 'l'): self.l(n)
			
			elif(c == 'M'): self.M(n)
			elif(c == 'm'): self.m(n)
			elif(c == 'E'): self.E(n)
			elif(c == 'e'): self.e(n)
			elif(c == 'S'): self.S(n)
			elif(c == 's'): self.s(n)
			
			elif(c == 'x'): self.x(n)
			elif(c == 'y'): self.y(n)
			elif(c == 'z'): self.z(n)
			
			else: continue
			
			s += self.zDecal(c, m, n) + " "
			
		self.z(3*m)
		
		if self.options["verbose"] > 1 and silent == False:
			if self.options["rotateMode"]: print(s)
			else:
				if m%4 == 0: print(s)
				if m%4 == 1: print('z -', s, "- z'")
				elif m%4 == 2: print('z2 -', s, '- z2')
				elif m%4 == 3: print("z' -", s, '- z')
	
	def addAlgo(self, name, algo):
		self.algo[name] = algo
        
	def doAlgo(self, str):
		if str in self.algo:
			return self.algo[str].do(self)
		else: return "Error: '" + str + "' has not been declared"
	
	def imp(self, file):
		a = Algorithm()
		a.loadFromFile(file + ".algo")
		self.addAlgo(file, a)
		
	def setOption(self, name, value):
		if name not in self.options:
			print("Error: '", name, "' is not an option", sep='')
		else:
			if type(self.options[name]) == int:
				self.options[name] = int(value)
			elif type(self.options[name]) == float:
				self.options[name] = float(value)
			elif type(self.options[name]) == bool:
				self.options[name] = (value.lower() in ["true", "yes", "y", "t", "1"])
			else:
				self.options[name] = value
		
	
	## Printing
	
	def zDecal(self, c, i, n):
		suffix = ['', "2", "'"]
		if self.options["rotateMode"]: 
			moves = [['U', 'L', 'D', 'R'], ['u', 'l', 'd', 'r']]
			for move in moves:
				if c in move:
					return move[(move.index(c) + i) % len(move)] + suffix[n-1]
			
			moves = [['M', 'E'], ['m', 'e']]
			for move in moves:
				if c in move:
					if i%4 == 0: return c + suffix[n-1]
					elif i%4 == 1: return move[(move.index(c) + i) % len(move)] + suffix[n-1]
					elif i%4 == 2: return c + suffix[-1*(n-2)+1]
					elif i%4 == 3: return move[(move.index(c) + i) % len(move)] + suffix[-1*(n-2)+1]
					
		return c + suffix[n-1]
		
	def __str__(self):
		s = ''
		f = self.faces
		
		s += "        |-------|\n"
		for i in range(3):
			s += "        | " + str(f[4][3*i]) + ' ' + str(f[4][3*i+1]) + ' ' + str(f[4][3*i+2]) + ' |\n'
		s += "|-------|-------|-------|-------|\n"
		for i in range(3):
			s += '| ' + str(f[0][3*i]) + ' ' + str(f[0][3*i+1]) + ' ' + str(f[0][3*i+2]) + ' | ' + str(f[1][3*i]) + ' ' + str(f[1][3*i+1]) + ' ' + str(f[1][3*i+2]) + ' | ' + str(f[2][3*i]) + ' ' + str(f[2][3*i+1]) + ' ' + str(f[2][3*i+2]) + ' | ' + str(f[3][3*i]) + ' ' + str(f[3][3*i+1]) + ' ' + str(f[3][3*i+2]) + ' |\n'
		s += "|-------|-------|-------|-------|\n"
		for i in range(3):
			s += "        | " + str(f[5][3*i]) + ' ' + str(f[5][3*i+1]) + ' ' + str(f[5][3*i+2]) + ' |\n'
		s += "        |-------|\n"
		return s
	def printCube(self):
		if not self.options["verbose"] > 0:
			return
	
		if not self.options["coloredOutput"]:
			print(self)
			return
			
		print('')
		f = self.faces
		
		for i in range(3):
			print("      ", end='')
			self.printCase(4, 3*i)
			self.printCase(4, 3*i+1)
			self.printCase(4, 3*i+2)
			print('')
			
		for i in range(3):
			self.printCase(0, 3*i)
			self.printCase(0, 3*i+1)
			self.printCase(0, 3*i+2)
			self.printCase(1, 3*i)
			self.printCase(1, 3*i+1)
			self.printCase(1, 3*i+2)
			self.printCase(2, 3*i)
			self.printCase(2, 3*i+1)
			self.printCase(2, 3*i+2)
			self.printCase(3, 3*i)
			self.printCase(3, 3*i+1)
			self.printCase(3, 3*i+2)
			print('')
			
		for i in range(3):
			print("      ", end='')
			self.printCase(5, 3*i)
			self.printCase(5, 3*i+1)
			self.printCase(5, 3*i+2)
			print('')
		print('')
        
	def printCase(self, f, i):
		if self.faces[f][i] == 0: print(colorama.Back.GREEN, "  ", colorama.Back.RESET, sep='', end='')
		if self.faces[f][i] == 1: print(colorama.Back.WHITE, "  ", colorama.Back.RESET, sep='', end='')
		if self.faces[f][i] == 2: print(colorama.Back.BLUE, "  ", colorama.Back.RESET, sep='', end='')
		if self.faces[f][i] == 3: print(colorama.Back.YELLOW, "  ", colorama.Back.RESET, sep='', end='')
		if self.faces[f][i] == 4: print(colorama.Back.MAGENTA, "  ", colorama.Back.RESET, sep='', end='')
		if self.faces[f][i] == 5: print(colorama.Back.RED, "  ", colorama.Back.RESET, sep='', end='')
			
			
c = Cube()

files = ["firstcross", "firstface", "middle", "lastcross", "lastface", "resolve"]
for s in files:
	a = Algorithm()
	a.loadFromFile(s + ".algo")
	c.addAlgo(s, a)
	
# print(c.zDecal("U", 2, 1))
# print(c.zDecal("M", 0, 1))
# print(c.zDecal("M", 1, 1))
# print(c.zDecal("M", 2, 1))
# print(c.zDecal("M", 3, 1))
# print(c.zDecal("M", 0, 3))
# print(c.zDecal("M", 1, 3))
# print(c.zDecal("M", 2, 3))
# print(c.zDecal("M", 3, 3))

print("Welcome to Rubick's Cube player ! :)");
print("Type 'help' to get a list of usable command");
c.printCube();

inStr = ""
while inStr != "exit":
	s = c.eval(inStr)
	inStr = input(">> ")
	