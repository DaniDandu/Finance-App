def is_divisible(number, divisor):
    a = number/ divisor
    if type(a) == int:
        return True
    else:
        return False
    # check that the variable `number` is divisible by `divisor`
    # return True or False
print("1:")
print(is_divisible(6, 3))

def get_number(x):
    if x % 2 != 0:
        x = x * 3
        return x
    else:
        x = x / 2
        return x
# create a function which receives a number
# if the number is odd (impar) multiply by 3, if not divide it by 2
print("2:")
print(get_number(5))

# What values should x,y have so the following if statements are True? What about False?
print("3:")
x = 8
# x = 5 pentru fals
a = x > 6 and x < 12
print(a)

print("4:")
x = 11
y = 9
# x = 9, y = 9 pentru fals
b = x > 10 or y > 10
print(b)

print("5:")
x = 8
# indiferent de numar, nu poate si fals
c = x < 9 or True
print(c)

print("6:")
y = 100
# nu poate fi adevarat
d = y > 99 and False
print(d)

print("7:")
x = 10
# nu poate fi adevarat
e = x > 10 and x < 10
print(e)

print("8:")
x = 5
# nu poate fi adevarat
f = not x
print(f)

print("9:")
x = 14
y = 90
# x = 10
# y = 80
h = x > 12 and x < 18 or y > 4 and not y < 89
print(h)
