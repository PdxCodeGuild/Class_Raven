home = input("Name something a person could fit in, but wouldn't want to: ")
admission = input("What is something you do to relax? ")
replacement = input("Something you would never EVER spend money on: ")
location = input("Where would you go if you needed a quick snack? ")
resource = input("Something a 3 year old would place a lot of value in: ")
request = input("If you could do anything right now for the next 3 hours, what would it be? ")

madlib = f"I live in a {home} down by the {location}. There's not a lot of {resource} but there's plenty of {replacement}. Now please {request}, as I can't be bothered to {admission}."
print(madlib)