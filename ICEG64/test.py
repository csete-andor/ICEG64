from ICEdocs import *

def ICEG64TEST(input, saltInput):
    var = translate(input, translation_dict)
    print(var, saltInput)
    var = convertStI(var, 0)
    print(var, saltInput)
    var = translate(var, translation_dict)
    print(var, saltInput)

    #salting
    salt = create_saltStr(saltInput)
    print(var, salt)
    salt = convertStI(salt, 0)
    print(var, salt)
    salt = translate(salt, translation_dict)
    print(var, salt)

    print(salt[:saltInput] + var)

def deICEG64TEST(input, saltInput):
    var = input[saltInput:]
    print(var, saltInput)
    var = translate_back(var, translation_dict)
    print(var, saltInput)
    var = convertSfI(var, 0)
    print(var, saltInput)
    var = translate_back(var, translation_dict)
    print(var, saltInput)

    print(var)

while True:
    funct=input("Funct ")
    if funct=="e":

        text=input("TEXT ")
        salt=input("SALT ")
        ICEG64TEST(text,int(salt))
    else:
        text=input("TEXT ")
        salt=input("SALT ")
        deICEG64TEST(text,int(salt))