# Lauren Phan and Chun Tseng
# we are aware our solution isn't correct/complete.  we will fgure out
# better way to represent the tree and account for branching in HW3.
# we tried to read in the list, parse it into a list of strings
# and provide surface level validation. we tried to come up with pl tree rules as well but
# our solution/algorithm is essentially incorrect at the moment.

def UI(arg, unticked):
    #how do we implement this?
    return
def EI():
    # "                    "?
    return
#disjunction
def D(p, q, unticked):
    unticked.append(p, q)
    return untcked
#non-disjunction
def ND(p, q, unticked):
    unticked.append("NEG"+p)
    unticked.append("NEG"+q)
    return unticked
#conjunction
def C(p, q, unticked):
    unticked.append(p)
    unticked.append(q)
    return unticked
#non-conjunction
def NC(p, q, unticked):
    unticked.append("NEG" + p, "NEG" + q)
    return unticked
#implication
def I(p, q, unticked):
    unticked.append("NEG"+p,q)
    return unticked
def NI(p, q, unticked):
    unticked.append(p)
    unticked.append("NEG"+q)
    return unticked
#double-negation
def DN(p, unticked):
    unticked.append(p)
    return unticked
#negation
def N(p, unticked):
    unticked.append(p)
    return unticked

def isOpen(unticked):
    #determines whether an open path exists on the current level
    return
#take in the list of arguments and break them up
def read(args):
    arg = []
    #split arguments in list by " "
    #store individually split arguments into list arg
    for st in args:
        temp = st.split(" ")
        arg.append(temp)
    #print to check
    #for elem in arg:
    #    print elem
    #return the list of lists of broken up arguments
    return arg

#check for malformed string
def check(arg):

### needs revision, we can't use simple iteration here? maybe recursion to validate as we go along?

    #list to hold individual strings
    args = []

    #parse string by space into list
    for elem in arg:
        args = elem.split()
    for i in range(0, len(args)):
        #checking for quantifiers
        if args[i] == "FORALL" or args[i] == "EXISTS":
            #at end of args
            if i+ 1 > len(args):
                return False
            #quantifier identified
            #ensure the next element is a single variable
        elif args[i] == "AND" or args[i] == "OR":
            #at end of args
            if i+1 > len(args):
                return False
            #do something here?
        elif args[i] == "NEG":
            #at end of args
            if i+1 > len(args):
                return False
            #negation found
        else:
            return False

#build the tree
def construct_tree(list):
    list_arg = read(list)

    if(check(list_arg) == True):
        print 0
        #call to above functions after implementation
    else:
        print "INVALID_INPUT"
        return
check(["FORALL X"])
