x = 0
a_list = []
l = int(input('list length: '))
while x <= l:
    k = int(input(f'{x}: '))
    a_list.append(k)
    x += 1


def bubbleSort(a_list):
    for i in range(len(a_list)):
        for j in range(i + 1, len(a_list)):
            if a_list[i] > a_list[j]:
                a_list[i], a_list[j] = a_list[j], a_list[i]
    print(a_list)


bubbleSort(a_list)
