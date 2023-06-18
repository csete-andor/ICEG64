import time
import random as rr

translation_dict={'a': '$W57', 'b': '~F80', 'c': '&P91', 'd': '&R32', 'e': ':Á50', 'f': '%B27', 'g': '@H21', 'h': '*L49', 'i': '^É64', 'j': '*V89', 'k': '/I52', 'l': '?A42', 'm': '$Ű56', 'n': ':N47', 'o': '!S69', 'p': '|Q18', 'q': '$J70', 'r': '!Í74', 's': '@M85', 't': '^Ó92', 'u': '/E21', 'v': '>T62', 'w': '<X88', 'x': '%D92', 'y': '&Ü08', 'z': '!Y17', 'á': '#Ő96', 'é': '\\K13', 'í': ';G55', 'ó': '#Ö02', 'ö': '|Ú27', 'ő': '%Z75', 'ú': '>C27', 'ü': '~O23', 'ű': ';U68', 'A': '$f44', 'B': '!n94', 'C': '\\é82', 'D': '#í34', 'E': '!u46', 'F': '<e83', 'G': '~t92', 'H': '*z13', 'I': '@w56', 'J': '#g67', 'K': '^m12', 'L': ';q10', 'M': ':j12', 'N': '%d84', 'O': '#r90', 'P': '@i53', 'Q': '<ö89', 'R': '/l87', 'S': '!ű92', 'T': '^s69', 'U': ';h60', 'V': '\\k27', 'W': '&p88', 'X': '&y59', 'Y': ':ó52', 'Z': '%b33', 'Á': '%o12', 'É': '?ő49', 'Í': '~á13', 'Ó': '$v88', 'Ö': '$ú95', 'Ő': '>a03', 'Ú': '&x59', 'Ü': '|ü66', 'Ű': '|c09', '0': '@2Ol', '1': '$3Ví', '4': '$6Pű', '5': '\\8Kh', '7': '/5Gv', '!': '#9dŐ', '@': '/4fA', '%': '<9üY', '&': '*1qM', '<': '|2yU', '?': '!5zC', '/': '?0oH', '\\': '^9bE', ':': '$8őJ', '$': '*5mS', '>': '@4úP', '~': ':6vX', '#': '%2kÓ'}

def create_key():
    #create some random characters (for both sides, generated sometimes)
    var = randomNum()+randomNum()
    var = var+rr.randint(rr.randint(0, 20), rr.randint(100, 200))
    var= bin(int(var)).replace("0b", "")

    return var

def create_saltBin(index):
    #just create some random characters (for only encoding, generated always)
    var=(rr.randint(0, 64))
    var= int((var/8.23)*(randomNum()/8.79))
    var = str(var)+str(randomNum())
    while len(var) < int(index):
        var = (var + str(randomNum()))
    var = bin(int(var))[2:int(index)]

    return var

def create_saltInt(index):
    #just create some random characters (for only encoding, generated always)
    var=(rr.randint(0, 64))
    var= int((var/8.23)*(randomNum()/8.79))
    var = str(var)+str(randomNum())
    while len(var) < int(index):
        var = (var + str(randomNum()))
    var = str(var)[:int(index)]

    return var

def create_saltStr(index):
    #generate random characters
    varB = create_saltBin(index*5)
    varS = convertSfB(varB, 0)
    while len(varS) < index:
        varB = varB + create_saltBin(index*5)
        varS = convertSfB(varB, 0)
    return varS[:index]

def convertStB(input, index):
    var = input
    #encode input (str) to binary
    var = ''.join(format(ord(char), '08b') for char in str(input))
    var = create_saltBin(int(index)) + var
    return var

def convertSfB(input, index):
    var = input
    var = var[int(index):]
    #decode input (bin) to string
    var = ''.join(chr(int(var[i:i+8], 2)) for i in range(0, len(var), 8))

    return var

def convertStI(input, index):
    var = input
    #encode input (str) to integer
    var = ''.join(format(ord(char), '08b') for char in str(input))
    var = int(var, 2)
    var = create_saltInt(int(index)) + str(var)

    return var
    
