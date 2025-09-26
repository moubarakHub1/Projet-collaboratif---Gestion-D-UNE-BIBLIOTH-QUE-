def utilisateur_majeur(users):
    def fun_logique(user):
        if user[3] >= 18 :
            return True
        else:
            return False
    return list(filter(fun_logique,users))


def nom_complete_majuscules(users):
    logique = lambda user : f"{user[1]} {user[2]}".upper()    
    return list(map(logique,users))