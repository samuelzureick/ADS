import sys

from knapsack import knapsack

class enum_knapsack(knapsack):
    def __init__(self, filename):
        knapsack.__init__(self, filename)
        
    def enumerate(self):
        # Do an exhaustive search (aka enumeration) of all possible ways to pack
        # the knapsack.
        # This is achived by creating every "binary" solution vectore of length Nitems.
        # For each solution vector, its value and weight is calculated
        
        solution = [False]*(self.Nitems + 1) # (binary/ true/false) solution vectore representing items pack
        best_solution = [False]*(self.Nitems + 1) # (binary) solution veectore for best solution found
        j = 0.0
        
        self.QUIET = False
        best_value = 0 # total value packed in the best solution
        checked = 1
        while (not self.next_binary(solution, self.Nitems)):
            # ADD CODE IN HERE TO KEEP TRACK OF FRACTION OF ENUMERATION DONE
            frac = checked/(2**self.Nitems)
            if (checked % 100000 == 0):
                perc = str(frac)[2]
                bar = "\r["
                for i in range(int(perc)):
                    bar+="="
                for i in range(10-int(perc)):
                    bar+=" "
                bar+="] progress"
                print(bar,end='')
            


            # calculates the value and weight and feasibility
            infeasible = self.check_evaluate_and_print_sol(solution)
            checked+=1
            # ADD CODE TO PRINT OUT BEST SOLUTION
            if (not infeasible):
                if self.total_value > best_value:
                    best_value = self.total_value
                    best_solution = solution
        print("\r[==========]",end='')
        print("\nvalue="+str(best_value))
        
        



    def next_binary(self, sol, Nitems):
        # Called with a "binary" vector of length Nitmes, this
        # method "adds 1" to the vector, e.g. 0001 would turn to 0010.
        # If the string overflows, then the function returs True, else it returns False
        i = Nitems
        while (i > 0):
            if (sol[i]):
                sol[i] = False
                i = i -1
            else:
                sol[i] = True
                break
        if (i == 0):
            return True
        else:
            return False
        
            


knapsk = enum_knapsack(sys.argv[1])
knapsk.print_instance()
knapsk.enumerate()


