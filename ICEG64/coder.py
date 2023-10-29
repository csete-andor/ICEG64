import ICEdocs
import webbrowser

print("\n© 2023 Csete Andor \nAll rights reserved!\nType 'help' to open help page\n")

def builtin():
    index = 16
    xvar = ""
    while True:
        var = input("text ")
        varY = input("method ")
        if varY == "q" or varY == "quit":
            break
        indexYN = input("modify salt? ["+str(index)+"] (y/n) ")
        if indexYN=="y":
            index = input()
        if varY == "e":
            xvar = ICEdocs.convertStB(var, int(index))
        elif varY == "d":
            xvar = ICEdocs.convertSfB(var, int(index))
        elif varY == "eI":
            xvar = ICEdocs.convertStI(var, int(index))
        elif varY == "dI":
            xvar = ICEdocs.convertSfI(var, int(index))
        elif varY == "encode":
            xvar = ICEdocs.encode(var, int(index))
        elif varY == "decode":
            xvar = ICEdocs.decode(var, int(index))
        elif varY == "transT":
            xvar = ICEdocs.translate(var, ICEdocs.translation_dict)
        elif varY == "transF":
            xvar = ICEdocs.translate_back(var, ICEdocs.translation_dict)
        elif varY == "saltB":
            xvar = ICEdocs.create_saltBin(int(index))
        elif varY == "saltI":
            xvar = ICEdocs.create_saltInt(int(index))
        elif varY == "saltS":
            xvar = ICEdocs.create_saltStr(int(index))
        elif varY == "key":
            xvar = ICEdocs.create_key()
        elif varY == "ICE":
            xvar = ICEdocs.ICEG64(var, int(index))
        elif varY == "deICE":
            xvar = ICEdocs.deICEG64(var, int(index))
        elif varY == "ICE32":
            xvar = ICEdocs.ICEG32(var, int(index))
        elif varY == "deICE32":
            xvar = ICEdocs.deICEG32(var, int(index))
        elif varY == "ICEfib":
            xvar = ICEdocs.ICEG64Fib(var, int(index))
        elif varY == "deICEfib":
            xvar = ICEdocs.deICEG64Fib(var, int(index))
        elif varY == "transNew":
            ICEdocs.random_translate()
        print(xvar)

while True:
    funct = input("Function: ")
    if funct == "builtin":
        builtin()
    elif funct == "custom":
        coding = True
        whole_code = []
        while coding:
            var = input()
            if var == ":save":
                xvar = ""
                for i in whole_code:
                    xvar = xvar+ i
                with open("ICEG64/customcode.py", "w") as file:
                    file.write("import ICEdocs as ICE\n"+xvar)
                coding = False
                try:
                    import customcode
                except:
                    print("\nThere was an error in you custom code. Please try again. \nYour code was:\n"+xvar)
            elif var == ":qa!":
                break
            elif var != ":qa!" and var != ":save":
                whole_code.append(var+"\n")
    elif funct == "run":
        try:
            import customcode
        except:
            print("\nThere was an error in you custom code. Please try again. \nYour code was:\n"+xvar+"\n")
    elif funct == "help":
        ICEdocs.help()
    elif funct == "webhelp":
        webbrowser.open("https://iceg-coder.static.domains")
    elif funct == "killall":
        exit()
    elif funct == "":
        builtin()
    else:
        print('No fucntion found called "'+funct+'"')