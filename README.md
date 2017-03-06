# Interactive Rubik's

This project is an old project I made when I was learning Python.
It is basically a shell that allows playing with a rubik's cube.
It is patched with an homemade algorithm language that allows easily creating solving algorithms that adapt to the cube.

## Usage

The setup is fairly easy, you just need to install colorama
```
pip install colorama
```

And then, start the program using
```
python interactive-rubiks.py
```

## Shell commands

Here is the list of commands the shell accepts :

* `help` will display the list of commands.
* `exit` will quit the prompt
* `do` followed by a space-separated sequence of moves, will update the cube according to the given sequence.  
The moves are defined as in standard rubiks algorithms.
* `import` followed by a name such that `name.algo` will be loaded into the algorithm set.
* `doalgo` followed by the name of an already-imported algorithm.
* `reset` will refresh the cube to its initial state
* `set <name> = <val>` to set one of the following option :
 * `interactive = true/false`. Will make algorithm pause during the process, so you can do moves on you're own cube.
 * `coloredOutput = true/false`. Will display colors instead of numbers.
 * `verbose = 2/1/0`. Will respectively display moves and cube, only cube, or nothing.
* `randomize` to generate a random cube. If not followed by `silent`, it will display the move sequence so you can reproduce it on your own cube.

## Algorithm language

The heart of the project is its algorithm language. It allows easily defining scalable algorithms depending on the state of the cube.
The language is a one command per line language.

Basic commands are :

* `print` followed by a string to be printed
* `printCube` to print the cube in its current state
* `pause` will pause the algorithm, waiting for the user output
* `import` and `doalgo`
* `do` (can be followed by `silent` if you don't want to output the sequence)

But most importantly, there are conditionnal blocks.
Conditions are expressed using cube patterns.
For exemple, this is a pattern :
```
						1 1 1
						1 1 1
						1 1 _
				4 4 4	5 5 _	_ 2 2	0 0 0
				4 4 4	5 5 5	2 2 2	0 0 0
				4 4 _	_ 5 _	_ 2 2	0 0 0
						_ 3 _
						3 3 3
						3 3 3
```
Numbers are used to represent cells that have the same color. Underscore are used to describe any color.

Patterns are rotation insensitive. When we're trying to match a pattern, we try it 4 times rotating the cube around the z axis.
Then, when matched, the rotation is remembered and every action that follows is re-adapted to the rotation.

You can also mix multiple patterns separating them with `or` line.

Now this is how you use a conditionnal block :
```
if/match x doing y
  condition
  commands
[elseif/elseif-match doing y
  commands]*
[else
  commands]?
end
```

The difference between match and if, is that `match x doing y` will first try matching only the number `x`, and if done, it will then do `y` until the full pattern is matched.

You can also use loops :
```
until/while
  condition
  commands
end
```
