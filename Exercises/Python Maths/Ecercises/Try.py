def word_count(string):
    # Create list element containing words in string
    lst = string.lower().split()
    # Create new class of words in list
    st = set(lst)
    # Create an empty dictionary
    dic = {}
    # Check count of each word in class
    for i in st:
        # Assign counts to each word in class under a new dictionary
        dic[i] = lst.count(i)

    print(dic)
#
# word_count("I do not like it Sam I Am")
# word_count("QWEFG")
# word_count("I  do  not  like  it  Sam  I  Am")
# word_count("")

# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# {'i': 2, 'not': 1, 'am': 1, 'do': 1, 'sam': 1, 'like': 1, 'it': 1}
# Lowercase the string to make it easier.

d = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections'], 'Daniel J': ['Python somthing', 'Java basics', 'HTML foundation']}

def courses(dic):
    new_list = []
    for value in dic.values():
        new_list.extend(value)

    print(new_list)


# def most_courses(dic):
#     dic.key(max(dic.value()) in dic.values())
#     print(max([len(dic[k]) for k in dic]))
#
#
# most_courses(d)
#
#
# inverse = [(len(value), key) for key, value in d.items()]
# print(max(inverse)[1])
# print(d)

#
# def stringcases(string):
#     upper_c = string.upper()
#     lower_c = string.lower()
#     title_c = string.title()
#     reverse_c = ''.join(list(string)[::-1])
#     return upper_c, lower_c, title_c, reverse_c
#
# print(stringcases("abcd"))

#
# def combo(arg1, arg2):
#     list1 = [item for index, item in enumerate(arg1)]
#     list2 = [item for index, item in enumerate(arg2)]
#     list3 = []
#     for i in range(len(list1)):
#         list3.append((list1[i], list2[i]))
#     return list3
#
# print(combo([1, 2, 3], 'abc'))

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

"""
def covers(st):
    results = []
    for key, value in COURSES.items():
        if value & st:
            results.append(key)
    return results
"""
"""
def covers(st):
    return [key for key, value in COURSES.items() if st & value]

def covers_all(st):
    return [key for key, value in COURSES.items() if not st - value]

print(covers({"Python"}))
"""
"""
moves = ["LEFT", "RIGHT", "UP", "DOWN"]

if True:
    moves.remove("LEFT")

print(moves)

TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)
for i in TILES:
    if i == '||':
        print('\n')
    else:
        print(i, end="")
"""

a = '12345'

print(a[::-1])
