from random import randint

def convert(lst):
    return [str(i) for i in lst]

print(convert([1, 2, 3]))

def capital_indexes(string):
    return [i for i in range(len(string)) if string[i].isupper()]
        
print(capital_indexes("HeLlO"))

def mid(string):
    if (len(string) % 2) == 0:
        return ""
    else:
        return string[ (len(string) // 2) ]
        
print(mid("Hello"))

def online_count(dictionary):
    return len([key for key in dictionary if dictionary[key] == "online"])
    
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

print(online_count(statuses))

def random_number():
    return randint(1, 100)
    
print(random_number())

def only_ints(a, b):
    return type(a) == int and type(b) == int
        
print(only_ints(1, False))

def double_letters(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True
        else:
            continue
    
    return False
    
print(double_letters("string"))

def add_dots(string):
    return ".".join(string)

def remove_dots(string):
    return string.replace(".", "")

print(remove_dots(add_dots("Hello")))

def count(string):
    return len(string.split("-"))

print(count("ter-min-a-tor"))

def build_anagram_dict(string):
    return {l: string.count(l) for l in string}

def is_anagram(a, b):
    return build_anagram_dict(a) == build_anagram_dict(b)

print(is_anagram("typhoon", "opython"))

def flatten(lstoflst):
    return [i for lst in lstoflst for i in lst]
    
flatten([[1, 2], [3, 4]])

def largest_difference(lstofnums):
    return max(lstofnums) - min(lstofnums)
    
largest_difference([1, 2, 3])

def format_number(num):
    newstring = ""
    count = len(str(num)) - 1
    
    while (count >= 0):
        newstring = str(num)[count] + newstring
        if ((len(str(num)) - count) % 3 ) == 0 and count != 0:
            newstring = "," + newstring
        count = count - 1

    return newstring
    
print(format_number(1000000))