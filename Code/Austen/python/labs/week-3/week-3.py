class importer:
    def system():
        import sys
        default = 'X:\\pdx-code-guild\\'
        root = input(
            f'enter your directory upto Class_Raven: \n (example: {default})\n')
        if root == 'default':
            root = default
        utilspath = f'{root}Class_Raven\\Code\\Austen\\python\\'
        sys.path.append(utilspath)


def week_3():
    importer.system()
    from utilities.responses import response
    from utilities.timestamp import now
    from workbook import Oct_25
    labs = ['ATM', 'done']
    lab = input(f'Which lab?\n{labs}\n')
    lab = response.validate(lab, labs)
    results = []
    while lab != 'done':
      if lab == 'ATM':
        result = Oct_25.lab_ATM()
        stamp = now.result()
        result = f'{stamp} \n- [{result}]'
        results.append(result)
      lab = input(f'Which lab?\n{labs}\n')
      lab = response.validate(lab, labs)
    file = open('data/results.log', 'a')
    for result in results:
      file.write(f'\n{result}')


week_3()
