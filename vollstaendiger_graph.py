#!/usr/bin/python3
import matplotlib.pyplot as plt
import networkx as nx

def graph_gen(knoten,tup):
    G=nx.Graph()            #Graph Objekt
    G.add_node(knoten)      #Knoten anzahl hinzufügen
    G.add_edges_from(tup)   #Kanten aus den Tupeln hinzufügen
    nx.draw(G,with_labels=True) #ausgabe von Labels auf dem Graphen
    plt.savefig("simple_path.png") # save as png
    plt.show() #print out

#Tupel generierung
def tupel_gen(tup,knoten):
    n=knoten
    tup += [(n,n-1)] # Verbindung des letzten Knotens mit dem Vorgänger und Speichern in Tupel
    for j in range(1,n): # Knoten Anzahl durchgehen
             i = n-1    #schleifen dekrementierung
             if(j == 1): #Wenn die Knoten Anzahl gleich 1 ist dann den initial case 1
                 tup += [(1,1)] # das tupel für 1 Knoten
             while i != 1:      # i läuft bis 1
                i=i-1           #schleifen dekrementierung
                tup += [(n-j+1,n-i-1)] #generierz die tupel anzahl entsprechend der Knoten und der Vorgänger
                #tup += [(i,i)]
    print ("Kanten:",tup)

#Rekurrent Kanten Berechnung
def edges(n,elist,knoten):
    if n == 1: # Wenn n == 1 dann wird platz für einen wert reserviert
        elist.append(0)     #
        elist[1] = 0        # Die initial Bedingung elist[1] = 0
        edges(n+1,elist,knoten)    # Aufruf der Funktion mit erhöhen
    elif n == 0:            #
        elist.append(0)     # Wenn die Liste gleich leer, dann Funktionsaufruf
        edges(n+1,elist,knoten)    # Anfangsbedingung
    elif n >= 2 and n != knoten+1:     # Abbruch und Ausführbedingung abbr+1 da rekurrenz sonst 1 weniger läuft
            elist.append(0)
            elist[n] = elist[n-1] + n-1     # Recurrence
            edges(n+1,elist,knoten)
            #print(n)                        #Ausgabe der Werte bei Rückkehr aus Rekursion
            return 0                        #Funktionsaufruf

###############################################################################
tup = []              # Tupel liste
elist=[]              # Generieren der Liste
#print(res)
print("Wie viele Knoten:")
knoten = input()                # Eingabe Anzahl der Knoten

res = edges(0,elist,int(knoten)) #Aufruf der Recursiven Funktion, Wert abbr gibt die Abbruchbedingung für die Rekurrenz
tupel_gen(tup,int(knoten))      # Generierung der Tupelelemente
graph_gen(knoten,tup)           # Generierung des Graphen
print("Anzahl der Kanten:",elist[int(knoten)])                    # Ausgabe der generierten Kanten Liste