def convertSfI(input, index):
    var = input
    var = var[int(index):]
    binary = bin(int(var))[2:]
    binary = binary.zfill((len(binary) + 7) // 8 * 8)

    decoded_string = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        decimal = int(byte, 2)
        char = chr(decimal)
        decoded_string += char

    return decoded_string

def randomNum():
    # Use the current time as a seed value
    seed = int(time.time())
    # Algorithm parameters
    a = 1103515245
    c = 18446744073709551616
    m = 2**31
    # Generate pseudo-random number
    seed = (a * seed + c) % m
    var = ((seed / m) * 4096) / 0.128
    var = str(var)
    var = var.replace(".", "")
    var = int(var)

    return (var+7142128)

def encode(text, index):
    var = int(convertStI(text, 0))
    var *= 29
    var = convertSfI(var, 0)
    var = translate(var, translation_dict)
    var = create_saltInt(index) + str(var)

    return var

def decode(text, index):
    var = int(text[index:])
    var /= 29
    var = convertSfI(var, 0)

    return var

def random_translate():
    lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','á', 'é', 'í', 'ó', 'ö', 'ő', 'ú', 'ü', 'ű']
    uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','Á', 'É', 'Í', 'Ó', 'Ö', 'Ő', 'Ú', 'Ü', 'Ű']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_characters = ['!', '@', '#', '$', '%', '&', '*','<', '>', '?', '/', '|', '\\','~','^', ':', ';','!', '@', '#', '$', '%', '&', '*','<', '>', '?', '/', '|', '\\','~','^', ':', ';','!', '@', '#', '$', '%', '&']

    translation_dict = {}

    for i in lowercase_letters:
        choiceS = rr.choice(special_characters)
        special_characters.remove(choiceS)
        choiceU = rr.choice(uppercase_letters)
        uppercase_letters.remove(choiceU)
        curLtr = choiceS+choiceU+rr.choice(numbers)+rr.choice(numbers)
        translation_dict[i] = curLtr
    
    lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','á', 'é', 'í', 'ó', 'ö', 'ő', 'ú', 'ü', 'ű']
    uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','Á', 'É', 'Í', 'Ó', 'Ö', 'Ő', 'Ú', 'Ü', 'Ű']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_characters = ['!', '@', '#', '$', '%', '&', '*','<', '>', '?', '/', '|', '\\','~','^', ':', ';','!', '@', '#', '$', '%', '&', '*','<', '>', '?', '/', '|', '\\','~','^', ':', ';','!', '@', '#', '$', '%', '&']

    for i in uppercase_letters:
        choiceS = rr.choice(special_characters)
        special_characters.remove(choiceS)
        choiceU = rr.choice(lowercase_letters)
        lowercase_letters.remove(choiceU)
        curLtrU = choiceS+choiceU+rr.choice(numbers)+rr.choice(numbers)
        translation_dict[i] = curLtrU

    lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','á', 'é', 'í', 'ó', 'ö', 'ő', 'ú', 'ü', 'ű']
    uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','Á', 'É', 'Í', 'Ó', 'Ö', 'Ő', 'Ú', 'Ü', 'Ű']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_characters = ['!', '@', '#', '$', '%', '&', '*','<', '>', '?', '/', '|', '\\','~','^', ':', ';','!', '@', '#', '$', '%', '&', '*','<', '>', '?', '/', '|', '\\','~','^', ':', ';','!', '@', '#', '$', '%', '&']

    for i in numbers:
        choiceS = rr.choice(special_characters)
        special_characters.remove(choiceS)
        choiceU = rr.choice(numbers)
        numbers.remove(choiceU)
        curLtr = choiceS+choiceU+rr.choice(uppercase_letters)+rr.choice(lowercase_letters)
        translation_dict[i] = curLtr

    lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','á', 'é', 'í', 'ó', 'ö', 'ő', 'ú', 'ü', 'ű']
    uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','Á', 'É', 'Í', 'Ó', 'Ö', 'Ő', 'Ú', 'Ü', 'Ű']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_characters = ['!', '@', '#', '$', '%', '&', '*','<', '>', '?', '/', '|', '\\','~','^', ':', ';','!', '@', '#', '$', '%', '&', '*','<', '>', '?', '/', '|', '\\','~','^', ':', ';','!', '@', '#', '$', '%', '&']

    for i in special_characters:
        choiceS = rr.choice(special_characters)
        special_characters.remove(choiceS)
        choice1 = rr.choice(uppercase_letters)
        uppercase_letters.remove(choice1)
        choice2 = rr.choice(lowercase_letters)
        lowercase_letters.remove(choice2)
        choiceU=rr.choice(numbers)
        curLtrU = choiceS+choiceU+choice2+choice1
        translation_dict[i] = curLtrU

    return translation_dict

def translate(input, translation_dict):
    translated_string = ''
    for char in input:
        if char in translation_dict:
            translated_string += translation_dict[char]
        else:
            translated_string += char
    
    return translated_string

def translate_back(input_string, translation_dict):
    var = input_string
    for letter, new in translation_dict.items():
        var = str(var).replace(new, letter)
    return var

def ICEG64(input, index):
    var = translate(input, translation_dict)
    var = convertStI(var, 0)
    var = translate(var, translation_dict)

    salt = create_saltStr(index)
    salt = convertStI(salt, 0)
    salt = translate(salt, translation_dict)

    return salt[:index] + var

def deICEG64(input, index):
    var = input[index:]
    var = translate_back(var, translation_dict)
    var = convertSfI(var, 0)
    var = translate_back(var, translation_dict)

    return var

def ICEG64Fib(input, index):
    var = ICEG64(input, 0)
    fibvar = generate_fibonacci(len(var))
    for i in fibvar:
        var = var[:i] + create_saltStr(index) + var[i:]

    return create_saltStr(index)+var

def deICEG64Fib(input, index):
    var = input[index:]

def generate_fibonacci(x):
    fib_sequence = [0, 1]
    i = 2

    while fib_sequence[-1] < x:
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        i += 1

    return fib_sequence[:-1]

def ICEG32(input, index):
    var = translate(input, translation_dict)
    var = convertStI(var, 0)

    salt = create_saltStr(index)
    salt = convertStI(salt, 0)

    return salt[:index] + var

def deICEG32(input, index):
    var = input[index:]
    var = convertSfI(var, 0)
    var = translate_back(var, translation_dict)

    return var

def help():
    for i in range(10):
        print("\n")
    print("\t\t\t\t\t|  | |¯ |   |¯¯|\n\t\t\t\t\t|__| |- |   |¯¯'\n\t\t\t\t\t|  | |_ |__ |")
    print("\t\t\t\t-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
    print("Function keywords:")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    print("  • builtin - open built-in command menu")
    print("  • custom - open custom code editor")
    print("  • help - open this help page")
    print("\nBuilt-in command keywords:")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    print(" keyword\t\t|\t\tfunction\t\t|\t\tdescription ")
    for i in range(110):
        print("-", end="")
    print("")
    print("  key\t\t\t\t\tcreate_key()\t\t\tGenerate random binary characters. (not in use)")
    print("  saltB\t\t\t\t\tcreate_saltBin()\t\tGenerate index length random binary")
    print("  saltI\t\t\t\t\tcreate_saltInt()\t\tGenerate index length random integer")
    print("  saltS\t\t\t\t\tcreate_saltStr()\t\tGenerate index length random string")
    print("  e\t\t\t\t\tconvertStB()\t\t\tconvert string to binary, insert index length salt at the beginning")
    print("  d\t\t\t\t\tconvertSfB()\t\t\tconvert string from binary, cut index length salt from the beginning")
    print("  eI\t\t\t\t\tconvertStI()\t\t\tconvert string to integer, insert index length salt at the beginning")
    print("  dI\t\t\t\t\tconvertSfI()\t\t\tconvert string from integer, cut index length salt from the beginning")
    print("  _NONE_\t\t\t\trandomNum()\t\t\tgenerate a pseudo-random number, based on time")
    print("  encode\t\t\t\tencode()\t\t\tConvert string to integer, multiply it by 29, and translate it, than insert index length salt")
    print("  decode\t\t\t\tdecode()\t\t\tCut index lenght salt off, divide by 29 convert to string")
    print("  transNew\t\t\t\trandom_translate()\t\tCreate a random translate table (dictionary), with a pattern using upper/lowercase, numbers, and special charachters")
    print("  transT\t\t\t\ttranslate()\t\t\tTranslate string to a coded text using a constant dictionary (generated random before)")
    print("  transF\t\t\t\ttranslate_back()\t\tTranslate coded text to string using a constant dictionary (generated random before)")
    print("  ICE\t\t\t\t\tICEG64()\t\t\tTranslate string, convert it to integer, translate it again, insert index lenght salt")
    print("  deICE\t\t\t\t\tdeICEG64()\t\t\tRemove salt, transalte back, convert integer to string, translate it again")
    print("  ICEfib\t\t\t\tICEG64Fib()\t\t\t[NOT FINISHED YET!] translate it, convert it to integer, translate it, insert index length salt every fibonacci position")
    print("  deICEfib\t\t\t\tdeICEG64Fib()\t\t\t[NOT FINISHED YET!] Remove index lenght salt from every fibonacci position, transalate it back, convert string form integer, translate it back")
    print("  _NONE_\t\t\t\tgenerate_fibonacci()\t\tGenerate fibonacci numbers that are below X. Created for ICEG64fib")
    print("  ICE32\t\t\t\t\tICEG32()\t\t\tLighter version of ICEG64. Translate string, than convert it to integer. Insert index length salt to the beginning.")
    print("  deICE32\t\t\t\tgenerate_fibonacci()\t\tDecode ICEG32. Remove salt, convert integer to string, translate it back.")
    print("  q\t\t\t\t\t_NONE_\t\t\t\tExit built-in mode to function selecter.")
    for i in range(5):
        print("\n")