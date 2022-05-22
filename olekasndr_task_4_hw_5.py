new_object = dir(set)
new_object_2 = []
for item in new_object:
    if item.startswith('__'):
        continue
    else:
        new_object_2.append(item)
print(new_object_2)