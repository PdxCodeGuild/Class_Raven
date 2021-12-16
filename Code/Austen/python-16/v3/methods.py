class search:
    def linear(data, value):
        index = 0
        for item in data:
            if item != value:
                index += 1
                found = False
            else:
                found = True
                break
        if found == False:
            index = 'value not in dataset'
        return index
    def binary(data, value):
        data = sort.bubble(data)
        length = len(data)
        Left = 0
        Right = length - 1
        while Left <= Right:
            mid = (Left + Right) // 2
            if data[mid] < value:
                Left = mid + 1
            elif data[mid] > value:
                Right = mid - 1
            else:
                return mid
        return "value not in dataset"
        
class sort:
    def bubble(data):
        def swap(data, index):
            item = data.pop(index)
            data.insert(index -1 , item)
            return
        length = len(data)
        swapped = ''
        while swapped != False:
            swapcount = 0
            for i in range(1, length):
                if data[i - 1] > data[i]:
                    swap(data, i)
                    swapped = True
                    swapcount += 1
            if swapcount == 0:
                swapped = False
        return data
    
