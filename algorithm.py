from pattern import Pattern
from random import randint

class AlgoAction:
	def __init__(self, code, silent=False):
		self.code = code
		self.silent = silent
		
	def do(self, cube, m):
		cube.do(self.code, m, self.silent)
		return False
		
class AlgoPrint:
	def __init__(self, str):
		self.str = str
		
	def do(self, cube):
		cube.pr(self.str)
		return False
		
class AlgoImport:
	def __init__(self, file):
		self.file = file
		
	def do(self, cube):
		cube.imp(self.file)
		return False
		
class AlgoDoAlgo:
	def __init__(self, str):
		self.str = str
		
	def do(self, cube):
		return cube.doAlgo(self.str)
		
class AlgoPrintCube:		
	def do(self, cube):
		cube.printCube()
		return False

class AlgoPause:
	def do(self, cube):
		cube.pause()
		return False
	
class AlgoReset:
	def do(self, cube):
		cube.reset()
		return False
		
class AlgoSetOption:
	def __init__(self, optname, optval):
		self.name = optname
		self.val = optval
		
	def do(self, cube):
		cube.setOption(self.name, self.val)
		return False
	
class AlgoRandomize:
	def __init__(self, silent=False):
		self.silent = silent
		
	def do(self, cube):
		s = ""
		for j in range(20):
			r = randint(0, 18)
			t, n = r//3, r%3
			if(t == 0):
				s += "F"
			if(t == 1):
				s += "B"
			if(t == 2):
				s += "U"
			if(t == 3):
				s += "D"
			if(t == 4):
				s += "R"
			if(t == 5):
				s += "L"
			
			if(n == 1): s+="2"
			elif(n == 2): s+="_"
			s += " "
			
		cube.do(s, 0, self.silent)
		return False
	
	

