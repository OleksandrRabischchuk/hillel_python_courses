my_dict = {'id1':

{

'name': 'Ruslan',

'class': 1,

'subjects' : {'Math', 'Algorithms', 'English'}

},

'id2':

{

'name': 'Mark',

'class': 2,

'subjects' : {'Geometry', 'Java', 'Cooking'}

},

'id3':

{

'name': 'Ruslan',

'class': 1,

'subjects' : {'Math', 'Algorithms', 'English'}

}

}
result = {}
for key, value in my_dict.items():
    if value not in result.values():
        result[key] = value

print(result)

