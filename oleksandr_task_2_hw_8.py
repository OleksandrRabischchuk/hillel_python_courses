def two_arguments(one, two):
    if one > two:
        return one
    else:
        return two


def three_arg(one,two,three):
    middle = two_arguments(one, two)
    if middle > three:
        return middle
    else:
        return three


