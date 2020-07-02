"""16. Write a Python program to print all permutations of a given string (including duplicates). """



def perm(var):
    k = 0


    while k < len(var):

        string = var[0: k]
        print(string)
        i = 0
        list_strings = []
        # ...
        final_list = []

        while i < len(string):

            first_string = string[0: i] + string[i + 1: len(string)]
            print(f"Thins is the 1st string: {first_string}")


            for j in range(0, len(string)):

                second_string = first_string[0: j] + string[i] + first_string[j: len(string)]
                print(f"Thins is the 2nd string: {second_string}")

                if second_string not in list_strings:

                    list_strings.append(second_string)

                for x in list_strings:

                    if len(x) == i + 1:

                        final_list.append(x)

                print(list_strings)

            i += 1


        k += 1

    print(final_list)

perm('ABC')

'''k = 0
while k < len(var):
    final_list = []
    string = var[0 : k]
    # Do ...
    # Initiate variables
    print(string)
    i = 0
    list_strings = []

    # ...
    while i < len(string):
        first_string = string[0: i] + string[i + 1: len(string)]
        print(f"Thins is the 1st string: {first_string}")
        for j in range(0, len(string)):
            second_string = first_string[0: j] + string[i] + first_string[j: len(string)]
            print(f"Thins is the 2nd string: {second_string}")
            if second_string not in list_strings:
                list_strings.append(second_string)
            print(list_strings)
        i += 1
    print(list_strings)
'''



'''
def permute_string(str):
    if len(str) == 0:
        return ['']

    prev_list = permute_string(str[1:len(str)])

    print(prev_list)

    next_list = []

    print(f"This is the parent next list: {next_list}")
    
    for i in range(0,len(prev_list)):
        for j in range(0,len(str)):
            new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]

            print(new_str)

            if new_str not in next_list:
                next_list.append(new_str)

    # print(next_list)
    return next_list


print(permute_string('ABCD'));
'''
