# quick component to convert degrees C to F.
# Function takes in value, does conversion and puts answer into a list


def to_f (from_c):
    fahrenheit = (from_c * 9/5) + 32
    return fahrenheit


# Main Routine
tempuratures = [0, 40, 100]
converted = []

for item in tempuratures:
    answer = to_f(item)
    ans_statement = "{} degrees C is {} degrees F".format(item, answer)
    converted.append(ans_statement)

    print(converted)


   # ['0 degrees C is 32.0 degrees F',
   # '40 degrees C is 104.0 degrees F',
   # '100 degrees C is 212.0 degrees F']
