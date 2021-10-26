#Build list by the name of peakvalley
peakvalley = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]
#Create for loop to enumerate through the peakvalley list using the enumerate function.
for i, value in enumerate(peakvalley):
#Conditional statement to test if the index is at the first or last location
    if i < 1 or i == len(peakvalley)-1:
#If the condition is true then skip the rest of the loop
        continue
#If the condition is false then continue
    else:
#Establish variables for the previous value, current value, and next value at the index behind, current and ahead.
        value_behind = peakvalley[i-1]
        value = value
        value_ahead = peakvalley[i+1]
#Now that we have those values, test the values for peaks and valleys. If the value is greater than the value ahead and behind it, it is a peak.
        if value > value_behind and value > value_ahead:
#If the condition is true, then print the index and the value of the peak
            print(f'Peak at index {i} with value {value}')
#Now test if the value is less than the value ahead and behind it to find a valley
        elif value < value_behind and value <value_ahead:
#If the condition is true, then print the index and the value of the valley
            print(f'Valley at index {i} with value {value}')