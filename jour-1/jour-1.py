def calculer_distance_totale(fichier):
    with open(fichier, "r") as f:
        lignes = f.readlines()


    tableauGauche = []
    tableauDroit = []

    for ligne in lignes:
        gauche, droite = map(int, ligne.strip().split())
        tableauGauche.append(gauche)
        tableauDroit.append(droite)


    tableauGauche.sort()
    tableauDroit.sort()


    ecarts = [abs(g - d) for g, d in zip(tableauGauche, tableauDroit)]


    distance_totale = sum(ecarts)


    print("Tableau gauche trié :", tableauGauche)
    print("Tableau droit trié :", tableauDroit)
    print("Écarts :", ecarts)
    print("Distance totale :", distance_totale)

    return distance_totale



fichier_test = "jour-1"
calculer_distance_totale(fichier_test)