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


def utilisateur_livres(users,books):
    def fun_logique(user):
        fav_books = []
        for book in books:
            if user[0] == book[0]:
                fav_books.append(book[1])
        return dict( name = f"{user[1]} {user[2]}".upper() , age = user[3] , fav_books = fav_books )

    return list(map(fun_logique,users))


def to_string(users_fav_books):
    
    for user in users_fav_books:
        books = ""
        for book in user["fav_books"]:
            if len(book) != 0:
                books += " , " + book
        print(f"{user["name"]} ({user["age"]} ans) {books}")
