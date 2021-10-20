from tools.stamp import Stamp


# * contains uis to access each lab completed throughout the week
def week_2():
    ''
# * allows the user to continuously access each monday lab
    def monday():
        from labs.Oct_18 import lab_pick_6
        results = []
        options = ['pick_6', 'done']
        print(options)
        lab = input('Which lab would you like to access?\n').lower()
        while lab != 'done':
            if lab == 'pick_6':
                result = f'pick_6: {lab_pick_6()}'
            print(options)
            lab = input('Which lab would you like to access?\n').lower()
            results.append(result)
        return results
# * allows the user to continuously access each tuesday lab

    def tuesday():
        from labs.Oct_19 import lab_blackjack
        results = []
        options = ['blackjack', 'done']
        print(options)
        lab = input('Which lab would you like to access?\n').lower()
        while lab != 'done':
            if lab == 'blackjack':
                result = f'blackjack: {lab_blackjack()}'
            print(options)
            lab = input('Which lab would you like to access?\n').lower()
            results.append(result)
        return results

# * allows the user to continuously access each available day
    def ui():
        results = []
        options = ['monday', 'tuesday', 'done']
        print(options)
        day = input('Which day would you like to access?\n').lower()
        while day != 'done':
            if day == 'monday':
                result = f'Monday: {monday()}'
                results.append(result)
                print(options)
            if day == 'tuesday':
                result = f'Tuesday: {tuesday()}'
                results.append(result)
                print(options)
            day = input('Which day would you like to access?\n').lower()
        return results
    results = ui()
    return results


# * creates a file to record results and runs the week_2 ui
def run_and_write():
    file = open('week-2/results-log.txt', 'a')
    results = week_2()
# * adds an entry to identify the results
    stamp = Stamp().results()
    results.insert(0, stamp)
    file.write('\n')
# * prints and writes each result
    counter = 0
    for result in results:
        if counter > 0:
            result = f'{counter} of {len(results)-1} - {result}\n'
        else:
            result = f'{result}\n'
        print(result)
        file.write(result)
        counter += 1


run_and_write()
