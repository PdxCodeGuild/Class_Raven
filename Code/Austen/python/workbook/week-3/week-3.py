class importer:
  def directory():
    import os
    current_directory = os.getcwd()
    current_directory = os.path.dirname(current_directory)
    current_directory = os.path.dirname(current_directory)
    return current_directory

  def path():
    import sys
    directory = importer.directory()
    path = sys.path.append(directory)
    return path

  def response():
    importer.path()
    from utilities.responses import response
    return response

  def timestamp():
    importer.path()
    from utilities.timestamp import now
    return now

  def labs():
    from workbook.lab_ATM import lab_ATM
    from workbook.lab_search_sort import lab_search_sort
    labs = [lab_ATM, lab_search_sort]
    return labs


def week_3():
    response = importer.response()
    now = importer.timestamp()
    labs = importer.labs()
    lablist = ['ATM', 'search', 'done']
    lab = input(f'Which lab?\n{lablist}\n')
    lab = response.validate(lab, lablist)
    results = []
    while lab != 'done':
        if lab == 'ATM':
            result = labs[0]()
            stamp = now.result()
            result = f'{stamp} \n- [{result}]'
            results.append(result)
        elif lab == 'search':
            result = labs[1]()
            stamp = now.result()
            result = f'{stamp} \n- [{result}]'
            results.append(result)
        lab = input(f'Which lab?\n{lablist}\n')
        lab = response.validate(lab, lablist)
    file = open('data/results.log', 'a')
    for result in results:
        file.write(f'\n{result}')
        print(result)


week_3()
