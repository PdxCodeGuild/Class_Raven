test_list = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks_valleys = []
max_numbers = []


while test_list != [0 for x in test_list]:  ## while test_list is not equal to all zeros:
    
    for number in test_list:
        
        if peaks_valleys != [] and number == max(test_list) and number not in max_numbers and max_numbers != []:
            ## if peaks_valleys empty, number is max in list, number not in max list, and max numbers not empty:
            index_position = test_list.index(number) # variable index = index of number in test list 
            peaks_valleys[index_position] = 'x' # add x to the same index position in peaks and valleys
            max_number = number # assign variable to current max number
            test_list[index_position] = 0 # turn test list number at current index position to 0
            ## this particular line of code causes code not to work on all lists since if i'm assigning the number in the
            #test list at this position to zero.. if there is another number later in list greater than 0, it will recognize that number as new max number in list and run through the loop unecessarily 
        
        elif number == max(test_list) and number not in max_numbers:  ## number is max number and not in max number list (this is essentially for the first max number in list only)
           idx = 'x'  
           peaks_valleys.append(idx)  ## add x to peaks and valleys list 
           max_number = number ## set max number variable to the current max number
           index_position = test_list.index(number)  ## same as previous if statement
           test_list[index_position] = 0 ## same as previous if statement
           
        elif len(peaks_valleys) < len(test_list): ## this lines ensures that when the peaks and valleys list first populates it will be same length as test_list and remain that way as code is ran 
           idx = ' '
           peaks_valleys.append(idx) ## appending x to peaks and valleys list if number for current iteration is not a max number
           
        else:
           continue
        
    max_numbers.append(max_number)  #creates list of max numbers that can be used to ensure we are not adding x for max number already assigned an x in peaks and valleys list 
    print('  '.join(peaks_valleys)) # joins all items in peaks and valleys list into one string
    continue






#tally up wins
#expenditure
#while loop...while time played is less than 100,000 for example
