import random

# bytes = random.randbytes(77)
# print(bytes)
#
# from_range = random.randrange(90, 100000, 78)
# print(from_range)
#
# c = random.choice(['piatra', 'foarfece', 'hartie'])
# print(c)


# d = {'piatra': 0, 'foarfece': 0, 'hartie': 0 }
# for i in range(0, 10000):
#     c = random.choice(['piatra', 'foarfece', 'hartie'])
#     d[c] += 1
#     print(i)
#     f = lambda d, c, i: print(c, d[c] / i * 100)
#     f(d, 'piatra', i)
#     f(d, 'foarfece', i)
#     f(d, 'hartie', i)


shuf = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(shuf)
print(shuf)
