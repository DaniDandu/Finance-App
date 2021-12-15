# Some of these exercises can be solved using some built-in functions of python.
# The scope is not to use them, to use and exercise `for` and `if`.

# homework with lists and for
# ex 1
def say_hello_to_all(list_of_names):
    for name in list_of_names:
        print("hello " + name)
    # write a for to say(print) hello to all names

print("ex1")
names = ["Bob", "Jane", "Bill", "George", "Ryan"]
say_hello_to_all(names)


# ex 2
def print_only_odd_numbers(list_of_numbers):
    for nr in list_of_numbers:
        if nr % 2 !=0:
            print(nr)
    # print only the odd numbers from the list (numerele impare)


print("ex2")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_only_odd_numbers(numbers)


# ex 3
def return_even_numbers(list_of_numbers):
    list = []
    for number in numbers:
        if number % 2 == 0:
            list.append(number)
    return list
    # return a new list with only the even numbers
    # example of code to add element to the end of a list
    #   lista.append(4)


print("ex3")
even_numbers = return_even_numbers(numbers)
print(even_numbers)



# ex 4 - difficult

def return_an_ordered_list(list_of_numbers):
    index1 = 0
    index2 = 0
    for el1 in list_of_numbers:
        for el2 in list_of_numbers:
            if index1 < index2 and numbers[index1] > numbers[index2]:
                aux = numbers[index2] #we save one of the numbers in a variable
                numbers[index2] = numbers[index1]
                numbers[index1] = aux #aux is the initial value of numbers[index2]
            index2 = index2 + 1
        index1 = index1 + 1
        index2 = 0
    return numbers

    # write code that returns a list of ordered numbers (0, 1, 2, 3, ...)


print("ex4")
numbers = [0, -4, 56, 7.0, 89, 203.45, 0.45, -0.3, 5, 8]
ordered_numbers = return_an_ordered_list(numbers)
if ordered_numbers == [-4, -0.3, 0, 0.45, 5, 7.0, 8, 56, 89, 203.45]:
    print("function is good")
else:
    print("function is not good")
# a little hint, you need to keep track of the index on which you are on


# ex 5
def count_list(lista):
    length = 0
    for element in lista:
        length = length + 1
    return length
#create a function which returns the number of elements in a list


print("ex5")
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(count_list(x))

# ex 6
def multiply(lista):
    result = 1
    for element in lista:
        if type(element) == int or type(element) == float:
            result = result * element
    return result
# create a function which multiplies all the numbers in the list

print("ex6")
list_to_try = ["hello", 2, 1, -4, "alt string", True]
print(multiply(list_to_try))

# ex 7 - difficult
list_with_duplicates = [1, 1, 2, 3, 3, 2, 5, 6, 7, "a", 5, 2]
list_without = [1, 2, 3, 5, 6, 7, "a"]
def is_in_list(element, lista):
    for el in lista:
        if el == element:
            return True # when we find the element, we exit and return True
    return False # means we didn't find the element

def remove_duplicates(lista):
    new_list = []
    for el in lista:
        if is_in_list(el, new_list):
            pass
        else:
            new_list.append(el)
    return new_list

print("ex7")
if remove_duplicates(list_with_duplicates) == list_without:
    print("we removed the duplicates")
else:
    print("we didn't remove")
# create a function which removes duplicate items from a list


# ex 8
def create_text(lista):
    sentence = ""
    for element in lista:
        if type(element) == str:
            sentence = sentence + element + " "
    return sentence
# create a function which creates a text with all the strings from the list

print("ex8")
lista8 = ["hey", 1, False, "there", "do", 0, "you", -0.9, "know", "the", "clock", 77, 88.9]
print(create_text(lista8))

# ex 9 - intermediary difficulty
def min_and_max(lista):
    min = lista[0]
    max = lista[0]
    for el in lista:
        if min > el:
            min = el
        if max < el:
            max = el
    return (min, max)
# create a function which returns the maximum and minimum number from a list

print("ex9")
print(min_and_max(numbers))
