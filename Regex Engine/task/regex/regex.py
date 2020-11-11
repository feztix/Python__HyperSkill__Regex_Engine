# write your code here
def splitting_input(string=str(input()).split("|")):
    return string[0], string[1]


def regEx_engine(tupple_of_splitted_string):
    regex_expr = tupple_of_splitted_string[0]
    input_value = tupple_of_splitted_string[1]

    return comparing_expr(regex_expr, input_value)

def comparing_expr(regex_expr, input_value):
    if regex_expr == input_value:
        return True
    elif len(regex_expr) == 0:
        return True
    elif regex_expr == ".":
        return True
    elif len(regex_expr) != 0 and len(input_value) == 0:
        return False
    # different patterns
    else:
        return False


print(regEx_engine(splitting_input()))