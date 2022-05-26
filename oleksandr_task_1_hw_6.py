first_dict = {1:10, 2:20}
second_dict = {3:30, 4:40}
third_dict = {5:50, 6:60}
four_dict = {7:70, 8:80}
all_dict = {}
for full_dict in first_dict, second_dict, third_dict, four_dict:
    all_dict.update(full_dict)
print(all_dict)


first_dict = {1:10, 2:20}
second_dict = {3:30, 4:40}
third_dict = {5:50, 6:60}
four_dict = {7:70, 8:80}
all_dict = first_dict | second_dict | third_dict | four_dict
print(all_dict)




