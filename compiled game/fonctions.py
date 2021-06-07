def GrillePleine(a1,a2,a3,b1,b2,b3,c1,c2,c3):
    """cette fonction vous dit si la grille est pleine ou pas, si elle est pleine, le programme s'arrete.
    :param: a1,a2,a3,b1,b2,b3,c1,c2,c"""
    if a1!= "-" and a2!= "-" and a3!= "-" and b1!= "-" and b2!= "-" and b3!= "-" and c1!= "-" and c2!= "-" and c3 != "-":
        return True


def JeuGagne(a1,a2,a3,b1,b2,b3,c1,c2,c3):
    """cette fonction retourne si le jeu a été gagné ou pas. Si la partie est gagnée, le jeu s'arrete, sinon la fonction retourne 0
    :param: name,a1,a2,a3,b1,b2,b3,c1,c2,c3. donc le nom et les point occupés
    :return: jeu gagné par... ou 0"""
    if a1 == "X" and a2 == "X" and a3 == "X" or a1 == "O" and a2 == "O" and a3 == "O":
        return True

    elif b1 == "X" and b2 == "X" and b3 =="X" or b1 == "O" and b2 == "O" and b3 =="O":
        return True

    elif c1 == "X" and c2== "X" and c3 =="X" or c1 == "O" and c2== "O" and c3 =="O":
        return True

    elif a1== "X" and b1== "X" and c1 =="X" or a1== "O" and b1== "O" and c1 =="O":
        return True

    elif a2== "X" and b2== "X" and c2 == "X" or a2== "O" and b2== "O" and c2 == "O":
        return True

    elif a3== "X" and b3== "X" and c3 == "X" or a3== "O" and b3== "O" and c3 == "O":
        return True

    elif a1== "X" and b2== "X" and c3 =="X" or a1== "O" and b2== "O" and c3 =="O":
        return True

    elif a3== "X" and b2== "X" and c1 =="X" or a3== "O" and b2== "O" and c1 =="O":
        return True

    else:
        return False