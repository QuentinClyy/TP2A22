from personnages import charger_personnages


def possede(donnees_personnage, type_caracteristique, valeur_caracteristique):
    """
    Indique si la valeur de caractéristique fait partie des données du personnage.

    Attention! Si le type de caractéristique est accessoires ou pilosite, il faut vérifier
    que la valeur cherchée EST DANS les données du personnage pour ce type, tandis que
    si le type est autre chose, il faut vérifier que la valeur cherchée EST la donnée du personnage
    pour ce type.

    Args:
        donnees_personnage (dict): Les données (sous forme type:valeur) pour un personnage
        type_caracteristique: Le type de caractéristique analysé
        valeur_caracteristique: La valeur de la caractéristique recherchée

    Returns:
        bool: True si le personnage possède la caractéristique, False sinon.
    """
    # VOTRE CODE ICI
    if type_caracteristique in ["accessoires", "pilosite"]:
        return valeur_caracteristique in donnees_personnage[type_caracteristique]
    else:
        return valeur_caracteristique == donnees_personnage[type_caracteristique]


def mettre_a_jour_hypotheses(personnages_restants, type_caracteristique, valeur_caracteristique, reponse):
    """
    Retourne un dictionnaire basé sur le dictionnaire de personnages restants en paramètre, dans
    lequel on enlève les personnages qui possèdent ou ne possèdent pas la caractéristique en paramètres.

    Args:
        personnages_restants (dict): Les personnages préalablement restants
        type_caracteristique (string): Le type de la caractéristique dont on
                                       veut conserver/enlever ceux qui l'ont
        valeur_caracteristique (string): La valeur de la caractéristique dont
                                   on veut conserver/enlever ceux qui l'ont
        reponse (bool): True si on doit conserver les personnages qui possèdent la caractéristique,
                        False si on doit conserver ceux qui ne la possèdent pas.

    Note: cette fonction devrait appeler la fonction possede.

    Returns:
        dict: Le dictionnaire de personnages restants mis à jour.
    """
    # VOTRE CODE ICI
    possede_perso = []
    not_possede_perso = []
    personnages_restants_copy = personnages_restants.copy()

    for perso, donnees in personnages_restants_copy.items():
        if possede(donnees, type_caracteristique, valeur_caracteristique):
            possede_perso.append(perso)
        else:
            not_possede_perso.append(perso)
    if reponse:
        for k in not_possede_perso:
            personnages_restants_copy.pop(k)
    if not reponse:
        for k in possede_perso:
            personnages_restants_copy.pop(k)

    return personnages_restants_copy



# Tests de la fonction score_dichotomie
personnages = {'Bernard': {'genre': 'homme', 'accessoires': ['chapeau']},
               'Claire': {'genre': 'femme', 'accessoires': ['chapeau']},
               'Eric': {'genre': 'homme', 'accessoires': ['chapeau']},
               'George': {'genre': 'homme', 'accessoires': ['chapeau']},
               'Maria': {'genre': 'femme', 'accessoires': ['chapeau']}}

# Tests de la fonction mettre_a_jour_hypotheses
assert len(mettre_a_jour_hypotheses(personnages, 'genre', 'homme', True)) == 3
assert len(mettre_a_jour_hypotheses(personnages, 'genre', 'homme', False)) == 2

personnages_restants = charger_personnages()
print(mettre_a_jour_hypotheses(personnages_restants, 'genre', 'homme', True))
print(mettre_a_jour_hypotheses(personnages_restants, 'genre', 'homme', False))