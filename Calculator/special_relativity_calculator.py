# This code is made by MRayan Asim
# Function to calculate time dilation
def time_dilation(time, velocity):
    gamma = 1 / (1 - (velocity ** 2 / 299792458 ** 2))  # Lorentz factor
    time_dilated = time * gamma
    return time_dilated


# Function to calculate length contraction
def length_contraction(length, velocity):
    gamma = 1 / (1 - (velocity ** 2 / 299792458 ** 2))  # Lorentz factor
    length_contracted = length / gamma
    return length_contracted


# Function to calculate energy using E=mc^2
def energy(mass):
    c = 299792458  # Speed of light in m/s
    energy = mass * c ** 2
    return energy


if __name__ == "__main__":
    # Input values
    relative_velocity = float(input("Enter the relative velocity (m/s): "))
    proper_time = float(input("Enter the proper time (seconds): "))
    proper_length = float(input("Enter the proper length (meters): "))
    object_mass = float(input("Enter the mass of the object (kg): "))

    # Calculate time dilation, length contraction, and energy
    dilated_time = time_dilation(proper_time, relative_velocity)
    contracted_length = length_contraction(proper_length, relative_velocity)
    object_energy = energy(object_mass)

    # Output results without rounding
    print(f"Time dilation: {dilated_time:.15f} seconds")
    print(f"Length contraction: {contracted_length:.15f} meters")
    print(f"Energy (E=mc^2): {object_energy:.15f} joules")
