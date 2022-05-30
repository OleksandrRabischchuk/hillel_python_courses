
def my_function():
    new_string = [1, 2, 3]
    new_string_2 = [11, 22, 33]
    new_string_3 = []
    i = 0
    while i != len(new_string) or i != len(new_string_2):
        new_string_3.append(new_string[i])
        new_string_3.append(new_string_2[i])
        i += 1
    return new_string_3
print(my_function())

    