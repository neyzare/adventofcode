def jour_2():
    rapport_sure = 0
    rapport_pas_sure = 0

    try:
        with open('jour-2', 'r') as f:
            lignes = f.readlines()

        if not lignes:
            print("Le fichier est vide.")
            return

        for ligne in lignes:
            colonne = ligne.strip().split()
            colonne = [int(val) for val in colonne]


            differences = [colonne[i + 1] - colonne[i] for i in range(len(colonne) - 1)]


            differences_valides = all(1 <= abs(diff) <= 3 for diff in differences)


            direction_uniforme = all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences)


            if differences_valides and direction_uniforme:
                print(f"Rapport sûr : {colonne}")
                rapport_sure += 1
            else:
                print(f"Rapport pas sûr : {colonne}")
                rapport_pas_sure += 1

        print(f"\nRapports sûrs total : {rapport_sure}")
        print(f"Rapports pas sûrs total : {rapport_pas_sure}")

    except FileNotFoundError:
        print("Le fichier 'jour-2' est introuvable. Veuillez vérifier son emplacement ou son contenu.")
    except ValueError as e:
        print(f"Erreur de conversion des données : {e}")

jour_2()