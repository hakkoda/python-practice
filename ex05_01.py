name = 'Jason Tennant'
age = 37
height = 76
weight = 220
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}")
print(f"He's {height} inches tall")
print(f"He's {weight} pounds heavy")
print(f"Actually, that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair")
print(f"His teeth are usally {teeth} depending on the soda")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")

# just wondering if using single quotes works with the string format thing...
print(f'will this work {total}')
