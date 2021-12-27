# how to cycle through a dictionary

d = {"a": 1, "b": 2, "c": 4, "d": 8}
for key, value in d.items():  # items function returns a list of tuples (<key>, <value>)
    print(key, value)

# print the keys until a value is bigger than 3
for key, value in d.items():
    if value < 3:
        print(key)
    else:
        break


def maximum(lista):
    max = lista[0]
    for x in lista:
        if type(x) == str or type(x) == bool:
            continue
        if max < x:
            max = x
    return max


print(maximum([1, "a", "b", True, 2, 0]))


# split applied on a string return a list
# reverse is join
strings = ["Are", "you", "sure", "?"]
sentence = " ".join(strings)
print(sentence)

