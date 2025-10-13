def main():
    mass = float(input("Enter the mass (kg): "))
    velocity = float(input("Enter the velocity (m/s): "))

    momentum = mass * velocity
    kinetic_energy = 0.5 * mass * velocity ** 2

    print("Momentum:", momentum)
    print("Kinetic energy:", kinetic_energy)

main()
