# Cryptage César

# Fonction de décalage d'un caractère dans l'alphabet
def decalage(caract, dis):

    if 65 <= ord(caract) <= 90:
        return (chr(((ord(caract)-65)+dis) % 26 + 65))

    if 97 <= ord(caract) <= 122:
        return (chr(((ord(caract)-97)+dis) % 26 + 97))

    return (chr(ord(caract)+dis))


def crypterConstant(texte, dec):

    renvoi = ""
    for i in texte:
        if i == ' ':
            renvoi += ' '
        elif i == "'":
            renvoi += "'"
        elif i == "-":
            renvoi += "-"
        elif i == ".":
            renvoi += "."
        else:
            renvoi += decalage(i, dec)
    return (renvoi)


def decrypterConstant(texte, dec):

    return (crypterConstant(texte, 26-dec))


texte = input("Message a decrypter : ")
dec = int(input("Decalage : "))
print("\n")
print("Message original : {}".format(decrypterConstant(texte, dec)))
