# write your code here
def splitting_input(string=str(input()).split("|")):
    return string[0], string[1]


def regEx_engine(tupple_of_splitted_string):
    regex_expr = tupple_of_splitted_string[0]
    input_value = tupple_of_splitted_string[1]

    return regular_express(regex_expr, input_value)


# character-by-character comparison
def comparison_ch_by_ch(regex_expr_ch, input_value_ch):
    if len(regex_expr_ch) == 0:
        return True
    if regex_expr_ch == '.':
        return True
    if regex_expr_ch == input_value_ch:
        return True
    return False


def comparing_expr(regex_expr, input_value):
    if len(regex_expr) == 0:
        return True
    if len(input_value) == 0:
        return False
    # character-by-character comparison
    if comparison_ch_by_ch(regex_expr[0], input_value[0]) is False:
        return False
    return comparing_expr(regex_expr[1:], input_value[1:])


def regular_express(regex_expr, input_value):
    if regex_expr == '':
        return True
    for i in range(len(input_value)):
        if comparing_expr(regex_expr, input_value[i:]) is True:
            return True
    return False


if __name__ == "__main__":
    print(regEx_engine(splitting_input()))
