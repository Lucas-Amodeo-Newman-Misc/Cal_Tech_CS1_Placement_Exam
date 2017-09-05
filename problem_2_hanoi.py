import sys

class Hanoi():

    #Initializes state.
    def __init__(self, starting_disks):
        self._state = {} # state is implemented as a dictionary of 3 lists, one per peg
        self._state["A"] = [(i) for i in range(starting_disks, 0, -1)] # creates the starting tower of disks on peg A
        self._state["B"] = []
        self._state["C"] = []

    #Displays the current contents of each peg.
    def display(self):
        print("A:  " + " ".join(list(map(str, self._state["A"]))))
        print("B:  " + " ".join(list(map(str, self._state["B"]))))
        print("C:  " + " ".join(list(map(str, self._state["C"]))))
        print()

    #Moves the top disk from a starting peg to a target peg.  Flags illegal moves.
    def move(self, start_peg, target_peg):
        start_disk = self._state[start_peg][-1] # the top disk
        if self._state[target_peg]: # the target peg has contents already, checks the intended move for legality
            target_disk = self._state[target_peg][-1]
            if start_disk > target_disk:
                print("Illegal move, '{0}' from '{1}' is smaller than '{2}' from '{3}'".format(target_disk, target_peg, start_disk, start_peg))
                raise ValueError
        self._state[target_peg].append(self._state[start_peg].pop()) # moves the disk
        self.display() # displays state - a convenient time to do this due to the recursive nature of the program, though it could go elsewhere

    #Solves the puzzle by transfering the entire stack on peg A to peg B
    def solve(self):
        self._transfer_stack("A", "B", len(self._state["A"]))

    #Recursive algorithm for transfering a stuck of arbitrary size from one peg to another.
    def _transfer_stack(self, start_peg, target_peg, depth):
        if depth > 1: # recursive case
            pegs = ["A", "B", "C"] # determines the intermediate peg
            for i in pegs:
                if i not in (start_peg, target_peg):
                    other_peg = i
            self._transfer_stack(start_peg, other_peg, depth-1) # transfers the n-1 stack to the intermediate peg
            self.move(start_peg, target_peg) # transfers the bottom disk to the target peg
            self._transfer_stack(other_peg, target_peg, depth-1) # transfers the n-1 stack to the target peg
        else: # base case
            self.move(start_peg, target_peg)

# main program, checks for correct input
try:
    if len(sys.argv) != 2:
        print("Wrong number of arguments - please input one natural number.")
    else:
        n_disks = int(sys.argv[1])
        if n_disks < 1:
            print("The number of disks must be a natural number.")
        else:
            Hanoi(n_disks).solve()
except TypeError:
    print("The number of disks must be a natural number.")
except ValueError:
    print("The number of disks must be a natural number.")
