def main():
    
    val = 1
    while val > 0:

        planet_name = ""
        sun_name = ""
        mass_of_a_star = 0
        color_of_life = ""
        number_of_drops_of_rain = 0
        hours_spent_on_zoom = 0
        verbs = ""

        planet_name = input("Make up the name of a planet: ")
        sun_name = input("Make up the name of a sun: ")
        mass_of_a_star = input("Weight of that star: ")
        color_of_life = input("The color of life: ")
        number_of_drops_of_rain = input("Number of rain drops last week: ")
        hours_spent_on_zoom = input("Hours spent on Zoom: ") 
        verbs = input("Enter three comma separated verbs: ")

        verb_1, verb_2, verb_3 = verbs.split()

        print(f"\n\nIt has been recently discovered that mankind originated on {planet_name}")
        print(f"Upon indication that {sun_name}, the sun, was turning into a {color_of_life} dwarf, exactly {number_of_drops_of_rain} fled.")
        print(f"Little did anyone know, {verb_1} {verb_2} and {verb_3} would have cost more than {hours_spent_on_zoom}.")

        quit = input("\n\nPress Enter to quit. Otherwise enter 'play again': ")
        if quit == "":
            val = 0
        else:
            val = 1

if __name__ == '__main__':
    main()