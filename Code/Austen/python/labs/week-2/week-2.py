def importutilities():
  import sys
  utilspath = 'X:\\python\\'
  sys.path.append(utilspath)

# * contains uis to access each lab completed throughout the week
def week_2():
    importutilities()
    from utilities.responses import response
    def monday():
        from labs.Oct_18 import lab_lottery
        results = []
        options = ['lottery', 'done']
        print(options)
        lab = input('Which lab would you like to access?\n').lower()
        lab = response.validate(lab, options)
        while lab != 'done':
            if lab == 'lottery':
                result = f'lottery: {lab_lottery()}'
            print(options)
            lab = input('Which lab would you like to access?\n').lower()
            results.append(result)
        return results
    def tuesday():
        from labs.Oct_19 import lab_blackjack
        results = []
        options = ['blackjack', 'done']
        print(options)
        lab = input('Which lab would you like to access?\n').lower()
        lab = response.validate(lab, options)
        while lab != 'done':
            if lab == 'blackjack':
                result = f'blackjack: {lab_blackjack()}'
            print(options)
            lab = input('Which lab would you like to access?\n').lower()
            results.append(result)
        return results
    def wednesday():
        from labs.Oct_20 import lab_rot_cipher
        results = []
        options = ['cipher', 'done']
        print(options)
        lab = input('Which lab would you like to access?\n').lower()
        lab = response.validate(lab, options)
        while lab != 'done':
            if lab == 'cipher':
                result = f'rot cipher: {lab_rot_cipher()}'
            print(options)
            lab = input('Which lab would you like to access?\n').lower()
            results.append(result)
        return results

    def thursday():
        from labs.Oct_21 import lab_dad_jokes
        results = []
        options = ['jokes', 'done']
        print(options)
        lab = input('Which lab would you like to access?\n').lower()
        lab = response.validate(lab, options)
        while lab != 'done':
            if lab == 'jokes':
                result = f'dad jokes: {lab_dad_jokes()}'
            print(options)
            lab = input('Which lab would you like to access?\n').lower()
            results.append(result)
        return results

    def friday():
        from labs.Oct_22 import lab_count_words
        results = []
        options = ['count words', 'done']
        print(options)
        lab = input('Which lab would you like to access?\n').lower()
        lab = response.validate(lab, options)
        while lab != 'done':
            if lab == 'count words':
                result = f'count words: {lab_count_words()}'
            print(options)
            lab = input('Which lab would you like to access?\n').lower()
            results.append(result)
        return results

    def ui():
        results = []
        options = ['monday', 'tuesday', 'wednesday',
                   'thursday', 'friday', 'done']
        print(options)
        day = input('Which day would you like to access?\n').lower()
        day = response.validate(day, options)
        while day != 'done':
            if day == 'monday':
                result = f'Monday: {monday()}'
                results.append(result)
                print(options)
            if day == 'tuesday':
                result = f'Tuesday: {tuesday()}'
                results.append(result)
                print(options)
            if day == 'wednesday':
                result = f'Wednesday: {wednesday()}'
                results.append(result)
                print(options)
            if day == 'thursday':
                result = f'Thursday: {thursday()}'
                results.append(result)
                print(options)
            if day == 'friday':
                result = f'Friday: {friday()}'
                results.append(result)
                print(options)
            day = input('Which day would you like to access?\n').lower()
        return results
    results = ui()
    return results


def run_and_write():
    importutilities()
    from utilities.timestamp import now
    file = open('docs/results-log.txt', 'a')
    results = week_2()
    stamp = now.result()
    results.insert(0, stamp)
    file.write('\n')
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
