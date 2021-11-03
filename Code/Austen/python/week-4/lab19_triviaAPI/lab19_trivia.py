import json
import requests
from functions.url import build
from functions.play import play


# *Prompt the user for each of api parameter.
topics = [
    {'parameter': 'any', 'name': 'Any Category'},
    {'parameter': '9', 'name': 'General Knowledge'},
    {'parameter': '10', 'name': 'Entertainment: Books'},
    {'parameter': '11', 'name': 'Entertainment: Film'},
    {'parameter': '12', 'name': 'Entertainment: Music'},
    {'parameter': '13', 'name': 'Entertainment: Musicals &amp; Theatres'},
    {'parameter': '14', 'name': 'Entertainment: Television'},
    {'parameter': '15', 'name': 'Entertainment: Video Games'},
    {'parameter': '16', 'name': 'Entertainment: Board Games'},
    {'parameter': '17', 'name': 'Science &amp; Nature'},
    {'parameter': '18', 'name': 'Science: Computers'},
    {'parameter': '19', 'name': 'Science: Mathematics'},
    {'parameter': '20', 'name': 'Mythology'},
    {'parameter': '21', 'name': 'Sports'},
    {'parameter': '22', 'name': 'Geography'},
    {'parameter': '23', 'name': 'History'},
    {'parameter': '24', 'name': 'Politics'},
    {'parameter': '25', 'name': 'Art'},
    {'parameter': '26', 'name': 'Celebrities'},
    {'parameter': '27', 'name': 'Animals'},
    {'parameter': '28', 'name': 'Vehicles'},
    {'parameter': '29', 'name': 'Entertainment: Comics'},
    {'parameter': '30', 'name': 'Science: Gadgets'},
    {'parameter': '31', 'name': 'Entertainment: Japanese Anime &amp; Manga'},
    {'parameter': '32', 'name': 'Entertainment: Cartoon &amp; Animations'}
]
# *Include them in the request to get the list of questions.
url = build(topics)
response = requests.get(url)
content = response.content
content = json.loads(content)
content = content['results']
result = play(content)
print(result)
