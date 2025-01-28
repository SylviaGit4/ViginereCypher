chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
         "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


# Draws out the 26x26 matrix of alphabetical characters, with each row shifted-
# -1 from the previous.
def drawSquare():
    vigSquare = []
    for i in range(26):
        templist = chars
        if i != 0:
            temp = chars[:i]
            templist = templist + temp
            del templist[:i]
        vigSquare.append(templist)
    return vigSquare


table = drawSquare()  # Creates the matrix.


def cypherEncrypt():
    cypherText = ""
    key = ""
    while True:
        print("\nText to encrypt? No numbers or special characters.")
        plainTxt = input("Text: ").upper()
        plainTxt.replace(" ", "")
        if plainTxt.isalpha() is True:
            break
        else:
            print("Invalid Input.")
    textLen = len(plainTxt)

    while True:
        print("Key to encrypt? No numbers or special characters.")
        keyTxt = input("Key: ").upper()
        keyTxt.replace(" ", "")
        if keyTxt.isalpha() is True:
            break
        else:
            print("Invalid Input.")
    keyLen = len(keyTxt)

    # Modifies the key to be the length of the text.
    if keyLen == textLen:
        key = keyTxt
    elif keyLen > textLen:
        key = keyTxt[:textLen]
    elif textLen > keyLen:
        modTime = textLen // keyLen
        # Modification times, how many times the text is repeated.
        if modTime == 1:
            key = (key + keyTxt)
        else:
            for i in range(modTime):
                key = (key + keyTxt)
        key = key[:textLen]

    # Accesses the matrix and creates the cypher text.
    for i in range(textLen):
        row = chars.index(plainTxt[i])
        column = chars.index(key[i])
        textInput = table[row][column]
        cypherText = cypherText + textInput
    print(f"\nThe encrypted text is: {cypherText}")


def cypherDecrypt():
    plainTxt = ""
    key = ""
    while True:
        print("\nText to decrypt? No numbers or special characters.")
        cypherTxt = input("CypherText: ").upper()
        cypherTxt.replace(" ", "")
        if cypherTxt.isalpha() is True:
            break
        else:
            print("Invalid Input.")
    cypherLen = len(cypherTxt)

    while True:
        print("Key to decrypt? No numbers or special characters.")
        keyTxt = input("Key: ").upper()
        keyTxt.replace(" ", "")
        if keyTxt.isalpha() is True:
            break
        else:
            print("Invalid Input.")
    keyLen = len(keyTxt)

    # Modifies the key to be the length of the cypher.
    if keyLen == cypherLen:
        key = keyTxt
    elif keyLen > cypherLen:
        key = keyTxt[:cypherLen]
    elif cypherLen > keyLen:
        modTime = cypherLen // keyLen
        # Modification times, how many times the text is repeated.
        if modTime == 1:
            key = (key + keyTxt)
        else:
            for i in range(modTime+1):
                key = (key + keyTxt)
        key = key[:cypherLen]

    for i in range(cypherLen):
        for row in range(26):
            textInput = ""
            column = chars.index(key[i])
            if cypherTxt[i] == table[row][column]:
                textInput = table[row][0]
            plainTxt = plainTxt + textInput
    print(f"\nThe decrypted text is: {plainTxt}")


def main():
    while True:
        print("'Encrypt', 'Decrypt', 'Display' the cypher table or 'Exit'?")
        choice = input("Selection: ").lower()
        if choice == "encrypt":
            cypherEncrypt()
        elif choice == "decrypt":
            cypherDecrypt()
        elif choice == "display":
            print("\nPrinting table.\n")
            for i in range(26):
                print(table[i])
        elif choice == "exit":
            break
        else:
            print("Invalid input.")


main()
