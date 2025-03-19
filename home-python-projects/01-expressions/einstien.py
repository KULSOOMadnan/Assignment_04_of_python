# constant value for the speed of light -- 
C = 299792458 #m/s


# Function to calculate the energy of a photon

def main():
    """ Calculate the energy formula E = mc^2 """
    mass_in_kg = float(input("Enter the mass in kg: "))
    energy_in_joules = mass_in_kg * (C ** 2 )
    # Display work to the user
    print(f"Formula Of Energy : e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    
    print(str(energy_in_joules) + " joules of energy!")

if __name__ == '__main__':
    
    main()
   