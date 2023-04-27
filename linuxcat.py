'''
python3 heady.py 10 [archivo]
python3 tail.py 10 [archivo]
python3 wc [archivo]
'''


x = input('> ').split(" ")

if x[0] == 'head':
    lst = open(x[1], "r").readlines()

    n = 0
    while n < int(x[2]):
        print(lst[n], end='')
        n += 1

        

elif x[0] == 'tail':
    lst = open(x[1], "r").readlines()

    n = int(x[2])
    while n < len(lst):
        print(lst[n], end='')
        n += 1


elif x[0] == 'wc':
    with open(x[1], 'w', encoding='utf-8') as f:
        r = input()
        f.write(r)


else:
    print('Command not found...')