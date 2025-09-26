from data import utilisateurs , aime_livres
from users import utilisateur_majeur , utilisateur_livres , nom_complete_majuscules


# tester fonction utilisateur_majeur qui filter par age
# print(utilisateur_majeur(utilisateurs))

# tester fonction Formater les noms complets en majuscules
# print(nom_complete_majuscules(utilisateurs))

# tester fonction Créer un dictionnaire associant chaque utilisateur à ses livres aimés
print(utilisateur_livres(utilisateurs,aime_livres))