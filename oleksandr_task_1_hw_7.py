#first_example = [0 for numbers in range(7)]
#print(first_example)

#second_example = ['sasha' for my_string in range(2)]
#print(second_example)

#three_example = [my_string for my_string in 'sasha']
#print(three_example)

#four_example = [i**2 for i in range(7)]
#print(four_example)

#import random
#five_example = [random.randint(-10,10) for numbers in range(9)]
#print(five_example)

#phone = ['959015337', '959025676']
#six_example = ['+380' + phone for phone in phone]
#print(six_example)


  # five example with set_comprehension

#first_example ={numbers for numbers in range(2,7)}
#print(first_example)

#second_example = {numbers**3 for numbers in range(1,4)}
#print(second_example)

#import random
#three_example ={random.randint(-10,10) for numbers in range(10) }
#print(three_example)

#four_example = {numbers for numbers in [2, 2, 3, 5, 5]}
#print(four_example)

#five_example = {my_string for my_string in ['hello', 'hi', 'hello', 'hi', 'qwerty']}
#print(five_example)

  # five example with dictionary


#first_example = {my_key:my_key**2 for my_key in range(1,11)}
#print(first_example)

#second_example = {word:len(word) for word in ['sasha', 'pasha', 'www']}
#print(second_example)

#three_example = {'Илон МаСк': 123,'БРед ПиТ': 145,'УИл СМит': 120}
#new_data = {key.title() for key in three_example.keys()}
#print(new_data)

'''four_example = {'Илон МаСк': '123',
                'БРед ПиТ': '145',
                'УИл СМит': '120'}
new_data = {key.title(): int(value) for key, value in four_example.items() }
print(new_data)'''

five_example =[
                [0, 'Misha', 'password'],
                [51, 'Slavik', '12345']
]
new_users = {user[0]: user for user in five_example}
print(new_users[51])



