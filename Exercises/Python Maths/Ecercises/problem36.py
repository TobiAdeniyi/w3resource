# def disemvowel(word):
#     w = list(word)
#     vowel = ['a', 'e', 'i', 'o', 'u']
#     for i in vowel:
#         if i in w:
#             w.remove(i)
#         elif i.upper() in w:
#             w.remove(i.upper())
#
#     w = ''.join(w)
#     return w

# print(disemvowel('QWERTTYUIOP'))

# print(list('qweRTYUI'))

messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]
messy_list.insert(0, messy_list.pop(3))
new_list = []

print(messy_list, "\n")

for i in messy_list:
    if type(i) is not int:
        print(f"{i} has type: {type(i)} which is not an integer! ")
        new_list.append(i)
        # messy_list.remove(i)

    else:
        print(f"{i} has type {type(i)}")

# for i in messy_list:
#     print(i, "has type:", type(i))

for i in new_list:
    messy_list.remove(i)
print(f"\nmessy_listt = {messy_list}")
# Your code goes below here


