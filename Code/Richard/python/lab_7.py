print("Peaks and Valleys")
topo = []

def peaks(data):
    tops = [] 
    for i in range(1, len(data)-1):
        x= i-1
        y= i+1
        #if i == 0:
        #    x = i
        #if i == (len(data)):
        #    y = i
        if data[i] > data[x] and data[i] > data[y]:
            #print(x, i, y)
            tops.append(i)
    return tops

def valleys(data):
    bottoms = [] 
    for i in range(len(data)):
        x= i-1
        y= i+1
        if i == 0:
            continue
        if i == (len(data)):
            continue
        if data[i] < data[x] and data[i] < data[y]:
            #print((data[x]), (data[i]), (data[y]))
            bottoms.append(i)
    return bottoms

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
final = []
for valley in valleys(data):
    final.append(valley)

for peak in peaks(data):
    final.append(peak)

final.sort()
print(final)

#for i in data:
#    print((data[x]), (data[i]), (data[y]))
