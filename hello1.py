# funct to return index & letter mapping
def cnt (i_min:int=1, i_max:int=5, pace:int=1)->dict:
    store = {}
    for i in range(i_min,i_max,pace):
        print (f"item {i}, letter:{chr(96+i)}")
        store[i] = chr(96 +i)
    #return dictionary with the current item and corresponding letter
    return store

diction = cnt(1, 6, 1)
print(diction.items())
