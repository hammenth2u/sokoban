# sokoban

Nom: Clara



Programme à rendre sur git pour 17h (dernier push)

Le but est de créer un sokoban en python avec la lib curses comme on a vu.

Nous devons prendre une map en paramètre qui doit être fermée!(toutes tailles possibles)
Avec un seul Joueur -> Par un P -> sinon erreur
Autant de boxe que d'emplacement -> une box X et un emplacement O
Sinon cas d'erreur

Pensez à faire des classes !!

Quand on appuie sur espace on reset la map de départ
Quand on appuie sur echap on quitte ou sur q on quitte

Gérez les conditions de victoire et les conditions de défaite
Le joueur ne doit pas sortir de la map et une box aussi
Gérez le KeyboardInterrupt avec les excepts!

nombre de coup fait par le joueur
La map doit contenir que des espaces \n des #,X,0,P

un -h (help) quand vous donnez en paramètre à la place d'un fichier
avec l'usage et une description du programme

Unit test avec pytest
Des commits clean!

Bonus:

Créez un menu pour choisir pour selectionner des différentes maps pré-chargées
Sauvegardez un high score dans un fichier
Mettre un chronomètre
Et toutes sortes de bonus sont acceptées!

Générateur de map


Barème

Gestion des erreurs(joueur et maps) : 4 points
    Il y aura plusieurs stades de gestion d'erreur

Condition de victoire et défaite 4 points
    Il y aura plusieurs stades de victoire et défaites
Jouabilité (sans lag) 2 points
    avec les touches que nous avons définis

Arbre git(Pushs réguliés et bien définis) 2 points
Code propre ! 4 points
si vous respectez une norme etc etc bien separer

Test 2 points
    Si les tests sont pertinants ou pas
    S'il couvre un certain niveau de %

Bonus à voir suivant celui qui a été choisi (ou plusieurs)