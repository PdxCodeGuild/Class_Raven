print("Distance Converter Program")
#conversion_factor ={'ft':0.3048, "mi":1609.34, "m":1, "km":1000}
user_distance = input('what is the distance?\n>')
user_distance = int(user_distance)

user_unit = input('what are the input units?\n(in, ft, yd, mi, m, km)\n>')

output_unit = input("what are the output units?\n(in, ft, yd, mi, m, km)\n>")

def convert(user_distance, user_unit, output_unit):
    conversion_factor ={'ft':0.3048, "mi":1609.34, "m":1, "km":1000, "in":0.0254, "yd":0.9144}
    output = user_distance * conversion_factor[user_unit]
    final_output = output / conversion_factor[output_unit]
    return final_output

print(f" {user_distance} {user_unit}s is equal to {convert(user_distance, user_unit, output_unit)} {output_unit}s.")