class Algorithm:
	
	IF = 0
	WHILE = 1
	UNTIL = 2

	def __init__(self, patterns=[Pattern()], parent=None, conditionType=IF):
		self.step = []
		self.patterns = patterns
		self.conditionType = conditionType
		self.parent = parent
		self.elseAlgo = None
		
	def newAlgo(self, patterns, cond):
		step = Algorithm(patterns, self, cond)
		self.step.append(step)
		return step
		
	def newDoAlgo(self, str):
		self.step.append( AlgoDoAlgo(str) )
		
	def newMatchdoing(self, pattern, c, action):
		step = AlgoMatch(self, [pattern], c, action)
		self.step.append(step)
		return step
		
	def newElseMatchdoing(self, pattern, c, action):
		self.elseAlgo = AlgoMatch(self.parent, [pattern], c, action)
		return self.elseAlgo
		
	def newElse(self, patterns):
		self.elseAlgo = Algorithm(patterns, self.parent, Algorithm.IF)
		return self.elseAlgo
		
	def newAction(self, str, silent=False):
		self.step.append( AlgoAction(str, silent) )
		
	def newPrint(self, str):
		self.step.append( AlgoPrint(str) )
		
	def newPrintCube(self):
		self.step.append( AlgoPrintCube() )
		
	def newPause(self):
		self.step.append( AlgoPause() )
		
	def newRandomize(self, silent=False):
		self.step.append( AlgoRandomize(silent) )
		
	def newReset(self):
		self.step.append( AlgoReset() )
		
	def newImport(self, str):
		self.step.append( AlgoImport(str) )
		
	def newSetOption(self, optname, optval):
		self.step.append( AlgoSetOption(optname, optval) )
		
		
	def loadFromFile(self, filepath):
		file = None
		try:
			file = open(filepath, "r")
		except IOError:
			print("Error: '", filepath, "' no such file", sep='')
			return
		
		line = file.readline()
		lineno = 1
		step = self
		while line != '':
			line = line.strip(' \t\n\r')
			
			
			if line.startswith("match "):
				param = line[6:].split("doing")
				param[0] = param[0].strip(); param[1] = param[1].strip()
				str = ''
				for i in range(9): str += file.readline()
				lineno += 9
				step = step.newMatchdoing(Pattern(str), param[0], param[1])
				
			elif line.startswith("elseif-match "):
				if self.conditionType != Algorithm.IF:
					print("Error in ",filepath,":", lineno,": 'elseif-match' must follow an 'if', 'elseif', 'match', or 'elseif-match' clause", sep='')
					return
				param = line[13:].split("doing")
				param[0] = param[0].strip(); param[1] = param[1].strip()
				str = ''
				for i in range(9): str += file.readline()
				lineno += 9
				step = step.newElseMatchdoing(Pattern(str), param[0], param[1])
				
			elif line.startswith("if"):
				l = self.parsePatterns(file)
				lineno += l[0]
				step = step.newAlgo(l[1], Algorithm.IF)
				
			elif line == "elseif":
				if self.conditionType != Algorithm.IF:
					print("Error in ",filepath,":", lineno,": 'elseif' must follow an 'if', 'elseif', 'match', or 'elseif-match' clause", sep='')
					return
				l = self.parsePatterns(file)
				lineno += l[0]
				step = step.newElse(l[1])
				
			elif line == "else":
				if self.conditionType != Algorithm.IF:
					print("Error in ",filepath,":", lineno,": 'else' must follow an 'if', 'elseif', 'match', or 'elseif-match' clause", sep='')
					return
				step = step.newElse([Pattern()])
				
			elif line.startswith("while"):
				l = self.parsePatterns(file)
				lineno += l[0]
				step = step.newAlgo(l[1], Algorithm.WHILE)
				
			elif line.startswith("until"):
				l = self.parsePatterns(file)
				lineno += l[0]
				step = step.newAlgo(l[1], Algorithm.UNTIL)
				
			elif line == "end":
				if step.parent == None:
					print("Error in ",filepath,":", lineno,": Too much 'end'", sep='')
					return
				step = step.parent
				
			else:
				self.parseLine(line, step, filepath, lineno)
				
			line = file.readline()
			lineno += 1
			
	def parseLine(self, line, step=None, filename='<input>', lineno=1):
		if(step == None): step = self
		line = line.strip()
		
		if line.lower() == "help":
			print("Here is a list of command :")
			print(" - 'randomize' to get a random rubick's cube (if you don't want to print the random moves, use 'randomize silent')")
			print(" - 'do' succeeded by a move sequence (moves are L, R, U, D, B, F, l, r, u, d, b, f, M, E, S, m, e, s, x, y, z)")
			print(" - 'doalgo <name>' will do the algorithm named <name>, previously loaded with import")
			print("    Startup loaded algo: firstcross, firstface, middle, lastcross, lastface, resolve")
			print(" - 'import <path>' so that <path>.algo will by imported into the algorithm list")
			print(" - 'reset' to start with a new fresh cube")
			print(" - 'set <name> = <value>' to set one of the options")
			print("    current options are : 'interactive' to enable ('true') or disable ('false') pause during algorithm execution")
			print("                          'coloredOutput' to enable a colored output ('true') vs a numbered output ('false')")
			print("                          'verbose' to enable all output ('2'), only cube printing ('1'), or no output at all ('0')")
			print(" - 'exit' to quit this command prompt")
			print("")
			print("Basically, if you want to have fun with this software, juste use :")
			print(" >> randomize")
			print(" >> doalgo resolve")
			print("")
			
			
		elif line.startswith("do "):
			if(line[3:].strip().startswith("silent ")): step.newAction(line[3:].strip()[6:], True)
			else: step.newAction(line[3:].strip())
			return True
			
		elif line.startswith("doalgo "):
			step.newDoAlgo(line[7:].strip())
			return False
			
		elif line.startswith("print "):
			step.newPrint(line[6:].strip())
			return False
			
		elif line.lower() == "printcube":
			step.newPrintCube()
			return False
			
		elif line.lower() == "reset":
			step.newReset()
			return True
			
		elif line.lower().startswith("import "):
			step.newImport(line[7:].strip())
			return False
			
		elif line.lower() == "pause":
			step.newPause()
			return False
			
		elif line.lower().startswith("randomize"):
			if(line[10:].strip().startswith("silent")): step.newRandomize(True)
			else: step.newRandomize()
			return True
			
		elif line.lower().startswith("set"):
			opt = line[3:].split("=")
			step.newSetOption(opt[0].strip(), opt[1].strip())
				
		elif line != '' and line.startswith('#') == False:
			print("Error in ",filename,":", lineno,": Unrecognized syntax", sep='')
			# print(line)
			return False
			
	def parsePatterns(self, file):
		lineno, pat, cont = 0, [], True
		while cont:
			str = ''
			for i in range(9): str += file.readline()
			lineno += 9
			pat.append(Pattern(str))
			s = file.readline()
			if(s.strip().lower() != "or"):
				lineno += 1
				cont = False
		return [lineno, pat]
			
	def do(self, cube):
		if(self.conditionType == Algorithm.IF):
			m = self.match(cube)
			if m >= 0:
				if self.doSteps(cube, m): return True
			elif self.elseAlgo != None:
				if self.elseAlgo.do(cube): return True
		elif(self.conditionType == Algorithm.WHILE):
			m = self.match(cube)
			while m >= 0:
				if self.doSteps(cube, m): return True
				m = self.match(cube)
		elif(self.conditionType == Algorithm.UNTIL):
			m = self.match(cube)
			j = 0
			while m < 0 and j <= 50:
				if self.doSteps(cube, 0): return True
				m = self.match(cube)
				j += 1
			if j >= 50:
				print("Erreur - boucle infinie detectee")
				return True
		return False
				
	def doSteps(self, cube, m):
			for step in self.step:
				if isinstance(step, AlgoAction):
					if step.do(cube, m): return True
				else:
					if step.do(cube): return True
			return False
				
	def match(self, cube):
		for p in self.patterns:
			m = p.match(cube)
			if m >= 0: return m
		return -1
				
class AlgoMatch(Algorithm):

	def __init__(self, parent, patterns, c, action):
		self.patterns = patterns
		self.action = action
		self.c = c
		
		self.parent = parent
		self.conditionType = Algorithm.IF
		self.step = []
		self.elseAlgo = None
		
	def do(self, cube):
		m = self.patterns[0].matchOnly(cube, self.c)
		if m >= 0:
			n = 0
			m = self.patterns[0].match(cube)
			while m < 0 and n < 4:
				cube.do(self.action, m, True)
				m = self.match(cube)
				n += 1
				
			if n != 4:
				print( cube.zDecal(self.action, m, n), ' - ', sep='', end='')
				if self.doSteps(cube, m): return True
			elif self.elseAlgo != None:
				if self.elseAlgo.do(cube): return True
		
		elif self.elseAlgo != None:
			if self.elseAlgo.do(cube): return True
		
	