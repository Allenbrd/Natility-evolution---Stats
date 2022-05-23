# Maths et statistiques - Graphiques
#Par Allen Bridi le 23/05/2022

### 1ère étape - Importation des librairies naicessaires ###

import numpy as np # Librairie utile pour le traitement de tableaux
import pandas as pnd # Librairie utile pour l'importation et l'interpretation de fichiers excels
import seaborn as sns # Librairie utile pour la génération de graphiques
import matplotlib.pyplot as plt # Librairie utile pour la génération de graphiques
from sklearn.linear_model import LinearRegression # Librairie utile pour la génération automatique de fonctions linéaire à partir d'une courbe

### 2ème étape - Initialisation des données ###

data_path  = 'demo-naiss-nbre-taux.xlsx' # Indication du nom du tableau excel
dataframe = pnd.read_excel(data_path) # Interpretation et stockage des valeurs du tableau
#Dans la ligne ci-dessous on séléctionne uniquement les colonnes qui nous intéressent
dataframe = dataframe[['Annee', 'Nombre de naissances vivantes', 'Taux de natalite (pour 1 000 habitants)', 'Variation par rapport a l annee precedente']]

### 3ème étape - Création de la courbe ###

#On place les Années en abscisse
X=dataframe[['Annee']]
#On place le Taux de natalité en ordonnée
y=dataframe[['Taux de natalite (pour 1 000 habitants)']]

#On initialise une courbe simple des données avec les abscisses et ordonnées indiqués précédemment
plt.plot(X, y)

#On trace sur le graphique une représentation linéaire de la courbe (axe rouge sur le graphique)
linear = LinearRegression()
linear.fit(X, y)
y_pred = linear.predict(X)
#On met l'axe linéaire en rouge
plt.plot(X, y_pred, color='red')

#On ajoute un titre à l'axe des ordonnées et à l'axe des abscisses
plt.xlabel('Annee')
plt.ylabel('Taux de natalite (pour 1 000 habitants)')

### 4ème étape - Création du diagramme en batons ###

sns.catplot(data=dataframe, kind="bar", x="Annee", y="Variation par rapport a l annee precedente")

### 5ème étape - Rendu de la courbe et du diagramme en baton ###

plt.show()

### 6ème étape - Création et rendu de la réprésentation circulaire de l'univers ###

pie=np.array([23/39, 10/39, 6/39]) #Initialisation de la liste des probabilités des partitions de notre univers
plt.pie(pie) #Création d'un diagramme circulaire
plt.show() #Rendu et affichage de la représentation circulaire de l'univers