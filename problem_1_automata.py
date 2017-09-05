import sys
from random import randrange

class Rule(): # Represents the rule of the automaton

    # Takes a 4-tuple (zero, one, two, three) corresponding to the rule spec.    
    def __init__(self, tupl):
         self._tupl = tupl

    # Applies the rule spec to an inputted sum to produce a cell value.
    def cell(self, value):
         return self._tupl[value]

class Line(): # Represents a single line of cells

    def __init__(self):
        self._contents = []

    # adds a cell to the line
    def add(self, value):
        self._contents.append(value)

    # prints the line as a string
    def display(self):
        print("".join(list(map(str, self._contents))))

    # creates a SumLine
    def export_sumline(self):
        return SumLine(self._contents)

    def random(self, width):
        self._contents = [randrange(0, 2) for i in range(width)]

class SumLine(): # Represents a single line of sums, suitable for interpretation by the rule.

    # creates the list of sums for each location in the line
    def __init__(self, contents):
        full_contents = [0] + contents + [0] # augementation to avoid problems at the margin
        trios = [[full_contents[j] for j in range(i, i+3)] for i in range(len(full_contents)-2)] # creates a list of cell triplets
        self._values = [sum(i) for i in trios] # sums each cell triplet to create the list of sums

    # uses a rule to produce a new line
    def export_line(self, rule):
        new_line = Line()
        for i in self._values:
            new_line.add(rule.cell(i)) 
        return new_line

class Automaton():

    # configures the automation based on the command line arguments 
    def __init__(self, args):
        self._width = args[0]
        self._gens = args[1]
        self._rule = Rule(args[2:])
        self._lines = []

    # appends and displays the most recently created line
    def _add_line(self, line):
        self._lines.append(line)
        line.display()

    # runs the automation        
    def run(self):
        self._lines = []
        first_line = Line() 
        first_line.random(self._width) # randomized first line
        self._add_line(first_line)
        for i in range(self._gens-1):
            new_sumline = self._lines[-1].export_sumline() # used the last added line to create a sumline
            new_line = new_sumline.export_line(self._rule) # uses the newly created sumline to produce the next line
            self._add_line(new_line)

            
# main program, checks for valid command line arguments before starting
try:
    args = list(map(int, sys.argv[1:]))
    if args[1] < 1:
        print("The automation must last at least one generation.")
    elif list(filter(lambda x: x < 0, args)):
        print("All arguments to configure the automaton must be whole numbers.")
    elif list(filter(lambda x: x > 1, args[2:])):
        print("Arguments which configure the rule must be either 0 or 1.")
    else:
        Automaton(args).run()
except TypeError:
    print("All arguments to configure the automaton must be whole numbers.ME")
except ValueError:
    print("All arguments to configure the automaton must be whole numbers.")    
