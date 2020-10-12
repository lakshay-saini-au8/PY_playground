from collections import OrderedDict
price_count = OrderedDict()

n = int(input())
for _ in range(n):
    field = input().split()
    item_name = " ".join(field[0:len(field)-1])
    net_price = field[-1]
    newdict = dict(price_count)
    if item_name in newdict.keys():
        price_count[item_name] += int(net_price)
    else:
        price_count[item_name] = int(net_price)

new_dict = dict(price_count)
for i in new_dict.items():
    print(i[0]+" "+str(i[1]))
