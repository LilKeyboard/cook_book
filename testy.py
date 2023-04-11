# from os.path import join
#
# listaa = ['how to make a coffee.txt', 'how to make a tea.txt']
#
# nowa_listaa = list(map(lambda x: x.split()[-1].split('.')[0], listaa))
#
# #print(nowa_listaa)
#
# word = 'how to make a coffee.txt'
# #print(word.split()[-1].split('.')[0])
#
# recipe_name = 'tea'
# list_static = ['how to make a coffee.txt', 'how to make a tea.txt']
# #list_transformed = list(list(map(lambda x: x.split()[-1].split('.')[0], list_static)))
#
# static_address = 'static/receipts/'
#
# recipe_name_address = ''
#
# for el in list_static:
#     if recipe_name in el:
#         recipe_name_address = el
#         break
#
# finall_address = join(static_address, recipe_name_address)
#
# with open(finall_address, 'r') as file:
#     content = file.readlines()
#     print(content[2])

# with open('static/comments/comments.txt', 'r') as file:
#     content = file.read().splitlines()
#     print(content)
#
#     html_list = '<ul>'
#     html_list_end = '</ul>'
#
#     for line in content:
#         html_list += f'<li>{line}</li>'
#
#     html_list = html_list + html_list_end
#
#     print(type(html_list))

# import os
# #os.stat('static/comments/comments.txt').st_size == 0
#
# print(os.stat('static/comments/comments.txt').st_size)

test_string1 = '< wiktor >'
test_string2 = '< >'
test_string3 = ' wi<ktor '

new_word = ''

for item in test_string3:
    if item == '<':
        item = '&lt'

    if item == '>':
        item = '&gt'

    new_word += item

print(new_word)
