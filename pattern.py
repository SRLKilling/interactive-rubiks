class Pattern:

	def __init__(self, str=None):
		self.faces = [['_' for j in range(9)] for i in range(6)]
		if str != None: self.load(str)
		
	def load(self, str):
		lines = str.split('\n')
		for i in range(3):
			lines[i] = lines[i].strip().split()
			self.faces[4][i*3], self.faces[4][i*3+1], self.faces[4][i*3+2] = lines[i][0], lines[i][1], lines[i][2]
		for i in range(3):
			lines[3+i] = lines[3+i].strip().split()
			self.faces[0][i*3], self.faces[0][i*3+1], self.faces[0][i*3+2] = lines[3+i][0], lines[3+i][1], lines[3+i][2]
			self.faces[1][i*3], self.faces[1][i*3+1], self.faces[1][i*3+2] = lines[3+i][3], lines[3+i][4], lines[3+i][5]
			self.faces[2][i*3], self.faces[2][i*3+1], self.faces[2][i*3+2] = lines[3+i][6], lines[3+i][7], lines[3+i][8]
			self.faces[3][i*3], self.faces[3][i*3+1], self.faces[3][i*3+2] = lines[3+i][9], lines[3+i][10], lines[3+i][11]
		for i in range(3):
			lines[6+i] = lines[6+i].strip().split()
			self.faces[5][i*3], self.faces[5][i*3+1], self.faces[5][i*3+2] = lines[6+i][0], lines[6+i][1], lines[6+i][2]
	
	def match(self, cube):
		for z in range(4):
			colors, matched = [], True
			for f in range(6):
				if matched:
					for i in range(9):
						if self.matchCase(cube, colors, f, i) == False:
							cube.z()
							matched = False
							break
			if matched:
				cube.z(3*z)
				return z
		
		return -1

	def matchOnly(self, cube, c):
		for z in range(4):
			color, matched = -1, True
			for f in range(6):
				if matched:
					for i in range(9):
						if color == -1 and self.faces[f][i] == c:
							color = cube.faces[f][i]
						elif color != -1 and self.faces[f][i] == c and cube.faces[f][i] != color:
							cube.z()
							matched = False
							break
			if matched:
				cube.z(3*z)
				return z
		return -1
		
	def matchCase(self, cube, colors, f, i):
		if(self.faces[f][i] == '_'):
			return True
		else:
			char, color = int(self.faces[f][i]), -1
			# print(colors, char)
			for c in colors:
				if c[0] == char:
					color = c[1]
					break
				elif c[1] == cube.faces[f][i]:
					return False
			if color == -1:
				colors.append( (char, cube.faces[f][i]) )
				return True
			else:
				return color == cube.faces[f][i]
			