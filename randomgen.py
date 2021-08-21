import random
from matplotlib import pyplot as plt

# combine all the lists i generate into one big stupid list, in case needed
def combine_lists(*args) :
    this_list = []
    for arg in args:
        for i in arg:
            this_list.append(i)
    print(this_list)

# N = size of randomly generated array, custom_list is an optional argument that allows you to feed your own list in
def main(n, custom_list=[]):

    # create a random list
    def gen_list(n):
        rand_list = []
        for _ in range(n):
            rand_list.append(int(random.random()*100))
        return rand_list

    # create a set off of a list that gets passed
    def gen_set(ls):
        this_set = set(ls)
        return this_set

    # generate an object based off the set and lists
    def gen_dict(set):
        this_dict = {}
        for i in set:
            this_dict[i] = 0
        return this_dict

    # populate a dictionary with the appropriate frequency of values
    def populate_dict(dict, ls):
        for i in ls:
            dict[i]+=1
        return dict

    this_list = gen_list(n) if not custom_list else custom_list
    this_dict = populate_dict(gen_dict(gen_set(this_list)), this_list)

    print(this_dict)

    plt.bar(this_dict.keys(), this_dict.values())
    plt.xlabel('Number')
    plt.ylabel('frequency')
    plt.show()