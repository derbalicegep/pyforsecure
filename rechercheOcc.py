# Renvoie les lettres les plus présentes dans un texte

def rechercheOcc(texte):
    listeOcc = list()

    for i in range(26):
        listeOcc += [[0, chr(i+65)]]

    texte = texte.upper()
    for i in texte:
        if 65 <= ord(i) <= 65+25:
            listeOcc[ord(i)-65][0] += 1

    renvoie = list()
    for _ in range(5):
        max = listeOcc[0][0]
        indice = 0
        for i in range(len(listeOcc)):
            if max < listeOcc[i][0]:
                max = listeOcc[i][0]
                indice = i
        renvoie += [listeOcc[indice]]
        del (listeOcc[indice])
    return (renvoie)

texte= str(input("Texte : "))
print (rechercheOcc(texte))


