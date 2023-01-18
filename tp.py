# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 13:03:07 2023

@author: paradoxe
"""

import copy

"""Passager

Un identifiant qui doit être unique
Un nom
Le poids de ses bagages

Bus

Un identifiant unique
Le nombre de place potentielle
Un tableau pouvant contenir des passages

En tant qu'administrateur, je veux créer des bus.
En tant qu'administrateur, je veux créer un passager
En tant qu'administrateur, je veux ajouter un passager à un bus
En tant qu'administrateur, je veux connaitre le nombre place disponible dans un bus
En tant qu'administrateur, je veux connaitre le nombre de kg reservé pour un bus
En tant qu'administrateur, je veux retirer un passager d'un bus
En tant qu'administrateur, je veux savoir si un bus peut accueillir les passagers provenant d'un autre bus
En tant qu'administrateur, je veux afficher la liste des passagers d'un bus dans la console
En tant qu'administrateur, je veux afficher l'ensemble des passagers de ma flotte de bus dans la console
En tant qu'administrateur, je veux savoir si un passager est enregistré 
---sur un bus de ma flotte. Si résultat positif,
---je souhaite afficher les détails de ce bus dans la console
"""
# parcourir les bus de la liste puis parcourir la liste des passagers
# contenue dans chaque bus

passagers = {
    "id": 11,
    "nom": "arial",
    "poidsBagage": 15}

bus = {
    "id": 1,
    "nombrePlace": 10,
    "listePassagers": [passagers]}

buses = [bus]
print(buses)


def vérificationId(busId):
    for bus in buses:
        if bus["id"] == busId:
            return True

    return False


def vérificationIdpass(Idpass):
    for bus in buses:
        # print(bus["listePassagers"])
        for elt in bus["listePassagers"]:
            if elt["id"] == Idpass:
                return True
           # return True
        # else:
            # return False


def placeRestantes(busId):
    for bus in buses:
        if bus["id"] == busId:

            print(bus["nombrePlace"]-len(bus["listePassagers"]))


def nombreKgDispo(busId):
    for bus in buses:  # on entre dans la liste des bus et pour chaque bus dans la liste,
        if bus["id"] == busId:  # si l'id de ce bus est égal à l'id passé en paramètre,
            poids = 0  # on instancit la variable de somme
            # on entre dans l'élément listePassagers de
            for passager in bus["listePassagers"]:
                # on se rend compte que c'est un dictionnaire d'élements propre à un passager puis on chercher l'élement dont la clé est poidsBagage et on l'utilise pour incrémenter la variable de compte
                poids += passager["poidsBagage"]
            # ensuite on désindente pour sortir de la boucle for et ainsi afficher le résultat final de la variable de compte
            print(poids)


def ajouterPassagerBus():
    passagern = copy.deepcopy(passagers)
    passagern["id"] = int(input("entrez l'id du passager\n"))
    while vérificationIdpass(passagern["id"]):
        passagern["id"] = int(input("entrez l'id du passager\n"))

    passagern["nom"] = str(input("entrez le nom du passager\n"))
    passagern["poidsBagage"] = int(
        input("entrez les poids bagage du passager\n"))
    listeId = ""
    for bus in buses:
        print(str(bus["id"]), "\n", type(str(bus["id"])))
        listeId += str(bus["id"])+" , "
    print("dans quel bus voulez-vous l'ajouter:\n \t\t liste des id de bus\n \t\t", listeId)
    busId = int(input())
    for bus in buses:
        if bus["id"] == busId:
            bus["listePassagers"].append(passagern)
            print(bus)
    restart = int(input("voulez-vous ajouter un autre passager?"))
    if (restart == 1):
        ajouterPassagerBus()


def createBus():
    busn = copy.deepcopy(bus)
    busn["id"] = int(input("entrez l'id du bus\n"))
    while vérificationId(busn["id"]):
        busn["id"] = int(input("entrez l'id du bus\n"))

    busn["nombrePlace"] = int(input("entrez le nombre de place dans le bus\n"))
    busn["listePassagers"] = []
    buses.append(busn)
    i = int(input("voulez-vous continuer?\n"))
    while i == 1:
        busn2 = copy.deepcopy(bus)
        busn2["id"] = int(input("entrez l'id2 du bus\n"))
        while vérificationId(busn2["id"]):
            busn["id"] = int(input("cet id existe deja entrez l'id du bus\n"))

        busn["nombrePlace"] = int(
            input("entrez le nombre de place dans le bus\n"))
        busn["listePassagers"] = []
        buses.append(busn.copy())

        # i=int(input("voulez-vous continuerx2?"))
        i = int(input("voulez-vous continuerx3?\n"))

    print("vous avez ajouté en tout", len(buses), " bus\n")

    # abuses.append(busn)


# vérificationIdpass(1)
# createBus()
ajouterPassagerBus()
# ajouterPassagerBus()
# ajouterPassagerBus()
# nombreKgDispo(1)
