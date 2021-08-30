from mass_and_moles import mass_and_mole
from Limiting_Reagents import limitingreagent
from balancing_equation import balancing_equation_function
while True:
    function = input("Chemistry Calculator\n1. mass and moles\n2. balancing equation ( 19 Aug 2021 )\n3. limiting reagent ( 17 Aug 2021 )\n")
    if function == '1':
        mass_and_mole()
    elif function == '2':
        balancing_equation_function()
    elif function == '3':
        limitingreagent()
    con = str(input("Continue ( y \ n ) : "))
    if con == 'n':
        break
