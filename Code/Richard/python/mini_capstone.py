import urllib.request, json

def load(): #loads and saves data from site to local json file.  You can use this to update file.
    with urllib.request.urlopen("https://data.nasa.gov/resource/y77d-th95.json") as url:
        data = json.loads(url.read().decode())
        with open('C:/Users/Richard Watkins/pdx_code/class_raven/Code/Richard/python/meteorite.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)
    return

mass_list =[]
year_list =[]
counter = 0
year_dict = {}
mass_dict={}



with open('C:/Users/Richard Watkins/pdx_code/class_raven/Code/Richard/python/meteorite.json', 'r') as json_file:
    data = json.loads(json_file.read())
    print(len(data))



def extract_data(database):
    entry = data[counter]
    # try: 
    #     entry['mass']
    #     mass = int(entry['mass'])
    #     mass_list.append(mass)
    # except:
    #     print('KeyError: 'mass'')
    year = int(entry['year'][:4])
    year_list.append(year)
    return year#, mass



for item in data:
    extract_data(data)
    counter += 1

for year in year_list: #imported and altered this process from lab_13
    if year in year_dict:
        year_dict[year] += 1
    else:
        year_dict[year] = 1

high_years = list(year_dict.items()) # .items() returns a list of tuples
high_years.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(high_years))):  # print the top 10 words, or all of them, whichever is smaller
    print(high_years[i])

# for mass in mass_list: #imported and altered this process from lab_13
#     if mass in mass_dict:
#         mass_dict[mass] += 1
#     else:
#         mass_dict[mass] = 1

# high_mass = list(mass_dict.items()) # .items() returns a list of tuples
# high_mass.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(high_mass))):  # print the top 10 words, or all of them, whichever is smaller
#     print(high_mass[i])

# print(mass_list)
# print(year_list)