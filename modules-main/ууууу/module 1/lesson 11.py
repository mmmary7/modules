from datetime import datetime
def repair_deco(func):
    def wrapper(a, b):
        return func(a, b)-1
    return wrapper


@repair_deco
def wrong_func(a,b):
    return a+b+1


def timeit(funk):
    def wrapper(val):
        start = datetime.now()
        res = funk(val)
        end = datetime.now()
        print(f"time: {end - start}")
        return res
    return wrapper


#print(wrong_func(2,2))
@timeit
def get_list_1(val):
    return [x for x in range(val)]


@timeit
def get_list_2(val):
    new_list=[]
    for x in range(val):
        if x%2:
            new_list.append(x)
    return new_list


val = 1000000
a = get_list_1(val)
b = get_list_2(val)
