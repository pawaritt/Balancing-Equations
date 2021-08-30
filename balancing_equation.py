from balancing_calculation import calculation
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def balancing_equation_function():
    def remove(letter, input_word):
        remove_list = []
        pos_remove = []
        for x in range(0, len(letter)):
            pos_remove.append(input_word.find(letter[x]))
        for count in range(0, len(input_word)):
            remove_list.append(input_word[count])
        pos_remove.reverse()
        for remove_alpha in pos_remove:
            remove_list.pop(remove_alpha)
        input_word = ""
        for counter in range(0, len(remove_list)):
            input_word += remove_list[counter]
        return input_word


    def lower_check(molecular_formula):
        element = ""
        element_range = int(len(molecular_formula) - 1)
        for a in range(0, element_range):
            lower_or_not = molecular_formula[a].islower()
            element_check = molecular_formula[int(a + 1)].islower()
            if (lower_or_not is False) and (element_check is True):
                element += molecular_formula[a]
                element += molecular_formula[(a + 1)]
                break
            elif lower_or_not is False:
                element += molecular_formula[a]
                break
        if element_range == 0:
            element += molecular_formula[0]
        return element


    def organize_coefficient_no_parenthesis(number, coe_list):
        if (len(number) == 1) and (number[0].isnumeric() is False):  # one element left
            number = remove(number[0], number)
            coe_list.append(1)
        elif (number[0].isnumeric() is False) and (number[1].isnumeric() is False):  # element and element behind
            coe_list.append(1)
            number = remove(number[0], number)
        elif len(number) >= 3:
            if (number[0].isnumeric() is False) and (number[1].isnumeric() is True) and (number[2].isnumeric() is True):  # element and 2 number behind
                coe_list.append(int(str(number[1]) + str(number[2])))
                number = remove(number[0], number)
                number = remove(number[0], number)
                number = remove(number[0], number)
            elif (number[0].isnumeric() is False) and (number[1].isnumeric() is True):  # element and number behind
                coe_list.append(int(number[1]))
                number = remove(number[0], number)
                number = remove(number[0], number)
        elif len(number) == 2:
            if (number[0].isnumeric() is False) and (number[1].isnumeric() is True):  # element and number behind
                coe_list.append(int(number[1]))
                number = remove(number[0], number)
                number = remove(number[0], number)
        return number


    def find_coefficient(number):
        mylist = []
        coe_list = []
        while True:
            if number == "":
                break
            if number[0] == "(":  # check parenthesis
                number = remove(number[0], number)
                while number[0] != ')':
                    number = organize_coefficient_no_parenthesis(number, mylist)
                number = number.replace(')', "")
                multiplier = number[0]
                number = remove(number[0], number)
                for coefficient_parenthesis in mylist:
                    multiplied_number = int(coefficient_parenthesis) * int(multiplier)
                    coe_list.append(multiplied_number)
            if len(number) > 0:
                number = organize_coefficient_no_parenthesis(number, coe_list)
        # print(coe_list)
        return coe_list

    def separate_element(chosen_dict, chosen_range, balance_len):
        mole__list = []
        for x in range(0, chosen_range):
            # how_time = 0
            # molecular_formula_org = ""
            if balance_len == "product":
                how_time = x
                # molecular_formula_org = "P2O5"
            if balance_len == "reactant":
                how_time = int(x + len_product)
                # molecular_formula_org = "P4O10"
            chosen_dict[alphabet[int(how_time)]] = []  # set list for variable
            molecular_formula_org = input(f"element {int(x + 1)} : ")
            mole__list.append(molecular_formula_org)
            # molecular_formula_org = "C4H10"
            molecular_formula = molecular_formula_org
            clist = []
            complete_dict = {}
            for integer in range(0, 101):
                molecular_formula = molecular_formula.replace(str(integer), "")
            molecular_formula = molecular_formula.replace("(", "")
            molecular_formula = molecular_formula.replace(")", "")
            number_element = int(len(molecular_formula))
            number_check_mole_formula = molecular_formula_org
            alpha = 0
            while number_element > 0:
                element = lower_check(molecular_formula)
                number_check_mole_formula = number_check_mole_formula.replace(element, alphabet[alpha])
                molecular_formula = remove(element, molecular_formula)
                number_element -= int(len(element))
                clist.append(element)
                alpha += 1
            coefficient = find_coefficient(number_check_mole_formula)
            for count_ in range(0, len(clist)):
                if clist[count_] in complete_dict:
                    complete_dict[clist[count_]] += coefficient[count_]
                else:
                    complete_dict[clist[count_]] = coefficient[count_]
            chosen_dict[alphabet[how_time]].append(complete_dict)
        return mole__list

    def print_answer(product_list, reactant_list, coefficient_list):
        molecule_ = 0
        for molecule in range(0, len(product_list)):
            molecular_list[product_list[molecule]] = coefficient_list[molecule]
        molecular_list["="] = 0
        for molecule_2 in range(molecule + 1, len(reactant_list) + molecule + 1):
            molecular_list[reactant_list[molecule_]] = coefficient_list[molecule_2]
            molecule_ += 1

    def abcd():
        product_ = separate_element(product_dict, len_product, "product")
        reactant_ = separate_element(reactant_dict, len_reactant, "reactant")
        # print(product_dict)
        # print(reactant_dict)
        coefficient__ = (calculation(product_dict, reactant_dict))
        print_answer(product_, reactant_, coefficient__)
        print(molecular_list)


    len_product = int(input("Number of molecular formula (1) : "))
    len_reactant = int(input("Number of molecular formula (2) : "))
    # len_product = int(2)
    # len_reactant = int(1)
    molecular_list = {}
    product_dict = {}
    reactant_dict = {}
    # print("yes")
    abcd()


