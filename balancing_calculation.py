import numpy as np
# #
# product_dict = {'a': [{'Na': 1}], 'b': [{'H': 2, 'O': 1}]}
# reactant_dict = {'c': [{'Na': 1, 'O': 1, 'H': 1}], 'd': [{'H': 2}]}


def calculation(product_dict, reactant_dict):
    print(product_dict)
    print(reactant_dict)
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_equation = []
    equation_list_0 = []
    a_list = []
    total_equation_list = []

    for alphabet in product_dict:
        alphabet_equation.append(alphabet)
    for alphabet in reactant_dict:
        alphabet_equation.append(alphabet)
    alist_range = len(alphabet_equation) - 1
    def create_equation(equation_list):
        equation = equation_list[0]
        equation_pos = equation_list.index(equation)
        equation_list.pop(equation_pos)
        # print(equation)
        for coefficient_element_list in equation:  # set a as 1
            for coefficient_element in coefficient_element_list:
                if len(coefficient_element) == 2:
                    if coefficient_element[1] == 'a':
                        pos_coefficient = coefficient_element_list.index(coefficient_element)
                        coefficient_element_list.remove(coefficient_element)
                        replaced_a = int(coefficient_element[0]) * 1
                        coefficient_element_list.insert(pos_coefficient, str(replaced_a))
        product_coe_list = equation[2]
        reactant_coe_list = equation[0]
        for abc_reactant in reactant_coe_list:
            if len(abc_reactant) == 1:
                if abc_reactant.isnumeric() == True:
                    alphabet_pos_reactant = reactant_coe_list.index(abc_reactant)
                    reactant_coe_list.pop(alphabet_pos_reactant)
                    reactant_negative = "-" + str(abc_reactant)
                    product_coe_list.append(reactant_negative)
        # print(equation)
        for abc_coe in product_coe_list:
            for alpha in alphabet_list:
                if len(abc_coe) == 2:
                    if abc_coe[1] == str(alpha):
                        alphabet_pos = product_coe_list.index(abc_coe)
                        product_coe_list.pop(alphabet_pos)
                        reactant_negative = "-" + str(abc_coe)
                        reactant_coe_list.append(reactant_negative)
                elif len(abc_coe) == 3:
                    if abc_coe[2] == str(alpha):
                        alphabet_pos = product_coe_list.index(abc_coe)
                        product_coe_list.pop(alphabet_pos)
                        reactant_negative = "-" + str(abc_coe)
                        reactant_coe_list.append(reactant_negative)
                elif len(abc_coe) == 4:
                    if abc_coe[3] == str(alpha):
                        alphabet_pos = product_coe_list.index(abc_coe)
                        product_coe_list.pop(alphabet_pos)
                        reactant_negative = "-" + str(abc_coe)
                        reactant_coe_list.append(reactant_negative)
                if len(product_coe_list) == 0:
                    product_coe_list.append("0")
        # print(equation)
        equation_list.append(equation)

    def dict_to_mathequation():
        duplicated_list = []
        alphabet_list = []
        math_dict_product = {}
        math_dict_reactant = {}
        line = []
        # print(product_dict)
        # print(reactant_dict)
        for alphabet in product_dict:
            duplicated_list += product_dict[alphabet][0]
            alphabet_list.append(alphabet)
        for alphabet in reactant_dict:
            duplicated_list += reactant_dict[alphabet][0]
            alphabet_list.append(alphabet)
        # print(duplicated_list)
        all_list = set(duplicated_list)
        for all_element in all_list:
            math_dict_product[all_element] = []
        for all_element in all_list:
            math_dict_reactant[all_element] = []
        for alphabet in product_dict:
            for all_element in all_list:
                if all_element in product_dict[alphabet][0]:
                    math_dict_product[all_element].append(str(product_dict[alphabet][0][all_element]) + alphabet)
        for alphabet in reactant_dict:
            for all_element in all_list:
                if all_element in reactant_dict[alphabet][0]:
                    math_dict_reactant[all_element].append(str(reactant_dict[alphabet][0][all_element]) + alphabet)
        for all_element in all_list:
            alphabet_math_product = []
            alphabet_math_reactant = []
            for alphabet_coefficient in range(0, len(math_dict_product[all_element])):
                if alphabet_coefficient > 0:
                    alphabet_math_product.append(str(math_dict_product[all_element][alphabet_coefficient]))
                else:
                    alphabet_math_product.append(str(math_dict_product[all_element][alphabet_coefficient]))

            for alphabet_coefficient in range(0, len(math_dict_reactant[all_element])):
                if alphabet_coefficient > 0:
                    alphabet_math_reactant.append(str(math_dict_reactant[all_element][alphabet_coefficient]))
                else:
                    alphabet_math_reactant.append(str(math_dict_reactant[all_element][alphabet_coefficient]))
            equation = []
            equation.append(alphabet_math_product)
            equation.append("=")
            equation.append(alphabet_math_reactant)
            line.append(equation)
        for x in range(0, len(line) * 2):
            create_equation(line)
        for element_equation in line:
            equation_reactant = element_equation[0]
            equation_list_0.append(equation_reactant)
        for element_equation in line:
            total_equation = element_equation[2][0]
            total_equation_list.append(int(total_equation))
        # print(equation_list_0)
    # -----------------------------------------------------------------------------------------

    # -----------------------------------------------------------------------------------------
        for element_mole_list in equation_list_0:  # fill in the gap
            alphabet_equation_cpy = alphabet_equation.copy()
            for element_mole in element_mole_list:
                for alpha_ in alphabet_equation_cpy:
                    if len(element_mole) == 2 and element_mole[1] == alpha_:
                        alphabet_equation_cpy.remove(alpha_)
                    elif len(element_mole) == 3 and element_mole[2] == alpha_:
                        alphabet_equation_cpy.remove(alpha_)
                    elif len(element_mole) == 4 and element_mole[3] == alpha_:
                        alphabet_equation_cpy.remove(alpha_)
                    elif len(element_mole) == 5 and element_mole[4] == alpha_:
                        alphabet_equation_cpy.remove(alpha_)
            for alphabet_coe in alphabet_equation_cpy:
                pos_element = alphabet_equation.index(alphabet_coe)
                element_mole_list.insert(pos_element, "0" + alphabet_coe)

    # -----------------------------------------------------------------------------------

        equation_editable = equation_list_0.copy()

        for element_mole_list_ in range(0, len(equation_editable)):
            element_mole_list_cpy = equation_editable[element_mole_list_]
            for element_moles in range(0, len(element_mole_list_cpy)):
                element_mole_cpy = element_mole_list_cpy[element_moles]
                for alpha_ in alphabet_equation:
                    # print(element_mole_cpy)
                    # print(equation_list_0[element_mole_list_])
                    if len(element_mole_cpy) == 2 and element_mole_cpy[1] == alpha_:
                        pos_alpha = alphabet_equation.index(element_mole_cpy[1])
                        equation_list_0[element_mole_list_].remove(element_mole_cpy)
                        equation_list_0[element_mole_list_].insert(pos_alpha, element_mole_cpy)
                    elif len(element_mole_cpy) == 3 and element_mole_cpy[2] == alpha_:
                        pos_alpha = alphabet_equation.index(element_mole_cpy[2])
                        equation_list_0[element_mole_list_].remove(element_mole_cpy)
                        equation_list_0[element_mole_list_].insert(pos_alpha, element_mole_cpy)
                    elif len(element_mole_cpy) == 5 and element_mole_cpy[4] == alpha_:
                        pos_alpha = alphabet_equation.index(element_mole_cpy[4])
                        equation_list_0[element_mole_list_].remove(element_mole_cpy)
                        equation_list_0[element_mole_list_].insert(pos_alpha, element_mole_cpy)
                    elif len(element_mole_cpy) == 6 and element_mole_cpy[5] == alpha_:
                        pos_alpha = alphabet_equation.index(element_mole_cpy[5])
                        equation_list_0[element_mole_list_].remove(element_mole_cpy)
                        equation_list_0[element_mole_list_].insert(pos_alpha, element_mole_cpy)
        # print(equation_list_0)
    # -----------------------------------------------------------------------------------
        for element_mole_list in equation_list_0:  # set all as integer
            for element_mole in range(0, len(element_mole_list)):
                # print(element_mole_list)
                # print(element_mole_list[element_mole])
                if len(element_mole_list[element_mole]) == 2:
                    element_mole_ = element_mole_list[element_mole]
                    removed_element = element_mole_[0]
                    pos_element = element_mole_.index(element_mole_list[element_mole])
                    element_mole_list.pop(element_mole_list.index(element_mole_list[element_mole]))
                    element_mole_list.insert(pos_element, int(removed_element))
                elif len(element_mole_list[element_mole]) == 3:
                    element_mole_ = element_mole_list[element_mole]
                    removed_element = element_mole_[0] + element_mole_[1]
                    pos_element = element_mole_.index(element_mole_list[element_mole])
                    element_mole_list.pop(element_mole_list.index(element_mole_list[element_mole]))
                    element_mole_list.insert(pos_element, int(removed_element))
                elif len(element_mole_list[element_mole]) == 4:
                    element_mole_ = element_mole_list[element_mole]
                    removed_element = element_mole_[0] + element_mole_[1] + element_mole_[2]
                    pos_element = element_mole_.index(element_mole_list[element_mole])
                    element_mole_list.pop(element_mole_list.index(element_mole_list[element_mole]))
                    element_mole_list.insert(pos_element, int(removed_element))
            element_mole_list.reverse()

        a_list.append(1)
        for x in range(0, alist_range):
            a_list.append(0)
        equation_list_0.insert(0, a_list)
        total_equation_list.insert(0, 1)
        print(equation_list_0)
        print(total_equation_list)
        A = np.array(equation_list_0)
        b = np.array(total_equation_list)
        answer = np.linalg.solve(A, b).tolist()
        return answer
    return dict_to_mathequation()


# print(calculation(product_dict, reactant_dict))
