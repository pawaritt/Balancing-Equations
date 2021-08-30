def limitingreagent():
    range__ = input("reactant range : ")
    total_mass = input("mass of each reactant : ")
    reactant_list = []
    reactant_dict = {}
    for x in range(0, int(range__)):
        mylist = []
        element = input(f"element {x+1} : ")
        molar_mass = input(f"molar mass {x+1} : ")
        coefficient = input(f"coefficient {x + 1} : ")
        reactant_list.append(element)
        mylist.append(molar_mass)
        mylist.append(coefficient)
        reactant_dict[element] = mylist
    # reactant_dict = {"Ag": [107.87, 4], "H2S": [34.1, 2], "O2": [32, 1]}
    # total_mass = 300
    # reactant_list = ["Ag", "H2S", "O2"]
    ans = {}
    ans_print = {}
    for chosen_element in reactant_dict:
        mass = reactant_dict[chosen_element][0]
        result = float(total_mass) / float(mass)
        reactant_dict[chosen_element][0] = result
        print(f"{str(chosen_element)} = {str(total_mass)} / {str(mass)} = {str(result)}")
    print()
    for x in range(0, len(reactant_list)):
        limiting_element = reactant_list[x]
        if x == len(reactant_list) - 1:
            needed_element = reactant_list[x - (len(reactant_list) - 1)]
        else:
            needed_element = reactant_list[x + 1]
        result = float(reactant_dict[needed_element][0]) * (float(reactant_dict[limiting_element][1]) / float(reactant_dict[needed_element][1]))
        ans_limiting_element = float(reactant_dict[limiting_element][0]) - result
        print(f"{limiting_element} ----> {needed_element}\n_______\n{reactant_dict[needed_element][0]} x ( {reactant_dict[limiting_element][1]} / {reactant_dict[needed_element][1]} )  =  {result}")
        if ans_limiting_element > 0:
            if limiting_element in ans_print:
                if ans_limiting_element > ans[limiting_element]:
                    ans[limiting_element] = float(reactant_dict[limiting_element][0]) - result
                    ans_print[limiting_element] = f"{limiting_element} : {reactant_dict[limiting_element][0]} - {result} = {ans[limiting_element]}"
            else:
                ans[limiting_element] = float(reactant_dict[limiting_element][0]) - result
                ans_print[limiting_element] = f"{limiting_element} : {reactant_dict[limiting_element][0]} - {result} = {ans[limiting_element]}"

    if len(reactant_list) > 2:
        for x in range(0, len(reactant_list)):
            limiting_element = reactant_list[x]
            needed_element = reactant_list[x - 1]
            result = float(reactant_dict[needed_element][0]) * (float(reactant_dict[limiting_element][1]) / float(reactant_dict[needed_element][1]))
            ans_limiting_element = float(reactant_dict[limiting_element][0]) - result
            print(f"{limiting_element} ----> {needed_element}\n_______\n{reactant_dict[needed_element][0]} x ( {reactant_dict[limiting_element][1]} / {reactant_dict[needed_element][1]} )  =  {result}")
            if ans_limiting_element > 0:
                if limiting_element in ans_print:
                    if ans_limiting_element > ans[limiting_element]:
                        ans[limiting_element] = float(reactant_dict[limiting_element][0]) - result
                        ans_print[limiting_element] = f"{limiting_element} : {reactant_dict[limiting_element][0]} - {result} = {ans[limiting_element]}"
                else:
                    ans[limiting_element] = float(reactant_dict[limiting_element][0]) - result
                    ans_print[limiting_element] = f"{limiting_element} : {reactant_dict[limiting_element][0]} - {result} = {ans[limiting_element]}"
    print("\n\nI ---------------------------------------------------------------------------------------------------------------- I")
    for ans_element in ans_print:
        print(ans_print[ans_element])
    print("I ---------------------------------------------------------------------------------------------------------------- I")
