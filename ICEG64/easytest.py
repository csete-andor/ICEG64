def convertSfI(StrInput, StrSalt):
    var = StrInput
    var = var[int(StrSalt):]
    binary = bin(int(var))[2:]
    binary = binary.zfill((len(binary) + 7) // 8 * 8)

    decoded_string = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        decimal = int(byte, 2)
        char = chr(decimal)
        decoded_string += char

    return decoded_string
