"""
PDX Code Guild Full Stack Bootcamp
->Lab 10
  Dad Jokes API
Michael B

Dad Joke API
Use the Dad Joke API to get a dad joke and display it to the user. You may want to also use time.sleep to add suspense.

Part 1
Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ with the accept header as application/json. This will return a dad joke in JSON format. You can then use the .json() method on the response to get a dictionary. Get the joke out of the dictionary and show it to the user.

Part 2 (optional)
Add the ability to "search" for jokes using another endpoint. Create a REPL that allows one to enter a search term and go through jokes one at a time. You can also add support for multiple pages.

requests.get(url, {'accept': 'application/json'}) 
"""


def track_keys() -> None:
    from pynput.keyboard import Key, Listener

    def on_press(key):
        print("{0} pressed".format(key))
        if key == Key.esc:
            return False

    with Listener(
        on_press=on_press,
    ) as listener:
        listener.join()


def main_program() -> None:
    from time import sleep
    import requests

    extra_punct = ""  # Sometimes puncutation is cut.
    response = requests.get(
        "https://icanhazdadjoke.com/", headers={"Accept": "application/json"}
    )
    json_joke = response.json()
    asked_joke = json_joke["joke"].split("?", 1)
    punctuation = "?"
    if len(asked_joke) == 1:  # If not ? (that didn't split).
        asked_joke = json_joke["joke"].split(",", 1)
        punctuation = ","
    if len(asked_joke) == 1:  # if not ? and , (they didn't split).
        asked_joke = json_joke["joke"].split(".", 1)
        punctuation = "."
    print(f"{asked_joke[0].strip()}{punctuation}")  # Readd puncuation that was split.
    for i in range(1, 4):  # comedic suspense
        sleep(0.35)
        print("." * i)
    if asked_joke[1] != "":  # Joke is not a one liner.
        print(f"{asked_joke[1].strip()}{extra_punct}")
    sleep(3)  # Flair.
    print(f"\n\nHahahahah")
    sleep(0.25)
    print("ha")


if __name__ == "__main__":
    from multiprocessing import Process

    # p1 = Process(target=track_keys)
    # p1.start()
    p2 = Process(target=main_program)
    p2.start()
    # p1.join()
    p2.join()
