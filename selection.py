x = 0
a_list = []
l = int(input('list length: '))
while x <= l:
    k = int(input(f'{x}: '))
    a_list.append(k)
    x += 1


def selection(a_list):
    for i in range(len(a_list)):
        min = a_list[i]
        for j in range(i+1, len(a_list)):
            if min > a_list[j]:
                min = a_list[j]
                a_list[i], a_list[j] = a_list[j], a_list[i]
    print(a_list)


selection(a_list)