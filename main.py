import numpy as np
import pandas as pnd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
from sklearn.linear_model import LinearRegression

#Initialisation des données
data_path  = 'demo-naiss-nbre-taux.xlsx'
dataframe = pnd.read_excel(data_path)
dataframe = dataframe[['Annee', 'Nombre de naissances vivantes', 'Taux de natalite (pour 1 000 habitants)', 'Variation par rapport a l annee precedente']]

#Attribution des données à annalyser
X=dataframe[['Annee']]
y=dataframe[['Taux de natalite (pour 1 000 habitants)']]

#Trace un graphique simple
plt.plot(X, y)
#Ajout d'une ligne d'ajustement optimal
linear = LinearRegression()
linear.fit(X, y)
y_pred = linear.predict(X)
plt.plot(X, y_pred, color='red')

plt.scatter(X, y)
plt.xlabel('Annee')
plt.ylabel('Taux de natalite (pour 1 000 habitants)')
print('coeff.: ', linear.coef_)
print('b: ', linear.intercept_)

#Ajout d'un diagram en baton de la variation du taux pour chaque année
sns.catplot(data=dataframe, kind="bar", x="Annee", y="Variation par rapport a l annee precedente")

#Rendu et affichage des graphiques
plt.show()

#Création du graphique de l'univers
pie=np.array([23/39, 10/39, 6/39])
plt.pie(pie)
plt.show()