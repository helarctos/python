# Raven Travillian, Quiz 1: Basic Programming Competence

# helper function: summation

def summation(array1):                                      # summation receives an array passed to it by another function
    sum = 0                                                 # initialize sum
    for i in range(len(array1)):                            # go through all the elements of the array one by one
        if (array1[i] % 2 > 0) or (array1[i] % 3 == 0):     # if current element is odd, or a multiple of 3, 
            sum = sum + array1[i]                           # then add current element to sum for comulative total
    return sum                                              # when the loop through the array is finished, the function returns the cumulative total


# main routine

def main():
    numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]               # create array, initialize all elements in array to 0
    element = 0                                             # initialize element
    for i in range(15):                                     # loop through array one element at a time
        element = element + 1                               # increment element
        numbers[i] = element                                # set current element of array equal to current value of element
    print "The sum of the numbers in the array is ",summation(numbers), "." # pass array to summation function

main()
