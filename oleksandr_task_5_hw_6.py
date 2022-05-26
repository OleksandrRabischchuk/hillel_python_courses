data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
my_dict = {}
for item in data:
    for dictItemValue in item.values():
        if my_dict.get(dictItemValue) is None:
            my_dict[dictItemValue] = None

print(my_dict)


