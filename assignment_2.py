#Use comments.
#Do not print anything else in the output other than what is mentioned.
#Give the correct filename(as given, not the one that is on your local machine) while reading a file.
#Plagiariasm will be checked this time.
#Call every function after defining them, so that the funcion executes.
#Before submission, make sure to run the program and check whether everything is working.

## Assignment 2 ME369P
## Name:
## EID :
##
## Fill in the functions and class below


def star_wars():
    ## Write Code Here
    ## Use instructions from the assignment document
    ## Use starwars.txt as file


'''
Assume if a kwarg is not present, you should create the basic matrix
Assume the style is default to random
Assume the set is default to [0, 1]
kwargs can be :
    n =>  size of nxn matrix NOTE: You can assume if n is passed, i and j won't be
    i =>  number of rows     NOTE: If i is passed, assume j will be too
    j =>  number of columns
    range => [min, max] list
    set   => [number1, ..., numberN]
                NOTE: If set is specified, use that over range
                NOTE: If not specified, assume the set is the range
    style => a string which can be anything in {diagonal, upper, lower, symmetric, random}
                NOTE: any non-square matrix will be random
                NOTE: different styles will always be square matrices
    format => string that will be formatted as 1st and last element of each row
'''

def generateMatrix(**kwargs):
    ## Write Code Here
    ## print out matrix with newlines between rows
    ## print out elements in rows 1 space apart, no space at the beginning

class QuadraticEquation:
    # Make sure to add all the specs the instructions ask for

    def getRoots(self):
        return

if __name__ == '__main__':
    star_wars()
    generateMatrix()
    # You can do any testing you want here
    # Anycode you run here will not run when being graded...
    # Here are some examples of how QuadraticEquation will be used..
    equation = QuadraticEquation(3, 4, 5)
    A = equation.GetA()
    equation.SetB(5)
    discr = equation.GetDiscriminant()
    roots = equation.GetRoots()
