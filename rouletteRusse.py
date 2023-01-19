# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 09:25:19 2023

@author: paradoxe
"""
import random

bourse=200
mise=200
listeRandom=[]
for i in range(0,29):
    listeRandom.append(i)

print("Vous possedez ",bourse,"\n voulez vous commencer à jouer?\n\t\t mise 200f\n")
start=str(input())
while start=="oui":
    
    if bourse>=mise:
        nombre=int(input("choisissez votre chiffre\n"))
        while nombre not in listeRandom:
            nombre=int(input("Mauvaise saisie choisissez votre chiffre\n"))
        hazard=random.randint(0, 29)
        print("et le nombre gagnant est le \n \t\t ",hazard)
        parite=hazard%2
        if nombre==hazard:
            bourse+=mise
            print("féllicitation vous gagnez 200f et désormais vous possedez",bourse,"f\nVoulez-vous rejouer?")
            start=str(input())
        elif nombre%2 == parite:
            bourse-=(mise/2)
            print("malheureusement votre chiffre n'est pas le bon mais vous gagnez la parité\net désormais vous possedez",bourse,"\n Voulez-vous rejouer?")
            start=str(input())
            
        else:
            bourse-=200
            print("Vous avez perdu\n et avez été débité de 200\n Bourse restante: " ,bourse,"\n Voulez-vous rejouer?")
            start=str(input())
    else:    
        print("Votre solde est insuffisant")
        start=="non"
        break
        
print("A bientot")