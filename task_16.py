def make_plosk(lis):
    i =0
    while i < len(lis):
        if type(lis[i]) == list:
            make_plosk(lis[i])
            lis[i:i+1] = lis[i]
        else :
            i += 1


list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
make_plosk(list_a)
print(list_a)