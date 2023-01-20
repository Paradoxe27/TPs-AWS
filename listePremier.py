# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 12:27:14 2023

@author: paradoxe
"""

listePremier=[1]
def nombrePremier():
    nombreTotal=int(input("jusqu'a quel nombre souhaitez vous obtenir les valeur premières\n"))
    for number in range(2,nombreTotal):
        #print(number)
        final=1
        for number2 in range(2,number):
            #print(number2)
            if number%number2!=0:
                #print(number)
                verif=1
            else:
                verif=0
           
            final=final*verif
            if final==0:
                break
        if final==1:
            listePremier.append(number)
                
    save=input("Voulez-vous saugarder cette liste dans un fichier? \n appuyez sur y pour valider ou toute autre touche pour refuser\n")
    if save=="y":
        name=input("quel nom voulez-vous donner à ce fichier?\n")
        file= open("C:/Users/paradoxe/Desktop/AWS/"+name+".txt", 'w')
        
        for numberPrems in listePremier:
            file.write(str(numberPrems)+",")
            
        file.close()
    else:
        print("vous ne voulez pas l'enregistrer Okay...Cependant voila le résultat:\n")
        print(listePremier)
           
                

                
                
nombrePremier()