def alphabeticalSort(list):
    list.sort()

def alpha_test():
    testList = ["car", 'bike', 'aeroplane']
    alphabeticalSort(testList)
    print(testList)

def sigmabeticalSort(list):
    import random
    random.shuffle(list)

def sigma_test():
    testList = ['first', 'second', 'third', 'fourth','fifth']
    sigmabeticalSort(testList)
    print(testList)

alpha_test()
sigma_test()