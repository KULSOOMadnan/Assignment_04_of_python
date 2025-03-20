MARS_GRAVITY = 0.378
MERCURY_GRAVITY = 0.376 
VENUS_GRAVITY = 0.889 
JUPITER_GRAVITY = 2.36 
SATURN_GRAVITY = 1.081 
URANUS_GRAVITY = 0.815 
NEPTUNE_GRAVITY = 1.14 
EARTH_GRAVITY = 1.0


def main():
    earth_weight_str = input('Enter a weight on Earth: ')
    planet = input("Enter a planet: ").capitalize()
    # print(planet)
    # Get the numeric value since input() returns a value in string form
    earth_weight = float(earth_weight_str)
    
# Determine the gravitational constant for the selected planet
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    else:
        # can assume user types in one of these planets, so this can be an else instead of elif
        gravity_constant = NEPTUNE_GRAVITY

    # Calculate the equivalent weight on the selected planet
    planetary_weight = earth_weight * gravity_constant
    rounded_planetary_weight = round(planetary_weight, 2)

    # Print the result
    print("The equivalent weight on " + planet + ":  " + str(rounded_planetary_weight))

    

if __name__ == "__main__":
    main()