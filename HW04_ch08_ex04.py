#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    # Explain what is wrong, if anything, here.
    # This function evaluates only the first letter of the string and exits the execution.
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    # Explain what is wrong, if anything, here.
    # What I supposse is wrong with this function is that it is evaluating the letter 'c', not the string contained in the variable c.
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    # Explain what is wrong, if anything, here.
    # What is wrong is that it only evaluates the last letter.
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    #Explain what is wrong, if anything, here.
    # What is wrong is that in the first execution the variable 'flag' can get the value 'True' and after that it will always returns 'True' no matter what 
    # happens with the sentence 'c.islower()'. It will only work partially if the fisrt letter is capital.
    flag = False
    for c in s:
        flag = flag or c.islower()
        #print(c + ' ' + str(flag))
    return flag


def any_lowercase5(s):
    # Explain what is wrong, if anything, here.
    # This function works fine for me, the function evaluates each letter and quits the the execution as soon as it finds the first capital letter.
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    #print("Hello World!")
    print(any_lowercase5("hisstringmefsFesupthefunction"))


if __name__ == '__main__':
    main()
