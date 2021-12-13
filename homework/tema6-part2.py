#ex1
def create_list(x, y, z, w, t):
    lista = [x, y, z, w, t]
    return lista
    # write code that creates a list with the input params of the function

print("ex1")
a = create_list(1, 2, 0, 0, 0)
print(a)

#ex2
def is_smaller_than_1_and_is_positive(a):
    return a < 1 and a >= 0
    #the function should return a bool
    # it should check the condition from the functions name

print("ex2")
print(is_smaller_than_1_and_is_positive(0.5))

#ex3
def compute_password_strength(password):
    s = {"weak": 0, "decent": 8, "good": 16, "strong": 32}
    length = len(password)
    if length < s["decent"]:
        return "weak"
    if length < s["good"]:
        return "decent"
    if length < s["strong"]:
        return "good"
    return "strong"
    # a password can be considered decent if it has at least 8 characters, so goes for the rest
    #write code that will return the strenght of the variable 'password'

print("ex3")
print(compute_password_strength("1234567891"))


#ex4
example_of_tuple = ("Horea", "Closca", "Crisan")
text = example_of_tuple[0] + ", " + example_of_tuple[1] + " & " + example_of_tuple[2] # create a sentence on this line using the 3 names from the tuple

print("ex4")
print(text)

#ex5
def is_email(email):
    arond_index = email.find("@")
    #if we don't find any @, we exit with false
    if not arond_index > 0:
        return False
    #if we find an @, we check that there is a point after it and no @
    #we do +1 so we ommit the first @
    point_index = email[arond_index+1:].find(".")
    arond_index2 = email[arond_index+1:].find("@")
    return point_index > 0 and arond_index2 == -1
    #receives a variable 'email' which is a string, checks if there is only one char '@' and after it only 1 '.'
    #returns bool

print("ex5")
print(is_email("danidandu@gmail"))
print(is_email("danidandu@gmail.com"))


if is_email("roberto.judet@itschool.ro"):
    print("Daca se printeaza asta, functia a evaluat corect")

if not is_email("roberto@judet@itschool.ro"):
    print("Daca se printeaza asta, functia a evaluat corect")

if not is_email("roberto.judet@itschool"):
    print("Daca se printeaza asta, functia a evaluat corect")

#ex6
def check_int_bigger_than_10_float_smaller_than_0_point_5(m, n):
    #first we check if one of them is int and bigger than 10
    if bigger_than_10(m) or bigger_than_10(n):
        return True
    #second we check if one is float and smaller than 0.5
    elif type(m) == float and m <= 0.5 and m >0 or type(n) == float and n <= 0.5 and n >0:
        return True
    else:
        return False
    # receives 2 params 'm' & 'n'
    # one is a float, the other int, we do not know which one
    # check the following 2 condtions: the int is bigger than 10, the float has after the point a value smaller than 0.5
    # if one condtion is True, return True from the function

print("ex6")

def bigger_than_10(a):
    return type(a) == int and a > 10

