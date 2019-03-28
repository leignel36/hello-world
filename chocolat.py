
class Chocolat:

	def __init__(self, nom, marque, poids, prix, cal100):
        	self.nom = nom
		self.marque=marque
		self.poids=poids
		self.prix=prix
		self.cal100=cal100

#poids en grammes
#prix pour une tablette
#cal100 nombre de calories pour 100g

	def montant_courses(ListeCourses):
		cost=0.0
		for l in ListeCourses :
			cost += l[0].prix*l[1]
		return(cost)

	def totalCalories(self, quantite):
		return(self.cal100 *quantite/100)


	


class chocolat_blanc(Chocolat):


	
	def __init__(self, nom, marque, poids, prix, cal100, pourcentagegraisse):
		Chocolat.__init__(self,nom, marque, poids, prix, cal100)
		self.couleur="blanc"
		self.pourcentagegraisse=pourcentagegraisse

	def le_plus_gras(self, liste_chocolat):
		taux_graisse=0.0
		chocolat_retenu=liste_chocolat[0]
		
		for c in liste_chocolat:
			if taux_graisse ==0.0:
				taux_graisse=c.pourcentagegraisse
				chocolat_retenu=c
			if taux_graisse <= c.pourcentagegraisse:
				taux_graisse=c.pourcentagegraisse
				chocolat_retenu=c
		return chocolat_retenu
	
	def le_moins_gras(self, liste_chocolat):
		taux_graisse=0.0
		chocolat_retenu=liste_chocolat[0]
		
		for c in liste_chocolat:
			if taux_graisse ==0.0:
				taux_graisse=c.pourcentagegraisse
				chocolat_retenu=c
			if taux_graisse >= c.pourcentagegraisse:
				taux_graisse=c.pourcentagegraisse
				chocolat_retenu=c

		return chocolat_retenu


class chocolat_noir(Chocolat):

#dans cette nouvelle classe, on ajoute la couleur du chocolat et son pourcentage
	def __init__(self, nom, marque, poids, prix, cal100, pourcentage):
		Chocolat.__init__(self, nom, marque, poids, prix, cal100)
		self.couleur="noir"
		self.pourcentage=pourcentage

	
	def chocolat_le_moins_cher( self, liste_chocolat, pourcentage):
		cost=0.0
		chocolat_retenu=liste_chocolat[0]

		for i in liste_chocolat:
			c=0.0
			if i.pourcentage == pourcentage:
				c=i.prix *100 / i.poids
				if cost==0.0:
					cost=0
					chocolat_retenu=i
				elif c<= cost:
					cost=c
					chocolat_retenu=i
	
		return chocolat_retenu


	def chocolat_le_plus_cher( self, liste_chocolat, pourcentage):
		cost=0.0
		chocolat_retenu=liste_chocolat[0]

		for i in liste_chocolat:
			c=0.0
			if i.pourcentage == pourcentage:
				c=i.prix *100 / i.poids
				if cost==0.0:
					cost=0
					chocolat_retenu=i
				elif c>= cost:
					cost=c
					chocolat_retenu=i
	
		return chocolat_retenu

#main
if __name__ == '__main__':
	cotedornoir=chocolat_noir('cotedornoir', 'cote dor', 200, 1.66, 530, 56)
	cotedornoirnoisette=chocolat_noir('cotedornoirnoisette', 'cote dor', 200, 2.18, 570, 46)
	cotedorlait=chocolat_noir('cotedorlait', 'cote dor', 200, 1.79, 540, 33)
	lindt85=chocolat_noir('lindt85', 'lindt', 100, 1.69, 580, 85)
	extrafin=chocolat_noir('extrafin', 'lindt', 100, 1.90, 545, 34)
	lindt99=chocolat_noir('lindt99', 'lindt', 50, 2.40, 590, 99)
	crunch=chocolat_blanc("crunch", "nestle", 100, 2.19, 527, 50)
	galak=chocolat_blanc("galak", "nestle", 100, 1.77, 546, 52)
	milka=chocolat_noir('milka', 'milka', 200, 1.51, 530, 32)

	liste_chocolat=[cotedornoir,cotedornoirnoisette, cotedorlait,lindt85, extrafin, lindt99, crunch, galak, milka]

	liste_choco_blanc=[galak,crunch]

	liste_choco_noir=[cotedornoir,cotedornoirnoisette, cotedorlait,lindt85, extrafin, lindt99, milka]

	print("le chocolat blanc le plus gras est", crunch.le_plus_gras(liste_choco_blanc).nom )

	print("le chocolat blanc le moins gras est", crunch.le_moins_gras(liste_choco_blanc).nom )

	print("le chocolat noir le moins cher est", milka.chocolat_le_moins_cher( liste_choco_noir, 85).nom)



#NB on cree ici des methodes qui pourraient tres bien etre crees en dehors des classes. cependant, on decide de proceder ainsi, il ne faut donc pas oublier de mettre self en argument, et de prendre un element quelconque a placer devant le nom de la methode lorsqu'on fait appelle a celle ci.


