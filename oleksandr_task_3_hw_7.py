a, b, c, d = 4, 4, 4, 4
def my_function(a):
    perimetr = a + b + c + d
    ploshad = a**2
    diagonal = a*2**(1/2)
    return perimetr, ploshad, diagonal

print(my_function(a))