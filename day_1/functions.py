# Write a function with one `number` argument that returns double the argument
def double(number: int):
    return 2 * number

# Write a function with two `number` arguments that returns double the first argument
def double_first(number1: int, number2: int):
    return number1 * 2

# Write a function with two `number` arguments that returns double the largest argument
def big_double(number1: int, number2: int):
     if number1 > number2: return number1 * 2
     else: return number2 * 2

# Write a function with a `string` argument and a `number` argument that repeates the string from the first argument but repeated the amount of times equal to the second argument. If the second number is negative, return an empty string
def repeat(text: str, number: int):
    if number < 0: return ""
    else: return text * number

# Write a function without any arguments. Have it return the string `'na'` repeated 10 times followed by the string `' batman'`. Use the `repeat` function you used before to accomplish this
def batman():
    return repeat("na", 10) + " batman"

# Write a function with two `number` arguments. Have it return the largest number of the two
def max_num(number1: int, number2: int):
    if number1 > number2: return number1
    else: return number2

# Write a function with two `number` arguments. Have it return the smallest number of the two divided by the largest number
def max_divide(number1: int, number2: int):
    return min(number1, number2) / max(number1, number2)

# Write a function with two `string` arguments. Have it return the longest string
def max_string(string1: str, string2: str):
    if len(string1) >= len(string2) : return string1
    else: return string2

# Write a function with a single `number` argument. Return a boolean that indicated wether this number is even
def even(number: int):
    return number % 2 == 0

# Write a function with a single `number` argument. Return a list of all the positive numbers lower than this argument that are even
def even_below(number: int):
    l = []
    for n in range(number):
        if n % 2 == 0 and n >= 0: l.append(n)
    return l

# Write a function with a single `list of numbers` argument. Return a list of all the numbers in this list that are even
def even_in(numbers: 'list[int]'):
    l = []
    for n in numbers:
        if n % 2 == 0: l.append(n)
    return l

# Write a function with a single `list of numbers` argument. Return the result of multiplying all the numbers. If the input contains just 1 number, return that number
def multiply_list(numbers: 'list[int]'):
    m = 1
    for n in numbers:
        m *= n
    return m

# Write a function with a single `list of numbers` argument. Return the result of dividing the number from left to right. So the first number gets divided by the second and the result of that gets divided by the third (and so on..). If the list contains a zero, return zero. If the list contains just one number, return that number
def divide_array(numbers: 'list[int]'):
    if numbers.count(0): return 0
    elif len(numbers) == 1: return numbers[0]
    else:
        m = numbers[0]
        for n in numbers[1:]:
            m/=n
    return m    

# Write a functions that takes a list of numbers and an argument. Return the average of those numbers
def average(numbers: 'list[int]'):
    return sum(numbers) / len(numbers)