

def mass_and_moles_function():
    molar_mass1 = float(input("Molar mass 1 - "))
    coefficient1 = float(input("Coefficient 1 - "))
    given_mass2 = float(input("Mass 2 - "))
    molar_mass2 = float(input("Molar mass 2 - "))
    coefficient2 = float(input("Coefficient 2 - "))
    calculate1 = molar_mass1 * coefficient1
    calculate2 = molar_mass2 * coefficient2
    calculate3 = given_mass2 / calculate2
    result = calculate3 * calculate1
    print(f"             a              =            {given_mass2}           ")
    print("--------------------------     --------------------------")
    print(f"       {coefficient1} * {molar_mass1}                  {coefficient2} * {molar_mass2}     \n\n")
    print(f"         a({calculate2})          =         ({given_mass2})({calculate1})  \n\n")
    print('              a             =        ' + str(result))


def mass_and_mole():
    print("              a             =            mass2           ")
    print("--------------------------     --------------------------")
    print("Coefficient1 * Molar mass1     Coefficient2 * Molar mass2\n")
    print("Your missing mass must be on the left")
    mass_and_moles_function()
    print("\n\n\n\n\n")
