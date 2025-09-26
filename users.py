def utilisateur_majeur(users):
    def fun_logique(user):
        if user[3] >= 18 :
            return True
        else:
            return False
    return list(filter(fun_logique,users))