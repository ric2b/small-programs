from __future__ import division # avoid integer division, so things like 1/3 don't return 0 in eval()

inputs = raw_input("please enter the 4 numbers separated by spaces: ").split()
if len(inputs) != 4:
    print("\nthe rules say 4 numbers but I guess if you knew them you wouldn't need this program ;)")

desiredResult = 24
operations = ['+', '*', '/', '-']

solutions = 0
for a in inputs: # for each number from 'inputs', the complete list
    index1 = inputs.index(a) # find the location of 'a' on the list
    remaining1 = inputs[:index1] + inputs[index1+1:] # make a list without 'a' by joining the list until 'a' with the list after 'a'

    for operation1 in operations: # for each operation
        for b in remaining1: # for each number from the 'remaining1' list
            index2 = remaining1.index(b)
            remaining2 = remaining1[:index2] + remaining1[index2+1:]

            for operation2 in operations: #  we don't need to remove the previous operation from the list because these CAN repeat
                for c in remaining2:
                    index3 = remaining2.index(c)
                    remaining3 = remaining2[:index3] + remaining2[index3+1:]

                    for operation3 in operations:
                        d = remaining3[0] # this is just to convert a list of a single character to a character

                        expression = a + operation1 + b + operation2 + c + operation3 + d # let's put everything together! (string concatenation)
                        if eval(expression) == desiredResult: # eval() evaluates a string as a mathematical expression, so we can get our result :D
                            print("found solution: " + expression + " = " + str(eval(expression)))
                            solutions += 1

print("found " + str(solutions) + " solutions")
